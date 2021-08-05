from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Supply, Category
from .forms import FormSupply
from django.db.models.functions import Lower

# Create your views here.


def all_supplies(request):
    """ A view to show all supplies, including sorting and search queries """

    supplies = Supply.objects.all()
    query = None
    categories = None
    sort = None
    direction = None
    manage_crate = request.session['manage_crate']
    request.session['manage_crate'] = False

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
        'manage_crate': manage_crate,
    }

    return render(request, 'supplies/supplies.html', context)


@login_required
def supply_add(request):
    """ Add a supply """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins are allowed to add supplies.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = FormSupply(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            request.session['manage_crate'] = False
            messages.success(request, 'Supply added successfully!')
            return redirect(reverse('supplies'))
        else:
            messages.error(request, 'Unable to add supply, please check your form information is correct.')
    else:
        form = FormSupply()

    template = 'supplies/supply_add.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def supply_edit(request, supply_id):
    """ Edit a supply """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins are allowed to add supplies.')
        return redirect(reverse('home'))

    supply = get_object_or_404(Supply, pk=supply_id)
    if request.method == 'POST':
        form = FormSupply(request.POST, request.FILES, instance=supply)
        if form.is_valid():
            form.save()
            
            messages.success(request, f'{supply.name} updated successfully!')
            return redirect('supplies')
        else:
            messages.error(request, 'Unable to update supply, please check your form information is correct.')
    else:
        form = FormSupply(instance=supply)
        messages.info(request, f'You are editing {supply.name}')

    template = 'supplies/supply_edit.html'
    context = {
        'form': form,
        'supply': supply,
    }

    return render(request, template, context)


@login_required
def supply_delete(request, supply_id):
    """ Delete a supply """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only admins are allowed to add supplies.')
        return redirect(reverse('home'))

    supply = get_object_or_404(Supply, pk=supply_id)
    supply.delete()
    messages.success(request, 'Supply deleted successfully!')
    return redirect(reverse('supplies'))