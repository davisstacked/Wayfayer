from django import forms
from .models import Profile
from django.contrib.auth.models import User

#Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'city']

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']