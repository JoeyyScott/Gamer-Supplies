from django.shortcuts import render
from .models import Supply

# Create your views here.


def all_supplies(request):
    """ A view to show all products, including sorting and search queries """

    supplies = Supply.objects.all()

    context = {
        'supplies': supplies,
    }

    return render(request, 'supplies/supplies.html', context)
