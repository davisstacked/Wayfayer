from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import * 
from .forms import ProfileForm, PostForm

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

@login_required
def profile(request):
    # if request.method == "POST":
    #     profile = Profile.objects.get(user=request.user)
    #     form = ImageForm(request.POST, request.FILES, instance=profile)
    #     if form.is_valid():
    #         print(request.FILES)
    #         form.save()
    #         return redirect('profile')
    # else:
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
        # 'formType': post
    }
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
            # post.city = chosen_city
            post.save()
            context['hidden'] = "hidden"
            context['showform'] = "hidden"
    else:
        post_form = PostForm(instance=post)
        context['post'] = post
        context['post_form'] = post_form
        context['hidden'] = ""
        context['showform'] = ""
        context['formType'] = 'editpost'
    return render(request, 'show_city.html', context)

@login_required
def deletepost(request, city_id, post_id):
    post = Post.objects.get(id=post_id)
    # print(post.city_name)
    print("in deletepost block")
    post.delete()
    return redirect('show_city', city_id=city_id)