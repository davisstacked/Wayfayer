from django import forms
from .models import Profile

#Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'city']

class ImageForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']