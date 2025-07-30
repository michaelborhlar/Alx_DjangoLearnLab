from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-based view: List all books with authors
def list_books(request):
    books = books = Book.objects.all()

    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view: Display library details
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
