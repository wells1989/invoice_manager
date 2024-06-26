from . import views
from .views import CustomLoginView
from django.urls import path
from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('login/', CustomLoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('setup/', views.setup, name='setup'),

    path('change_username/', views.change_username, name='change_username'),
    path('change_password/', views.change_password, name='change_password')
]
