from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .models import * 
from .forms import ProfileForm

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
            city = City.objects.all().first()
            profile = Profile(user=user, city=city, display_name=user.username)
            profile.save()
            login(request, user)
            cities = City.objects.all()
            posts = Post.objects.filter(user=request.user.id)
            context = {
                'cities': cities,
                'user': user,
                'posts': posts,
                'profile': profile,
                'hidden': "hidden"
            }
            return render(request, 'profile.html', context)
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
    cities = City.objects.all()
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'cities': cities,
        'user': user,
        'posts': posts,
        'profile': profile,
        'hidden': "hidden"
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    user = User.objects.filter(id=request.user.id)
    profile = Profile.objects.get(user=request.user)
    cities = City.objects.all()
    posts = Post.objects.filter(user=request.user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            context = {
                'cities': cities,
                'user': user,
                'posts': posts,
                'profile': profile,
                'hidden': "hidden"
            }
            return render(request, 'profile.html', context)
        else:
            return HttpResponse('Form not valid')
    else:
        profile_form = ProfileForm(instance=profile)
        context = {
            'cities': cities,
            'user': user,
            'posts': posts,
            'profile': profile,
            'profile_form': profile_form,
            'hidden': ""
        }
        return render(request, 'profile.html', context)

def profile_post(request, post_id):
    cities = City.objects.all()
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    post = Post.objects.get(id=post_id)
    city = City.objects.get(id=post.city.id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'cities': cities,
        'city': city,
        'user': user,
        'posts': posts,
        'post': post,
        'profile': profile,
        'hidden': ""
    }
    return render(request, 'profile.html', context)
