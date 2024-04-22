import uuid
from django.db import models
from django.db.models import Sum
from django.conf import settings
from products.models import Product

# Define Mystery Box Tiers and their price thresholds
MYSTERY_BOX_TIERS = {
    'Tier 1': 50,
    'Tier 2': 100,
    'Tier 3': 250,
    'Tier 4': 500
}

class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = models.CharField(max_length=40, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    mystery_box_tier = models.CharField(max_length=50, null=True, blank=True)

    def _generate_order_number(self):
        """
        Generate a random, unique order number using UUID
        """
        return uuid.uuid4().hex.upper()

    def _calculate_mystery_box_tier(self):
        """
        Calculate the mystery box tier based on the order total
        """
        for tier, threshold in MYSTERY_BOX_TIERS.items():
            if self.grand_total >= threshold:
                return tier
        return None

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already, and calculate the mystery box tier.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # Calculate the mystery box tier based on the order total
        self.mystery_box_tier = self._calculate_mystery_box_tier()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    def update_total(self):
        """
        Update the total value of the order
        """
        # Calculate the total value of the order based on its line items
        total = sum(item.lineitem_total for item in self.lineitems.all())
        self.order_total = total
        self.grand_total = total
        self.save()


class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, editable=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    voucher_type = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total on the parent order instance.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return f'{self.product.name} x {self.quantity} on order {self.order.order_number}'