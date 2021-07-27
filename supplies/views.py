from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Supply, Category
from django.db.models.functions import Lower

# Create your views here.


def all_supplies(request):
    """ A view to show all supplies, including sorting and search queries """

    supplies = Supply.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                supplies = supplies.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            supplies = supplies.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            supplies = supplies.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter a search term!")
                return redirect(reverse('supplies'))

            queries = Q(name__icontains=query) | Q(description__icontains=query) | Q(brand__icontains=query)
            supplies = supplies.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'supplies': supplies,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting.replace('_', ' '),
    }

    return render(request, 'supplies/supplies.html', context)
