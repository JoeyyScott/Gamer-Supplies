from django.db import models


# Category model
class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name


# Supply model
class Supply(models.Model):

    class Meta:
        verbose_name_plural = 'Supplies'

    name = models.CharField(max_length=254, null=True)
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(null=True, blank=True)
    brand = models.CharField(max_length=254, null=True, blank=True)
    size = models.CharField(max_length=25, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
