from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from supplies.models import Supply
from .models import Coupon

# Create your views here.


@login_required
def view_crate(request):
    """ Crate page view """

    return render(request, 'crate/crate.html')


@login_required
def add_to_crate(request, item_id):
    """ Add a quantity of the specified supply to the shopping crate """

    supply = get_object_or_404(Supply, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    crate = request.session.get('crate', {})

    if item_id in list(crate.keys()):
        crate[item_id] += quantity
        messages.success(request, f'Updated quantity of {supply.name} to {crate[item_id]}.')
    else:
        crate[item_id] = quantity
        messages.success(request, f'Added {supply.name} to your crate.')

    request.session['crate'] = crate
    request.session['manage_crate'] = True
    return redirect(redirect_url)


@login_required
def modify_crate(request, item_id):
    """ Add a quantity of the specified supply to the shopping crate """

    supply = get_object_or_404(Supply, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    crate = request.session.get('crate', {})

    if quantity > 0:
        crate[item_id] = quantity
        messages.success(request, f'Updated quantity of {supply.name} to {crate[item_id]}.')
    else:
        crate.pop(item_id)
        messages.success(request, f'Removed {supply.name} from your crate.')

    request.session['crate'] = crate
    request.session['manage_crate'] = True
    return redirect(reverse('view_crate'))


@login_required
def remove_from_crate(request, item_id):
    """Remove the item from the shopping crate"""

    try:
        supply = get_object_or_404(Supply, pk=item_id)
        crate = request.session.get('crate', {})
        request.session['manage_crate'] = True

        if item_id in crate:
            crate.pop(item_id)
            messages.success(request, f'Removed {supply.name} from your crate')

        request.session['crate'] = crate
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    code = request.POST.get('coupon-code')
    try:
        coupon = Coupon.objects.get(code=code)
        request.session['coupon_id'] = coupon.id
        messages.success(request, f'Coupon code: { code } applied')
    except Coupon.DoesNotExist:
        request.session['coupon_id'] = None
        messages.warning(request, f'Coupon code: { code } not accepted')
        return redirect('view_crate')
    else:
        return redirect('view_crate')