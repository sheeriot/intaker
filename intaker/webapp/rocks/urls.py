from django.urls import path

from . import views

urlpatterns = [
    path("", views.addrock, name="rocks"),
    path("add", views.addrock, name="addrock"),
    path("<slug:lakeslug>/add", views.addrock, name="addrock_by_lake")
]
