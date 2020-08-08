from django.urls import path 
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('login/', views.login_page, name='login_page'),
    path('signup/', views.signup, name='signup'),
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/edit/', views.edit_profile, name='edit_profile'),
    path('accounts/profile/<int:post_id>/', views.profile_post, name='profile_post'),
    path('accounts/profile/<int:post_id>/edit/', views.profile_editpost, name='profile_editpost'),
    path('accounts/profile/<int:post_id>/deletepost/', views.profile_deletepost, name='profile_deletepost'),
    path('cities/<int:city_id>/', views.show_city, name='show_city'),
    path('cities/<int:city_id>/newpost/', views.newpost, name='newpost'),
    path('cities/<int:city_id>/editpost/<int:post_id>/', views.editpost, name='editpost'),
    path('cities/<int:city_id>/deletepost/<int:post_id>/', views.deletepost, name='deletepost'),
    path('cities/<int:city_id>/<int:post_id>/', views.city_post, name='city_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)