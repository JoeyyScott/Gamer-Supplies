from django.shortcuts import render

# Create your views here.


def view_crate(request):
    """ Crate page view """

    return render(request, 'crate/crate.html')