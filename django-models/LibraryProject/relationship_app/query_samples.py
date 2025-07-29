# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Chinua Achebe"
try:
    author = Author.objects.get(name=author_name)
    books_by_author = author.books.all()  # Uses related_name='books'
    print(f"\nBooks by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name '{author_name}'")

# 2. List all books in a specific library
library_name = "National Library"
try:
    library = Library.objects.get(name=library_name)
    library_books = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in library_books:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with name '{library_name}'")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # Uses related_name='librarian' in OneToOneField
    print(f"\nLibrarian for {library.name}: {librarian.name}")
except AttributeError:
    print(f"{library.name} has no assigned librarian.")
