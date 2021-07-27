def crate_contents(request):

    crate_items = []
    total = 0
    product_count = 0

    context = {
        'crate_items': crate_items,
        'total': total,
        'product_count': product_count,
    }

    return context
