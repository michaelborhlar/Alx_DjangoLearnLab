from relationship_app.models import Author, Book, Library, Librarian

# ============================
# 1. Query all books by a specific author
# ============================

author_name = "Chinua Achebe"

try:
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # <-- Required by your task
    print(f"\nBooks by {author.name}:")
    if books.exists():
        for book in books:
            print(f"- {book.title}")
    else:
        print("No books found for this author.")
except Author.DoesNotExist:
    print(f"No author found with the name '{author_name}'.")

# ============================
# 2. List all books in a specific library
# ============================

library_name = "National Library"

try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"\nBooks in {library.name}:")
    if books_in_library.exists():
        for book in books_in_library:
            print(f"- {book.title}")
    else:
        print("No books in this library.")
except Library.DoesNotExist:
    print(f"No library found with the name '{library_name}'.")

# ============================
# 3. Retrieve the librarian for a library
# ============================

try:
    librarian = Librarian.objects.get(library=library)  # <-- Required by your task
    print(f"\nLibrarian of {library.name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"{library.name} has no assigned librarian.")
except NameError:
    print("Library not found earlier, so can't find a librarian.")
