# Retrieve the Book instance

```python
from bookshelf.models import Book
Book.objects.get(title="1984")
# Output:
<Book: 1984>