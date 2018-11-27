from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LogInForm(AuthenticationForm):
    """
    Default login form, uses username and password for standard authentication in django.contrib.auth
    """
    first_name = forms.CharField(
        max_length=254,
        label="First Name",
        widget=forms.TextInput(attrs={'autofocus': True, "class": "form-control"}),
        required=False
    )
    last_name = forms.CharField(
        max_length=254,
        label="Last Name",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=False
    )
    username = forms.CharField(
        max_length=254,
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    password = forms.CharField(
        label="Password",
        strip=False,
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
