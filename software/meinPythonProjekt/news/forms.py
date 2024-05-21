from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, password_validation
from django.contrib.auth import *


class SignupForm(forms.Form):
    email = forms.TextField(max_length=200, help_text='Required')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        user = authenticate(request=self.request, username=username, password=password)
        if user is None:
            raise forms.ValidationError('Ungültiger Benutzername oder Passwort')
            return self.cleaned_data

class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='E-Mail-Adresse')

    def clean_email(self):
        email = self.cleaned_data['email']
        user = auth.get_user_by_email(email)
        if user is not None:
            #send a reset password mail
            send_reset_password_mail(request=self.request, email=email)
            return email
        else:
            raise forms.ValidationError('Diese E-Mail-Adresse ist nicht unserem System registriert, bitte erstellen sie zuerst ein Konto bei uns')