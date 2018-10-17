from django.urls import path

from . import (
    views,
    conf
)

urlpatterns = [
    path(
        "sign-up/",
        views.Register.as_view(),
        name=conf.REGISTER_URL_NAME
    ),
    path(
        "log-in/",
        views.LogIn.as_view(),
        name=conf.LOGIN_URL_NAME
    ),
    path(
        "verify/",
        views.Verify.as_view(),
        name=conf.VERIFY_URL_NAME
    ),
]