from django.shortcuts import render, redirect, get_object_or_404
from django.shortcuts import reverse
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .contexts import bag_contents
from .contexts import generate_custom_id
from products.models import Product
import os


def view_bag(request):
    """ A view that renders the bag contents page
    with items and pricing details """
    context = bag_contents(request)
    return render(request, 'bag/bag.html', context)


@require_POST
def add_to_bag(request, item_id):
    # Check if product exists, throw 404 if not
    get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 1))
    redirect_url = request.POST.get('redirect_url', '/products/')
    bag = request.session.get('bag', {})

    for i in range(quantity):
        customization = {
            'first_name': request.POST.get(f'first_name_{i}', '').strip(),
            'last_name': request.POST.get(f'last_name_{i}', '').strip(),
            'voucher_type': request.POST.get(f'voucher_type_{i}', '').strip()
        }

        if not all(customization.values()):
            messages.error(request, "Please fill in all customization fields.")
            return redirect(redirect_url)

        unique_product_id = generate_custom_id(item_id, customization)
        bag_key = f"{item_id}_{unique_product_id}"

        if bag_key not in bag:
            bag[bag_key] = {
                'quantity': 1,
                'customization': customization
            }
        else:
            bag[bag_key]['quantity'] += 1

    request.session['bag'] = bag
    messages.success(request, "Product successfully added to your bag.")
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity', 0))
    bag = request.session.get('bag', {})

    if quantity > 0:
        if item_id in bag:
            bag[item_id]['quantity'] = quantity
            messages.success(
                request,
                message=(
                    "Updated " + product.name + "'s quantity " +
                    "to " + str(bag[item_id]['quantity']) + "."
                )
            )
        else:
            messages.error(request, "The product isn't in your bag.")
    else:
        bag.pop(item_id, None)
        messages.success(request, f"Removed {product.name} from your bag.")

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


@require_POST
def remove_from_bag(request, key):
    bag = request.session.get('bag', {})

    if key in bag:
        del bag[key]
        request.session['bag'] = bag
        messages.success(request, "Item removed successfully.")

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'status': 'success', 'message': 'Item removed successfully.'},
                status=200
            )
        else:
            return redirect(reverse('view_bag'))
    else:
        messages.error(request, "Item not found in your bag.")

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse(
                {'status': 'error', 'message': 'Item not found in your bag.'},
                status=404
            )
        else:
            return redirect(reverse('view_bag'))


@require_POST
def save_customization(request):
    item_id = request.POST.get('item_id')
    first_name = request.POST.get('first_name', '').strip()
    last_name = request.POST.get('last_name', '').strip()
    voucher_type = request.POST.get('voucher_type', '').strip()

    if not all([item_id, first_name, last_name, voucher_type]):
        return JsonResponse(
            {'status': 'failed', 'error': 'Incomplete data provided.'}
        )

    request.session[f'customization_{item_id}'] = {
        'first_name': first_name,
        'last_name': last_name,
        'voucher_type': voucher_type
    }
    request.session.modified = True
    return JsonResponse({'status': 'success'})
