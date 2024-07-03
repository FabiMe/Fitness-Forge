from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import UserProfile
from .forms import UserProfileForm
from wishlist.models import Wishlist
from checkout.models import Order
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        logger.debug("Form submitted with data: %s", request.POST)
        if form.is_valid():
            user = form.save()
            logger.debug("User created successfully: %s", user.username)
            login(request, user)
            try:
                send_mail(
                    "Welcome to Fitness Forge",
                    "Thank you for signing up.",
                    DEFAULT_FROM_EMAIL,
                    [user.email],
                    fail_silently=False,
                )
                logger.info("Welcome email sent to %s", user.email)
            except Exception as e:
                logger.error("Error sending email: %s", e)
            return redirect("some_success_url")
        else:
            logger.debug("Form is not valid. Errors: %s", form.errors)
    else:
        form = UserCreationForm()
    context = {
        "form": form,
        "meta_description": "Sign up for an account at Fitness Forge to start your fitness journey.",
    }
    return render(request, "profiles/signup.html", context)


@login_required
def profile(request):
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == "POST":
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully")
            return redirect("profile")
        else:
            messages.error(request, "Update failed. Please ensure the form is valid.")
    else:
        form = UserProfileForm(instance=profile)

    orders = profile.orders.all()
    wishlist_items = Wishlist.objects.filter(user_profile=profile)

    template = "profiles/profile.html"
    context = {
        "form": form,
        "orders": orders,
        "wishlist_items": wishlist_items,
        "on_profile_page": True,
        "meta_description": "View and update your profile, see your order history and wishlist items.",
    }

    return render(request, template, context)


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(
        request,
        (
            f"This is a past confirmation for order number {order_number}. "
            "A confirmation email was sent on the order date."
        ),
    )

    template = "checkout/checkout_success.html"
    context = {
        "order": order,
        "from_profile": True,
        "meta_description": f"Order details for order number {order_number}.",
    }

    return render(request, template, context)
