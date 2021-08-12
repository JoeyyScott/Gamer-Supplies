# Imports
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Review
from .forms import FormReview


def index(request):
    # View to load the index page and reviews
    reviews = Review.objects.all()
    context = {'reviews': reviews, }

    return render(request, 'home/index.html', context)


@login_required
def review_add(request):
    # View to add review to the site
    if request.method == 'POST':
        review_form = FormReview(request.POST)

        # Check if the review form is valid and display appropriate message
        if review_form.is_valid():
            form_data = review_form.save(commit=False)
            form_data.added_by = request.user
            form_data.save()
            messages.success(request, 'Review posted successfully!')
            return redirect('home')
        else:
            messages.error(request, 'Unable to add review, please check your \
                form information is correct.')
            return redirect('review_add')
    else:
        review_form = FormReview()

    template = 'home/review_add.html'
    context = {'review_form': review_form, }
    return render(request, template, context)


@login_required
def reviews_manage(request):
    # View to allow admins to see the manage reviews page
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins have permission to manage\
            reviews.')
        return redirect(reverse('home'))

    reviews = Review.objects.all()
    context = {'reviews': reviews, }

    return render(request, 'home/reviews_manage.html', context)


@login_required
def review_delete(request, review_id):
    # View to allow reviews to be deleted by their owners and admins
    redirect_url = request.META.get('HTTP_REFERER')
    review = get_object_or_404(Review, pk=review_id)
    # Check if the user is not the user who added the review
    if not request.user == review.added_by:
        # If they are an admin, delete the review else fallback to below code
        if request.user.is_superuser:
            review.delete()
            messages.success(request, 'Review deleted successfully!')
            return redirect(redirect_url)

        # Security incase a user is not an admin and manages to call this function
        messages.error(request, 'Only the review posters have \
            permission to delete reviews.')
        return redirect(reverse('home'))

    review.delete()
    messages.success(request, 'Review deleted successfully!')
    return redirect(redirect_url)
