from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Create your views here.
def home(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'home.html', context)

def login(request):
    form = AuthenticationForm()
    context = {
        'hidden': "",
        'form': form,
    }
    return render(request, 'home.html', context)

def signup(request):
    form = UserCreationForm()
    context = {
        'hidden': "",
        'form': form,
    }
    return render(request, 'home.html', context)