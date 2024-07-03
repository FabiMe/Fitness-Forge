from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = (
            "full_name",
            "email",
            "phone_number",
            "street_address1",
            "street_address2",
            "town_or_city",
            "county",
            "postcode",
            "country",
            "billing_street_address1",
            "billing_street_address2",
            "billing_town_or_city",
            "billing_county",
            "billing_postcode",
            "billing_country",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "full_name": "Full Name",
            "email": "Email Address",
            "phone_number": "Phone Number",
            "postcode": "Postal Code",
            "town_or_city": "Town or City",
            "street_address1": "Street Address 1",
            "street_address2": "Street Address 2",
            "county": "County, State or Locality",
            "billing_street_address1": "Billing Street Address 1",
            "billing_street_address2": "Billing Street Address 2",
            "billing_town_or_city": "Billing Town or City",
            "billing_county": "Billing County, State or Locality",
            "billing_postcode": "Billing Postal Code",
            "billing_country": "Billing Country",
        }

        for field in self.fields:
            if field in placeholders:
                placeholder = placeholders[field] + (
                    " *" if self.fields[field].required else ""
                )
                self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].widget.attrs["class"] = "stripe-style-input"
            self.fields[field].label = False
