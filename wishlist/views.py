from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Wishlist
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(
        user_profile=request.user.profile, product=product
    )

    if created:
        messages.success(request, "Product added to your wishlist!")
    else:
        messages.error(request, "Product is already in your wishlist.")

    return redirect("view_wishlist")


@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user_profile=request.user.profile)
    context = {
        "wishlist_items": wishlist_items,
        "meta_description": "View your wishlist items and manage your favorites.",
    }
    return render(
        request,
        "wishlist/wishlist.html",
        context,
    )


@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(
        user_profile=request.user.profile, product=product
    ).delete()
    messages.success(request, "Product removed from your wishlist.")
    return redirect("view_wishlist")
