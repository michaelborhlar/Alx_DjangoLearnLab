from django.urls import path
from django.contrib.auth import views as auth_views
from .admin_view import admin
from .member_view import member
from .librarian_view import librarian

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('Admin/', admin, name="admin"),
    path('Librarian/', librarian, name="librarian"),
    path('Member/', member, name="member"),
]

