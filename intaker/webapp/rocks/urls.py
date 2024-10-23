from django.urls import path

# from . import views
from .views.rockadd import rockadd
from .views.lakes import lakes
from .views.rocks import rocks
from .views.rockstable_edit import rockstable_edit

urlpatterns = [
    path("list", rocks, name="rocks"),
    path("lakes", lakes, name="lakes"),
    # path("add", views.addrock, name="addrock"),
    path("<slug:lakeslug>/add", rockadd, name="rockadd_by_lake"),
    path("<slug:lakeslug>/list", rocks, name="rocklist_by_lake"),
    path("<slug:lakeslug>/edit", rockstable_edit, name='rockstable_edit'),
]
