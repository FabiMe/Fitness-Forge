from decimal import Decimal
from django.conf import settings

def get_mystery_box_tier(total):
    if total >= settings.TIER_4_THRESHOLD:
        return "Tier 4"
    elif total >= settings.TIER_3_THRESHOLD:
        return "Tier 3"
    elif total >= settings.TIER_2_THRESHOLD:
        return "Tier 2"
    elif total >= settings.TIER_1_THRESHOLD:
        return "Tier 1"
    else:
        return "None"

def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0

    # Calculate total and product count from bag items
    for item in bag_items:
        total += item.price * item.quantity
        product_count += item.quantity

    # Calculate the tier of the mystery box
    mystery_box_tier = get_mystery_box_tier(total)

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'mystery_box_tier': mystery_box_tier,
    }

    return context