import json

import stripe
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, reverse
from django.views.decorators.http import require_POST

from bag.contexts import bag_contents
from products.models import Product
from profiles.forms import UserProfileForm
from profiles.models import UserProfile

from .forms import OrderForm
from .models import Order, OrderLineItem

stripe.api_key = settings.STRIPE_SECRET_KEY


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get("client_secret").split("_secret")[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(
            pid,
            metadata={
                "bag": json.dumps(request.session.get("bag", {})),
                "save_info": request.POST.get("save_info"),
                "username": (
                    request.user.username
                    if request.user.is_authenticated
                    else "Anonymous"
                ),
            },
        )
        return HttpResponse(status=200)
    except Exception as e:
        print(f"Error processing payment: {e}")
        messages.error(
            request,
            "Sorry, your payment cannot be processed right now. "
            "Please try again later.",
        )
        return HttpResponse(
            content=str(e), content_type="text/plain", status=400
        )


def get_numeric_id(combined_id):
    return int(combined_id.split("_")[0])


def checkout(request):
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe_public_key = settings.STRIPE_PUBLIC_KEY

    if request.method == "POST":
        bag = request.session.get("bag", {})
        form_data = {
            "full_name": request.POST["full_name"],
            "email": request.POST["email"],
            "phone_number": request.POST["phone_number"],
            "country": request.POST["country"],
            "postcode": request.POST["postcode"],
            "town_or_city": request.POST["town_or_city"],
            "street_address1": request.POST["street_address1"],
            "street_address2": request.POST.get("street_address2", ""),
            "county": request.POST.get("county", ""),
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()

            for item_id, item_data in bag.items():
                numeric_id = get_numeric_id(item_id)
                product = get_object_or_404(Product, pk=numeric_id)
                quantity = item_data["quantity"]
                customization = request.session.get(
                    f"customization_{numeric_id}",
                    {"first_name": "", "last_name": "", "voucher_type": ""},
                )
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity,
                    first_name=customization.get("first_name", ""),
                    last_name=customization.get("last_name", ""),
                    voucher_type=customization.get("voucher_type", ""),
                )
                order_line_item.save()

            request.session["save_info"] = "save-info" in request.POST
            return redirect(
                "checkout_success", order_number=order.order_number
            )
        else:
            messages.error(
                request,
                "There was an error with your form."
                "Please double check your information.",
            )
    else:
        bag = request.session.get("bag", {})
        if not bag:
            messages.error(
                request, "There's nothing in your bag at the moment."
            )
            return redirect(reverse("products"))

        current_bag = bag_contents(request)
        total = current_bag["grand_total"]
        stripe_total = round(total * 100)
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(
            request,
            "Stripe public key is missing. "
            "Did you forget to set it in your environment?",
        )

    template = "checkout/checkout.html"
    context = {
        "order_form": order_form,
        "stripe_public_key": stripe_public_key,
        "client_secret": intent.client_secret,
        "bag_items": current_bag["bag_items"],
        "meta_description": "Proceed to checkout and complete your purchase.",
    }

    return render(request, template, context)


def checkout_success(request, order_number):
    save_info = request.session.get("save_info")
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        order.user_profile = profile
        order.save()

        if save_info:
            profile_data = {
                "default_phone_number": order.phone_number,
                "default_country": order.country,
                "default_postcode": order.postcode,
                "default_town_or_city": order.town_or_city,
                "default_street_address1": order.street_address1,
                "default_street_address2": order.street_address2,
                "default_county": order.county,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    messages.success(
        request,
        f"Order successfully processed! Your order number is {order_number}. "
        f"A confirmation email will be sent to {order.email}.",
    )

    if "bag" in request.session:
        del request.session["bag"]

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "meta_description": "Order successfully processed. View your order details.",
    }
    return render(request, template, context)
