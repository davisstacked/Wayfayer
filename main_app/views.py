from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import * 

# Create your views here.
def home(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'home.html', context)

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return render(request, 'profile.html')
        return redirect('login_page')

    else:
        print('Else block')
        form = AuthenticationForm()
        context = {
            'hidden': "",
            'form': form,
            'formType': 'login'
        }
        return render(request, 'home.html', context)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return render(request, 'profile.html')
        return redirect('signup')
    else:
        form = UserCreationForm()
        context = {
            'hidden': "",
            'form': form,
            'formType': 'signup'
        }
        return render(request, 'home.html', context)

def profile(request):
    print(request.user.id)
    cities = City.objects.all()
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    profile = Profile.objects.get(user=request.user.id)
    context = {
        'cities': cities,
        'user': user,
        'posts': posts,
        'profile': profile
    }
    return render(request, 'profile.html', context)

