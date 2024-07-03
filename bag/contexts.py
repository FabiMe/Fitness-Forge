from decimal import Decimal
from django.shortcuts import get_object_or_404
from products.models import Product
import hashlib
import json

# Define mystery box tiers
MYSTERY_BOX_TIERS = {
    "Tier 1": {"threshold": 50, "sku": "MB001"},
    "Tier 2": {"threshold": 150, "sku": "MB002"},
    "Tier 3": {"threshold": 250, "sku": "MB003"},
    "Tier 4": {"threshold": 500, "sku": "MB004"},
}


def get_mystery_box_tier(total):
    for tier, details in sorted(
        MYSTERY_BOX_TIERS.items(), key=lambda x: x[1]["threshold"], reverse=True
    ):
        if total >= details["threshold"]:
            return details


def generate_custom_id(item_id, customization):
    # Create a consistent JSON string from the customization dictionary
    customization_str = json.dumps(customization, sort_keys=True)
    # Generate a hash of this string
    return hashlib.md5((str(item_id) + customization_str).encode()).hexdigest()


def bag_contents(request):
    bag_items = []
    total = Decimal("0.00")
    product_count = 0
    bag = request.session.get("bag", {})

    for bag_key, item_data in bag.items():
        actual_product_id, custom_key = bag_key.split("_")
        product = get_object_or_404(Product, pk=int(actual_product_id))
        quantity = item_data["quantity"]
        subtotal = quantity * product.price
        total += subtotal
        product_count += quantity

        bag_items.append(
            {
                "product": product,
                "quantity": quantity,
                "subtotal": subtotal,
                "customization": item_data["customization"],
                "customization_key": bag_key,
            }
        )

    mystery_box_details = get_mystery_box_tier(total)
    if mystery_box_details:
        mystery_box = get_object_or_404(Product, sku=mystery_box_details["sku"])
        bag_items.append(
            {
                "product": mystery_box,
                "quantity": 1,
                "subtotal": Decimal("0.00"),
                "customization": {},
            }
        )

    context = {
        "bag_items": bag_items,
        "total": total,
        "grand_total": total,
        "product_count": product_count,
    }

    return context
