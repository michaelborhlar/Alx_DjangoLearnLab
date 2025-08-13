# Book API Endpoints

## List all books
GET /api/books/
Permissions: Public

## Retrieve single book
GET /api/books/<id>/
Permissions: Public

## Create book
POST /api/books/create/
Permissions: Authenticated users only
Body:
{
  "title": "My Book",
  "author": "Author Name",
  "published_date": "2025-01-01",
  "isbn": "1234567890123"
}
