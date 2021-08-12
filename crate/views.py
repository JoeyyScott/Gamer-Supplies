# Imports
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404)
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from supplies.models import Supply
from .models import Coupon
from .forms import FormCoupon


@login_required
def view_crate(request):
    # Crate contents page view
    return render(request, 'crate/crate.html')


@login_required
def add_to_crate(request, item_id):
    # Add a specific supply and quantity to the crate

    supply = get_object_or_404(Supply, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    # Credit for adapted redirect url - see README.md for details
    redirect_url = request.META.get('HTTP_REFERER')
    crate = request.session.get('crate', {})

    # Checking if item exists in crate and displaying the appropriate message
    if item_id in list(crate.keys()):
        crate[item_id] += quantity
        messages.success(request, f'Updated quantity of {supply.name} to \
            {crate[item_id]}.')
    else:
        crate[item_id] = quantity
        messages.success(request, f'Added {supply.name} to your crate.')

    request.session['crate'] = crate
    request.session['manage_crate'] = True
    return redirect(redirect_url)


@login_required
def modify_crate(request, item_id):
    # View to adjust the quantity of a specific supply

    supply = get_object_or_404(Supply, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    crate = request.session.get('crate', {})

    # If specific supply exists in crate and displaying approrpiate message
    if quantity > 0:
        crate[item_id] = quantity
        messages.success(request, f'Updated quantity of {supply.name} to \
            {crate[item_id]}.')
    else:
        crate.pop(item_id)
        messages.success(request, f'Removed {supply.name} from your crate.')

    request.session['crate'] = crate
    request.session['manage_crate'] = True
    return redirect(reverse('view_crate'))


@login_required
def remove_from_crate(request, item_id):
    # View to remove a specific supplie

    try:
        supply = get_object_or_404(Supply, pk=item_id)
        crate = request.session.get('crate', {})

        # Checks to see if the item is in the crate
        if item_id in crate:
            crate.pop(item_id)
            messages.success(request, f'Removed {supply.name} from your crate')

        request.session['crate'] = crate
        return HttpResponse(status=200)

    # Handle errors
    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)


@login_required
@require_http_methods(["GET", "POST"])
def coupon_apply(request):
    # View to check code entered against codes in the coupon model
    code = request.POST.get('coupon-code')

    # Checking for blank coupon submissions
    if not code:
        messages.error(request, "You didn't enter a coupon code!")
        return redirect(reverse('view_crate'))

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


@login_required
def coupons_manage(request):
    # View to allow admins to see the manage coupons page
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins have permission to manage\
            coupons.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        coupon_form = FormCoupon(request.POST)

        # Check if the coupon form is valid and display appropriate message
        if coupon_form.is_valid():
            form_data = coupon_form.save(commit=False)
            form_data.code = form_data.code.upper()
            form_data.save()
            messages.success(request, 'Coupon added successfully!')
            return redirect('coupons_manage')
        else:
            messages.error(request, 'Unable to add coupon, please check your \
                form information is correct.')
            return redirect('coupons_manage')
    else:
        coupon_form = FormCoupon()

    coupon_form = FormCoupon()
    coupons = Coupon.objects.all()
    context = {
        'coupons': coupons,
        'coupon_form': coupon_form,
    }

    return render(request, 'crate/coupons_manage.html', context)
