from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, UserChangeForm
from .models import User
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget, PhoneNumberPrefixWidget


class NewUSerForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUSerForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]

        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'USERNAME',
    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'placeholder': 'PASSWORD',
    }))