from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile, Post

#Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'image', 'city']


class PostForm(forms.ModelForm):
    class Meta:
        model = Post 
        fields = ['title', 'blurb', 'city']

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=150, help_text='Required')
    class Mata:
        model = User
        fields = ['username', 'email', 'password']