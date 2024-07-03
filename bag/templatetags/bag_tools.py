from django import template


register = template.Library()


@register.filter(name="calc_subtotal")
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter
def get_customization(session, item_id):
    default = {"voucher_type": "N/A", "first_name": "N/A", "last_name": "N/A"}
    return session.get(f"customization_{item_id}", default)


@register.filter(name="multiply")
def multiply(value, arg):
    """Multiplies the value by the arg."""
    try:
        return value * arg
    except (ValueError, TypeError):
        try:
            return int(value) * int(arg)
        except (ValueError, TypeError):
            return ""


@register.filter(name="friendly_name")
def friendly_name(value):
    """
    Replaces underscores with spaces and capitalizes the first letter of
    each word.
    """
    return " ".join(
        word.capitalize() for word in value.replace("_", " ").split()
    )
