from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# from .tokens import account_activation_token
from .models import * 
from .forms import *

# Create your views here.
def home(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'hidden': "hidden"
    }
    return render(request, 'about.html', context)    

def login_page(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            profile = Profile.objects.get(user=user)
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
        print('form is valid? ' + str(form.is_valid()))    
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
    print('signup block')
    if request.method == 'POST':
        print('in POST block')
        # form = UserCreationForm(request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            print('Form is valid')
            print(form.cleaned_data.get('email'))
            user = form.save(commit=False)
            user.email = form.cleaned_data.get('email')
            user.save()
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
            # setting up auto emailing
            current_site = get_current_site(request)
            mail_subject = 'Welcome to Wayfayer'
            message = render_to_string('welcome_email.html', {
                'user': user,
                'domain': current_site.domain,
                # 'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                # 'token':account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                        mail_subject, message, to=[to_email]
            )
            email.send()
            # end auto emailing setup section
            return render(request, 'profile.html', context)
        print('Form is NOT valid')
        print(form.errors)
        return redirect('signup')
    else:
        print('signup else BLOCK')
        # form = UserCreationForm()
        form = SignUpForm()
        context = {
            'hidden': "",
            'form': form,
            'formType': 'signup'
        }
        return render(request, 'home.html', context)

@login_required
def profile(request):
    cities = City.objects.all()
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=request.user.id).select_related('city')
    profile = Profile.objects.get(user=request.user)
    chosen_city = profile.city
    context = {
        'cities': cities,
        'chosen_city': chosen_city,
        'user': user,
        'posts': posts,
        'profile': profile,
        'hidden': "hidden"
    }
    return render(request, 'profile.html', context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    cities = City.objects.all()
    posts = Post.objects.filter(user=request.user.id)
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, request.FILES, instance=profile)
        if profile_form.is_valid():
            profile_form.save()
            context = {
                'cities': cities,
                'user': request.user,
                'posts': posts,
                'profile': profile,
                'hidden': "hidden",
                'showform': "hidden",
            }
            return render(request, 'profile.html', context)
        else:
            return HttpResponse('Form not valid')
    else:
        profile_form = ProfileForm(instance=profile)
        context = {
            'cities': cities,
            'user': request.user,
            'posts': posts,
            'profile': profile,
            'profile_form': profile_form,
            'hidden': "",
            'showform': "",
        }
        return render(request, 'profile.html', context)

@login_required
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
        'hidden': "",
        'showform': "",
        'formType': "post"
    }
    return render(request, 'profile.html', context)

@login_required
def profile_editpost(request, post_id):
    post = Post.objects.get(id=post_id)
    cities = City.objects.all()
    user = User.objects.get(id=request.user.id)
    posts = Post.objects.filter(user=request.user.id)
    city = City.objects.get(id=post.city.id)
    profile = Profile.objects.get(user=request.user)
    context = {
        'cities': cities,
        'city': city,
        'user': user,
        'posts': posts,
        'post': post,
        'profile': profile,
    }
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            context['hidden'] = "hidden"
            context['showform'] = "hidden"
    else:
        form = PostForm(instance=post)
        context['post_form'] = form
        context['hidden'] = ""
        context['showform'] = ""
        context['formType'] = 'editpost'
    return render(request, 'profile.html', context)

def show_city(request, city_id):
    cities = City.objects.all().order_by('name')
    chosen_city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id).select_related('user__profile').order_by('-post_date')
    context = {
        'cities': cities,
        'chosen_city': chosen_city,
        'posts': posts,
        'user': request.user,
        'hidden': "hidden"
    }
    return render(request, 'show_city.html', context)


def city_post(request, city_id, post_id):
    cities = City.objects.all().order_by('name')
    post = Post.objects.get(id=post_id)
    user = User.objects.get(id=post.user.id)
    posts = Post.objects.filter(city=city_id).select_related('user__profile').order_by('-post_date')
    chosen_city = City.objects.get(id=city_id)
    post_city = City.objects.get(id=post.city.id)

    context = {
        'cities': cities,
        'chosen_city': chosen_city,
        'user': user,
        'posts': posts,
        'post': post,
        'post_city': post_city,
        # 'profile': profile,
        'hidden': "",
        'showform': "",
        'formType': "post"
    }
    return render(request, 'show_city.html', context)

@login_required
def newpost(request, city_id):
    cities = City.objects.all().order_by('name')
    chosen_city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id).select_related('user__profile').order_by('-post_date').order_by('title')
    context = {
            'cities': cities,
            'chosen_city': chosen_city,
            'posts': posts,
    }
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            # post.city = chosen_city
            post.save()
            context['hidden'] = "hidden"
            # return redirect('show_city.html', context)
    else:
        post_form = PostForm({'city': chosen_city})
        context['post_form'] = post_form
        context['hidden'] = ""
        context['formType'] = 'newpost'
    return render(request, 'show_city.html', context)

@login_required
def editpost(request, city_id, post_id):
    cities = City.objects.all().order_by('name')
    chosen_city = City.objects.get(id=city_id)
    posts = Post.objects.filter(city=city_id).select_related('user__profile').order_by('-post_date').order_by('title')
    post = Post.objects.get(id=post_id)
    context = {
            'cities': cities,
            'chosen_city': chosen_city,
            'posts': posts,
    }
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            context['hidden'] = "hidden"
            context['showform'] = "hidden"
    else:
        form = PostForm(instance=post)
        context['post'] = post
        context['post_form'] = form
        context['hidden'] = ""
        context['showform'] = ""
        context['formType'] = 'editpost'
    print('********** editpost')
    return render(request, 'show_city.html', context)

@login_required
def deletepost(request, city_id, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('show_city', city_id=city_id)

@login_required
def profile_deletepost(request, post_id):
    post = Post.objects.get(id=post_id)
    post.delete()
    return redirect('profile')