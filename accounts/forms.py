from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from .models import Profile
from educational_need.models import EducationalNeed
        
class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
        
    class Meta:
        model = Profile
        fields = ('birth_date', 'mobile_number', 'phone_number',
                  'country', 'state', 'zip_code', 'city', 'district', 'about')
        widgets = {
            'birth_date': forms.DateTimeInput(attrs={'class': 'datetime-input'})
        }

class PasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password',)
