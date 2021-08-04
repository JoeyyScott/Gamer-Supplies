from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import FormReview
# Create your views here.


def index(request):
    """ Index page view with reviews """
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/index.html', context)


@login_required
def review_add(request):
    # Add review to site
    if request.method == 'POST':
        review_form = FormReview(request.POST)

        # Check if the review form is valid
        if review_form.is_valid():
            form_data = review_form.save(commit=False)
            form_data.added_by = request.user
            form_data.save()
            messages.success(request, 'Review posted successfully')
            return redirect('home')
        else:
            messages.error(request, 'Failed to post review')
            return redirect('review_add')
    else:
        review_form = FormReview()

    template = 'home/review_add.html'
    context = {
        'review_form': review_form,
    }
    return render(request, template, context)


def reviews_manage(request):
    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/reviews_manage.html', context)
