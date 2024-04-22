from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product

# Define mystery box tiers
MYSTERY_BOX_TIERS = {
    'Tier 1': 50,
    'Tier 2': 150,
    'Tier 3': 250,
    'Tier 4': 500
}

def get_mystery_box_tier(total):
    for tier_name, threshold in sorted(MYSTERY_BOX_TIERS.items(), key=lambda x: x[1], reverse=True):
        if total >= threshold:
            return tier_name
    return "No tier"  # Default if no tier reached

def bag_contents(request):
    bag_items = []
    total = Decimal('0.00')
    product_count = 0
    bag = request.session.get('bag', {})

    for item_id, item_data in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        if isinstance(item_data, dict):
            quantity = item_data.get('quantity', 1)  # Default quantity is 1 if not specified
        else:
            quantity = int(item_data)  # Convert quantity to integer if not a dictionary

        product_total = quantity * product.price
        total += product_total
        product_count += quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'subtotal': product_total
        })

    grand_total = total  # Total cost; adjust if necessary to include other fees
    mystery_box_tier = get_mystery_box_tier(total)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'grand_total': grand_total,
        'mystery_box_tier': mystery_box_tier,
    }

    return context