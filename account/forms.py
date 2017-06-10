from django import forms

from account.models import UserProfile
from django.contrib.auth.models import User


class RegistrationForm(forms.ModelForm):

    username = forms.CharField(label="Username", max_length=30)
    email = forms.EmailField(label="E-Mail", max_length=30)
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
        label="Password (again)")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        if ('password1' in self.cleaned_data and 
            'password2' in self.cleaned_data):
            if (self.cleaned_data['password1'] != 
                self.cleaned_data['password2']):
                raise forms.ValidationError("Passwords don't match. \
                    Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.is_active = False
            user.save()
        return user


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('verified', 'user', )