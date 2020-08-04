from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login

# Create your views here.
def home(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'home.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
    else:
        form = AuthenticationForm()
        context = {
            'hidden': "",
            'form': form,
            'formType': 'login'
        }
        return render(request, 'home.html', context)

def signup(request):
    
    form = UserCreationForm()
    context = {
        'hidden': "",
        'form': form,
        'formType': 'signup'
    }
    return render(request, 'home.html', context)

def profile(request):
    return HttpResponse('Profile page')
