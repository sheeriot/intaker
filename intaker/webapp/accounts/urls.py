from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login.as_view(), name='login'),
    path('logout/', views.logout, name='logout'),
]
