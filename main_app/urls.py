from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
]