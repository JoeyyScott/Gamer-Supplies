from django.shortcuts import get_object_or_404
from decimal import Decimal

from supplies.models import Supply
from .models import Coupon


def crate_contents(request):
    coupon_id = request.session.get('coupon_id', int())
    crate_items = []
    crate_total = 0
    total = 0
    savings = 0
    coupon_amount = 0
    supply_count = 0
    crate = request.session.get('crate', {})

    try:
        coupon = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        coupon = None

    for item_id, quantity in crate.items():
        supply = get_object_or_404(Supply, pk=item_id)
        crate_total += quantity * supply.price

        if coupon != None:
            coupon_amount = coupon.amount
            savings = crate_total*(coupon_amount/Decimal('100'))
            total = crate_total - savings
        else:
            total = crate_total

        supply_count += quantity
        crate_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'supply': supply
        })

    context = {
        'crate_items': crate_items,
        'supply_count': supply_count,
        'total': total,
        'coupon': coupon,
        'coupon_amount': coupon_amount,
        'savings': savings,
    }

    return context
