from django.urls import path
from django.contrib.auth import views as auth_views
from .member_view import member
from .librarian_view import librarian
from . import views
from .views import admin_view


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('Admin/', views.admin_view, name="admin_view"),
    path('Librarian/', librarian, name="librarian"),
    path('Member/', member, name="member"),
]

