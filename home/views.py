from django.shortcuts import render

# Create your views here.


def index(request):
    """ Index page view """

    return render(request, 'home/index.html')


def review_add(request):
    """ Added review page view """

    return render(request, 'home/review_add.html')