from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Supply

# Create your views here.


def all_supplies(request):
    """ A view to show all products, including sorting and search queries """

    supplies = Supply.objects.all()
    query = None

    if 'q' in request.GET:
        query = request.GET['q']
        if not query:
            messages.error(request, "You didn't enter a search term!")
            return redirect(reverse('supplies'))

        queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
        supplies = supplies.filter(queries)

    context = {
        'supplies': supplies,
        'search_term': query,
    }

    return render(request, 'supplies/supplies.html', context)
