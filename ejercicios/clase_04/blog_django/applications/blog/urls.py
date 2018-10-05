from django.urls import path

from . import (
    views,
    conf,
)

urlpatterns = [
    path(
        "list/",
        views.List.as_view(),
        name=conf.BLOG_LIST_URL_NAME
    ),
    path(
        "create/",
        views.Create.as_view(),
        name=conf.BLOG_CREATE_URL_NAME
    ),
    path(
        "<int:post_id>/",
        views.Detail.as_view(),
        name=conf.BLOG_DETAIL_URL_NAME
    )
]