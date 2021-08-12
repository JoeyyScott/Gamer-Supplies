# Imports
import uuid
from django.db import models
from django.db.models import Sum
from decimal import Decimal
from django_countries.fields import CountryField
from supplies.models import Supply
from profiles.models import UserProfile
from crate.models import Coupon


# Order model from checkout form
class Order(models.Model):
    order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.SET_NULL,
        null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=80, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    address_line_1 = models.CharField(max_length=50, null=False, blank=False)
    address_line_2 = models.CharField(max_length=50, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    county = models.CharField(max_length=50, null=True, blank=True)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    coupon = models.ForeignKey(
        Coupon, on_delete=models.SET_NULL, null=True, blank=True)
    order_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)
    original_crate = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        # Use UUID to generate order number
        return uuid.uuid4().hex.upper()

    def update_total(self):
        # Update total each time a crate item is added
        self.order_total = (
            self.crateitems.aggregate(
                Sum("crateitem_total"))["crateitem_total__sum"] or 0
        )
        # Checking whether a coupon was applied to the order
        if self.coupon is not None:
            savings = self.order_total * (self.coupon.amount / Decimal("100"))
            self.order_total = self.order_total - savings

        self.save()

    def save(self, *args, **kwargs):
        # Set order number by overriding original save method
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


# Crate items model
class CrateItems(models.Model):

    class Meta:
        verbose_name_plural = "Crate Items"

    order = models.ForeignKey(
        Order, null=False, blank=False,
        on_delete=models.CASCADE, related_name="crateitems")
    supply = models.ForeignKey(
        Supply, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    crateitem_total = models.DecimalField(
        max_digits=6, decimal_places=2,
        null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Set the crate total and update the order total
        by overriding the original save method.
        """
        self.crateitem_total = self.supply.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.supply.name} on \
            order {self.order.order_number}'
