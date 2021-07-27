from django.shortcuts import get_object_or_404
from supplies.models import Supply


def crate_contents(request):

    crate_items = []
    total = 0
    supply_count = 0
    crate = request.session.get('crate', {})

    for item_id, quantity in crate.items():
        supply = get_object_or_404(Supply, pk=item_id)
        total += quantity * supply.price
        supply_count += quantity
        crate_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'supply': supply
        })

    context = {
        'crate_items': crate_items,
        'total': total,
        'supply_count': supply_count,
    }

    return context
