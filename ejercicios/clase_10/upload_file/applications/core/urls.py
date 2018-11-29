from django.urls import path

from . import (
    views,
    conf
)

urlpatterns = [
    path(
        "",
        views.SimpleUpload.as_view(),
        name=conf.FILE_UPLOAD

    )
]