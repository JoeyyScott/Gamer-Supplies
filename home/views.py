from django.shortcuts import render, redirect, reverse, get_object_or_404
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
            messages.success(request, 'Review posted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Unable to add review, please check your form information is correct.')
            return redirect('review_add')
    else:
        review_form = FormReview()

    template = 'home/review_add.html'
    context = {
        'review_form': review_form,
    }
    return render(request, template, context)


def reviews_manage(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins are allowed to manage reviews.')
        return redirect(reverse('home'))

    reviews = Review.objects.all()

    context = {
        'reviews': reviews,
    }

    return render(request, 'home/reviews_manage.html', context)


@login_required
def review_delete(request, review_id):
    if not request.user.is_superuser:
        messages.error(request, 'Only admins have permission to delete reviews.')
        return redirect(reverse('home'))

    review = get_object_or_404(Review, pk=review_id)
    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect(reverse('reviews_manage'))
