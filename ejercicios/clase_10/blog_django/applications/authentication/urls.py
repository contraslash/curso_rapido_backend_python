from django.urls import path
from django.contrib.auth import views as auth_views

from . import (
    conf,
    forms,
    views
)

urlpatterns = [
    path(
        'log-in/',
        views.Login.as_view(
            template_name="log_in.html",
            form_class=forms.LogInForm
        ),
        name=conf.LOGIN_URL_NAME
    ),

    path(
        'log-out/',
        auth_views.LogoutView.as_view(
            next_page="/"
        ),
        name=conf.LOGOUT_URL_NAME
    ),

]
