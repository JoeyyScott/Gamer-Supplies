from django.shortcuts import get_object_or_404
from decimal import Decimal

from supplies.models import Supply
from .models import Coupon


def crate_contents(request):
    coupon_id = request.session.get('coupon_id', int())
    crate_items = []
    total = 0
    total_with_coupon = 0
    coupon_discount = 0
    supply_count = 0
    crate = request.session.get('crate', {})

    try:
        coupon = Coupon.objects.get(id=coupon_id)

    except Coupon.DoesNotExist:
        coupon = None

    for item_id, quantity in crate.items():
        supply = get_object_or_404(Supply, pk=item_id)
        total += quantity * supply.price

        if coupon != None:
            coupon_discount = (coupon.amount/Decimal('100'))*total
            total_with_coupon = total - coupon_discount
        else:
            total_with_coupon = total
        supply_count += quantity
        crate_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'supply': supply
        })

    coupon_amount = coupon.amount

    context = {
        'crate_items': crate_items,
        'total': total,
        'total_with_coupon': total_with_coupon,
        'coupon_amount': coupon_amount,
        'coupon': coupon,
        'supply_count': supply_count,
    }

    return context
