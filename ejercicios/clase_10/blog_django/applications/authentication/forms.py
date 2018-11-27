from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LogInForm(AuthenticationForm):
    """
    Default login form, uses username and password for standard authentication in django.contrib.auth
    """
    username = forms.CharField(
        max_length=254,
        label="Username",
        widget=forms.TextInput(attrs={'autofocus': True, "class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
