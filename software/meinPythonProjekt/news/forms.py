from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, get_user_model, password_validation


class SignupForm(forms.Form):
    email = forms.CharField(max_length=200, help_text='Required')

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