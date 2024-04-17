from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

MYSTERY_BOX_TIERS = {
    'Tier 1': 50,
    'Tier 2': 100,
    'Tier 3': 250,
    'Tier 4': 500
}

def get_mystery_box_tier(total):
    for tier, threshold in MYSTERY_BOX_TIERS.items():
        if total >= threshold:
            return tier
    return None

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    # Determine Mystery Box tier
    mystery_box_tier = get_mystery_box_tier(total)

    # Calculate delivery (not needed for mystery boxes)
    delivery = 0

    # Calculate grand total
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'mystery_box_tier': mystery_box_tier,  # Add Mystery Box tier to context
        'grand_total': grand_total,
    }

    return context