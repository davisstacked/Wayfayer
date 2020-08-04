from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def home(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'home.html', context)

def login(request):
    context = {
        'hidden': ""
    }
    return render(request, 'home.html', context)

def signup(request):
    context = {
        'hidden': ""
    }
    return render(request, 'home.html', context)