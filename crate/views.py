from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from supplies.models import Supply

# Create your views here.


def view_crate(request):
    """ Crate page view """

    return render(request, 'crate/crate.html')


def add_to_crate(request, item_id):
    """ Add a quantity of the specified supply to the shopping crate """

    supply = get_object_or_404(Supply, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    crate = request.session.get('crate', {})

    if item_id in list(crate.keys()):
        crate[item_id] += quantity
        messages.success(request, f'Updated quantity of {supply.name} to {crate[item_id]}')
    else:
        crate[item_id] = quantity
        messages.success(request, f'You\'ve added {supply.name} to your crate!')

    request.session['crate'] = crate
    return redirect(redirect_url)


def modify_crate(request, item_id):
    """ Add a quantity of the specified supply to the shopping crate """

    quantity = int(request.POST.get('quantity'))
    crate = request.session.get('crate', {})

    if quantity > 0:
        crate[item_id] = quantity
    else:
        crate.pop(item_id)

    request.session['crate'] = crate
    return redirect(reverse('view_crate'))


def remove_from_crate(request, item_id):
    """Remove the item from the shopping crate"""

    try:
        supply = get_object_or_404(Supply, pk=item_id)
        crate = request.session.get('crate', {})

        if item_id in crate:
            crate.pop(item_id)
            messages.success(request, f'Removed {supply.name} from your crate')

        request.session['crate'] = crate
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
