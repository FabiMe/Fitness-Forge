from decimal import Decimal
from django.shortcuts import get_object_or_404, Http404
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

    for item_key, item_data in bag.items():
        product_id = item_key.split('_')[0]  # Assuming item_key is like 'productid_index'
        product = get_object_or_404(Product, pk=product_id)
        quantity = item_data['quantity']
        subtotal = Decimal(item_data['quantity']) * product.price
        total += subtotal
        product_count += quantity

        customization = item_data.get('customization', {'first_name': 'N/A', 'last_name': 'N/A', 'voucher_type': 'N/A'})

        bag_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
            'customization': customization
        })

    mystery_box_tier = get_mystery_box_tier(total)  # Call to determine the mystery box tier

    return {
        'bag_items': bag_items,
        'total': total,
        'grand_total': total,  # Modify as necessary for additional fees or discounts
        'product_count': product_count,
        'mystery_box_tier': mystery_box_tier
    }

    return context
