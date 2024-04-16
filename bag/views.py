from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import messages

from products.models import Product

# Views for managing shopping bag functionality

def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    try:
        product = Product.objects.get(pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in bag:
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

        request.session['bag'] = bag
        return redirect(redirect_url)
    except Product.DoesNotExist:
        messages.error(request, "Product not found")
        return redirect(reverse('view_bag'))
    except ValueError:
        messages.error(request, "Invalid quantity")
        return redirect(reverse('view_bag'))

def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    try:
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity > 0:
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return redirect(reverse('view_bag'))
    except ValueError:
        messages.error(request, "Invalid quantity")
        return redirect(reverse('view_bag'))

def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        bag = request.session.get('bag', {})
        bag.pop(item_id)
        request.session['bag'] = bag
        messages.success(request, "Item removed from your bag")
        return HttpResponse(status=200)
    except KeyError:
        messages.error(request, "Item not found in your bag")
        return HttpResponse(status=404)