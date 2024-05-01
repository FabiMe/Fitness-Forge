from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Wishlist
from django.contrib.auth.decorators import login_required

@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    wishlist, created = Wishlist.objects.get_or_create(user_profile=request.user.profile, product=product)
    
    if created:
        messages.success(request, 'Product added to your wishlist!')
    else:
        messages.error(request, 'Product is already in your wishlist.')

    return redirect('view_wishlist')

@login_required
def view_wishlist(request):
    wishlist_items = Wishlist.objects.filter(user_profile=request.user.profile)
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    Wishlist.objects.filter(user_profile=request.user.profile, product=product).delete()
    return redirect('view_wishlist')