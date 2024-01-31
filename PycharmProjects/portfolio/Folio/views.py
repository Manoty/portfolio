from django.shortcuts import render


def index(request):
    return render(request, 'Folio/index.html')

# Create your views here.
