from django.shortcuts import render, get_object_or_404
from django.views.generic.detail import DetailView
from .models import Book
from .models import Library
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render
from .models import UserProfile


from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import UserProfile

def check_role(user, required_role):
    try:
        return user.userprofile.role == required_role
    except UserProfile.DoesNotExist:
        return False

def admin_check(user):
    return check_role(user, 'ADMIN')

def librarian_check(user):
    return check_role(user, 'LIBRARIAN')

def member_check(user):
    return check_role(user, 'MEMBER')

@login_required
@user_passes_test(admin_check)
def admin_view(request):
    return render(request, 'admin_view.html')

@login_required
@user_passes_test(librarian_check)
def librarian_view(request):
    return render(request, 'librarian_view.html')

@login_required
@user_passes_test(member_check)
def member_view(request):
    return render(request, 'member_view.html')



class register(CreateView):
    form_class=UserCreationForm
    success_url=reverse_lazy('login')
    template_name="relationship_app/register.html"


# Function-based view: List all books with authors
def list_books(request):
    books = books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# views.py
