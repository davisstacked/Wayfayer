from django import forms
from .models import Profile

#Profile Form
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['display_name', 'image', 'city']