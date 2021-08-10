# Credit for adapted code from Boutique Ado to calculate subtotals of items
from django import template

register = template.Library()


# Subtotal template tag
@register.filter(name='subtotal')
def subtotal(price, quantity):
    return price * quantity
