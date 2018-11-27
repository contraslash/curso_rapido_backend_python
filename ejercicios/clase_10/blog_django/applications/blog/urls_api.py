from django.urls import path

from . import api

urlpatterns = [
    path(
        "post/",
        api.Post.as_view()
    ),
    path(
        "post/<int:id>",
        api.PostWithId.as_view(),
    ),
]