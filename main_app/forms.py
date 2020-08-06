from django import forms
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
