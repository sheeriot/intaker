from django.urls import path

from . import views

urlpatterns = [
    path("", views.addrock, name="rocks"),
    path("addrock", views.addrock, name="addrock")
]
