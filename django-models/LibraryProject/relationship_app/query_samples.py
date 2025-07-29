# relationship_app/query_samples.py

from relationship_app.models import Author, Book, Library, Librarian

# 1. Query all books by a specific author
author_name = "Chinua Achebe"

try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # ✅ This is the line you're missing
    print(f"\nBooks by {author.name}:")
    for book in books:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.")

# 2. List all books in a specific library
library_name = "National Library"

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    for book in books_in_library:
        print(f"- {book.title}")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")

# 3. Retrieve the librarian for a library
try:
    librarian = library.librarian  # because of related_name="librarian"
    print(f"\nLibrarian of {library.name}: {librarian.name}")
except AttributeError:
    print(f"{library.name} has no assigned librarian.")
