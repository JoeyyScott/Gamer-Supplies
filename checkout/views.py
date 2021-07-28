from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings

from .forms import OrderForm
from crate.contexts import crate_contents

import stripe


def checkout(request):
    stripe_public_key_gs = settings.STRIPE_PUBLIC_KEY_GS
    stripe_secret_key_gs = settings.STRIPE_SECRET_KEY_GS
    crate = request.session.get('crate', {})
    if not crate:
        messages.error(request, "There's nothing in your crate at the moment")
        return redirect(reverse('products'))

    current_crate = crate_contents(request)
    total = current_crate['total']
    total_stripe = round(total * 100)
    stripe.api_key = stripe_secret_key_gs
    intent = stripe.PaymentIntent.create(
        amount=total_stripe,
        currency=settings.STRIPE_CURRENCY,
    )

    order_form = OrderForm()

    if not stripe_public_key_gs:
        messages.warning(request, 'Oh no! Stripe public key missing! \
            Double check that it is set in your environment.')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key_gs,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)
