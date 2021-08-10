# Imports
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from .models import UserProfile
from .forms import FormUserProfile
from checkout.models import Order


@login_required
def profile(request):
    # View to display a user's profile
    profile = get_object_or_404(UserProfile, user=request.user)

    # Check for form submission and display appropriate message
    if request.method == 'POST':
        form = FormUserProfile(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile successfully updated.')
        else:
            messages.error(request, 'Unable to update your profile, please \
                check that your details are correct.')
    else:
        form = FormUserProfile(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
    }

    return render(request, template, context)


@login_required
def order_history(request, order_number):
    # View to display an order history
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, mark_safe(
        f'This is a past confirmation for order number beginning: \
            <span class="highlight">{ order_number[:16] }.. </span><br> A \
            confirmation email was sent to: <span class="highlight">\
            {order.email}</span><br> Order date: <span class="highlight">\
            {order.date}</span>.'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
