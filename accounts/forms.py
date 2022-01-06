from django import forms
from django.contrib.auth.models import User
from .models import Profile
# from django.forms import fields

# HARD CODING login form
# class LoginForm(forms.Form):
#     """A form to authenticate users"""

#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,label='Password')

    password2 = forms.CharField(label='Repeat password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name','last_name','email','username')

    def clean_password2(self):
        """Check exactness of passwords"""
        data = self.cleaned_data

        if data['password'] != data['password2']:
            raise forms.ValidationError("Passwords didn't match")

        return data['password2']
       
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth','photo')