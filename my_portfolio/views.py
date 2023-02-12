from django.shortcuts import render
from django.views import View
from .models import All

# Create your views here.

def index(request):
    all = All.objects.all()
    context = {
        'alls': all
    }
    return render(request, 'index.html', context)
