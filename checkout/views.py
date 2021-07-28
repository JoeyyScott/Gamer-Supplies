from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    crate = request.session.get('crate', {})
    if not crate:
        messages.error(request, "There's nothing in your crate at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JBmxeE1JD70w0vYGXg0llD59ASHmLAlJMuRa49190Qhjd8b9C0JIsKG4GliLGeiVh4ybgYQ8cmW03eMzHXx448v002mkhcy49',
        'client_secret': 'test client secret'
    }

    return render(request, template, context)