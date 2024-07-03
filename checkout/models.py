import uuid
from django.db import models
from products.models import Product
from django_countries.fields import CountryField
from profiles.models import UserProfile

# Define Mystery Box Tiers and their price thresholds
MYSTERY_BOX_TIERS = {"Tier 1": 50, "Tier 2": 100, "Tier 3": 250, "Tier 4": 500}


class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="orders",
    )
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label="Country *", null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    grand_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0
    )
    mystery_box_tier = models.CharField(max_length=50, null=True, blank=True)
    billing_street_address1 = models.CharField(
        max_length=80, null=True, blank=True
    )
    billing_street_address2 = models.CharField(
        max_length=80, null=True, blank=True
    )
    billing_town_or_city = models.CharField(
        max_length=40, null=True, blank=True
    )
    billing_county = models.CharField(max_length=80, null=True, blank=True)
    billing_postcode = models.CharField(max_length=20, null=True, blank=True)
    billing_country = CountryField(
        blank_label="(select country)", null=True, blank=True
    )

    def _generate_order_number(self):
        """Generate a random, unique order number using UUID."""
        return uuid.uuid4().hex.upper()

    def _calculate_mystery_box_tier(self):
        """Calculate the mystery box tier based on the order total."""
        for tier, threshold in MYSTERY_BOX_TIERS.items():
            if self.grand_total >= threshold:
                return tier
        return None

    def save(self, *args, **kwargs):
        if not self.order_number:
            self.order_number = self._generate_order_number()

        # Recalculate mystery box tier only if the grand_total has changed
        if (
            self.pk
            and self.grand_total != Order.objects.get(pk=self.pk).grand_total
        ):
            self.mystery_box_tier = self._calculate_mystery_box_tier()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

    def update_total(self):
        """Update the total value of the order based on its line items."""
        total = sum(item.lineitem_total for item in self.lineitems.all())
        self.order_total = total
        self.grand_total = total
        self.save()


class OrderLineItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name="lineitems"
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, editable=False
    )
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    voucher_type = models.CharField(max_length=100, blank=True)

    def save(self, *args, **kwargs):
        """Set the lineitem total and update the order total."""
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)
        self.order.update_total()

    def __str__(self):
        return (
            f"{self.product.name} x {self.quantity} "
            f"on order {self.order.order_number}"
        )
