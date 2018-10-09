from django.urls import path


from . import views

urlpatterns = [
    path("", views.List.as_view(),),
    path("create", views.Create.as_view(),),
    path("<int:pk>", views.Update.as_view(),),
    path("<int:pk>/delete", views.Delete.as_view(),)
]