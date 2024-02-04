from django.urls import path
from .views import *
from django.contrib.auth.views import LoginView,LogoutView

app_name='Users'

urlpatterns = [
    path('',register,name='register'),
    path('login/',LoginView.as_view(template_name='Users/login.html') ,name='login'),
    path('logout/',LogoutView.as_view(template_name='Users/logout.html') ,name='logout'),
    path('profile/',profile,name='profile'),
    path('profile/edit',edit_profile,name='edit_profile'),
    path('profile/author/<int:pk>/',author_profile,name='author_profile'),
]
