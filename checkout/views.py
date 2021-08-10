# Imports
from django.shortcuts import (
    render, redirect, reverse, get_object_or_404, HttpResponse)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.utils.safestring import mark_safe

from .forms import OrderForm
from .models import Order, CrateItems
from supplies.models import Supply
from crate.models import Coupon
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
from crate.contexts import crate_contents

import stripe
import json


@login_required
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY_GS
        stripe.PaymentIntent.modify(pid, metadata={
            'crate': json.dumps(request.session.get('crate', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, there was an error \
            processed your payment. Please try again later.')
        return HttpResponse(content=e, status=400)


@login_required
def checkout(request):
    # Handle requests to the checkout page
    stripe_public_key_gs = settings.STRIPE_PUBLIC_KEY_GS
    stripe_secret_key_gs = settings.STRIPE_SECRET_KEY_GS

    if request.method == 'POST':
        crate = request.session.get('crate', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'contact_number': request.POST['contact_number'],
            'address_line_1': request.POST['address_line_1'],
            'address_line_2': request.POST['address_line_2'],
            'town_or_city': request.POST['town_or_city'],
            'county': request.POST['county'],
            'postcode': request.POST['postcode'],
            'country': request.POST['country'],
        }
        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            coupon = request.session.get('coupon_id')
            if coupon is not None:
                code = Coupon.objects.get(pk=coupon)
                order.coupon = code
                request.session['coupon_id'] = None
            else:
                print('no coupon')
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_crate = json.dumps(crate)
            order.save()
            for item_id, quantity in crate.items():
                try:
                    supply = Supply.objects.get(id=item_id)
                    crate_item = CrateItems(
                        order=order,
                        supply=supply,
                        quantity=quantity,
                    )
                    crate_item.save()
                except Supply.DoesNotExist:
                    messages.error(request, ("One of the supplies in your \
                        crate was not found in our database. Please contact \
                        us."))
                    order.delete()
                    return redirect(reverse('view_crate'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Oh no, error has occured! Please check \
                your information.')
    else:
        crate = request.session.get('crate', {})
        if not crate:
            messages.error(request, "Your crate is empty at the moment.")
            return redirect(reverse('supplies'))

        current_crate = crate_contents(request)
        total = current_crate['total']
        total_stripe = round(total * 100)
        stripe.api_key = stripe_secret_key_gs
        intent = stripe.PaymentIntent.create(
            amount=total_stripe,
            currency=settings.STRIPE_CURRENCY,
        )

        # If the user is logged in, pull details from profile
        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.default_full_name,
                    'email': profile.user.email,
                    'contact_number': profile.default_contact_number,
                    'address_line_1': profile.default_address_line_1,
                    'address_line_2': profile.default_address_line_2,
                    'town_or_city': profile.default_town_or_city,
                    'county': profile.default_county,
                    'postcode': profile.default_postcode,
                    'country': profile.default_country,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

    if not stripe_public_key_gs:
        messages.warning(request, 'Oh no! Stripe public key missing! \
            Double check that it is set in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key_gs': stripe_public_key_gs,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    # Handle successful checkouts
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, mark_safe(f'Checkout successful!<br> We will \
        send a confirmation email to <span class="highlight">{order.email}\
        </span>.<br> Your order number is: <span class="highlight">\
        {order_number}</span>.'))

    if request.user.is_authenticated:
        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's profile to the order
        order.user_profile = profile
        order.save()

        # Save the user's info
        if save_info:
            profile_data = {
                'default_full_name': order.full_name,
                'default_email': order.email,
                'default_contact_number': order.contact_number,
                'default_address_line_1': order.address_line_1,
                'default_address_line_2': order.address_line_2,
                'default_town_or_city': order.town_or_city,
                'default_county': order.county,
                'default_postcode': order.postcode,
                'default_country': order.country,
            }
            user_profile_form = UserProfileForm(profile_data, instance=profile)
            if user_profile_form.is_valid():
                user_profile_form.save()

    if 'crate' in request.session:
        del request.session['crate']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'order_number': order_number,
    }

    return render(request, template, context)
