# Retrieve Operation - Django CRUD

## Overview
This document demonstrates how to retrieve Book instances using Django's ORM query methods.

## Basic Retrieve Commands

### Get All Books
```python
from bookshelf.models import Book

# Retrieve all books
all_books = Book.objects.all()
print("All books:")
for book in all_books:
    print(f"- {book}")

# Count total books
total_books = Book.objects.count()
print(f"Total books in database: {total_books}")
```

### Get a Specific Book by ID
```python
# Retrieve book by primary key (ID)
try:
    book = Book.objects.get(id=1)
    print(f"Found book: {book}")
    print(f"Publication year: {book.publication_year}")
    print(f"ISBN: {book.isbn}")
    print(f"Pages: {book.pages}")
except Book.DoesNotExist:
    print("Book with ID 1 does not exist")
```

### Get a Book by ISBN
```python
# Retrieve book by ISBN (unique field)
try:
    book = Book.objects.get(isbn="9781735467207")
    print(f"Found book by ISBN: {book}")
    print(f"Cover type: {book.get_cover_display()}")
except Book.DoesNotExist:
    print("Book with this ISBN does not exist")
```

## Advanced Retrieve Operations

### Filter Books
```python
# Filter books by author
vincent_books = Book.objects.filter(author="William S. Vincent")
print("Books by William S. Vincent:")
for book in vincent_books:
    print(f"- {book}")

# Filter books by publication year
recent_books = Book.objects.filter(publication_year__gte=2020)
print("Books published in 2020 or later:")
for book in recent_books:
    print(f"- {book} ({book.publication_year})")

# Filter books by cover type
hardcover_books = Book.objects.filter(cover="hard")
softcover_books = Book.objects.filter(cover="soft")
print(f"Hardcover books: {hardcover_books.count()}")
print(f"Softcover books: {softcover_books.count()}")
```

### Search Operations
```python
# Case-insensitive search in title
django_books = Book.objects.filter(title__icontains="django")
print("Books with 'django' in title:")
for book in django_books:
    print(f"- {book}")

# Books with more than 300 pages
thick_books = Book.objects.filter(pages__gt=300)
print("Books with more than 300 pages:")
for book in thick_books:
    print(f"- {book} ({book.pages} pages)")
```

### Get First/Last Book
```python
# Get first book (alphabetically by title due to Meta ordering)
first_book = Book.objects.first()
print(f"First book (alphabetically): {first_book}")

# Get last book
last_book = Book.objects.last()
print(f"Last book (alphabetically): {last_book}")

# Get latest book by creation date
latest_book = Book.objects.latest('created_at')
print(f"Most recently added book: {latest_book}")
```

## Expected Output Examples
```
All books:
- Django for Beginners by William S. Vincent
- Python Crash Course by Eric Matthes
Total books in database: 2

Found book: Django for Beginners by William S. Vincent
Publication year: 2022
ISBN: 9781735467207
Pages: 400

Found book by ISBN: Django for Beginners by William S. Vincent
Cover type: Softcover

Books by William S. Vincent:
- Django for Beginners by William S. Vincent

Books published in 2020 or later:
- Django for Beginners by William S. Vincent (2022)

First book (alphabetically): Django for Beginners by William S. Vincent
```

## Query Optimization Tips
```python
# Use exists() for checking existence
if Book.objects.filter(isbn="9781735467207").exists():
    print("Book exists")

# Use values() for specific fields only
book_titles = Book.objects.values_list('title', flat=True)
print("All book titles:", list(book_titles))

# Use select_related() for foreign key relationships (when applicable)
# books = Book.objects.select_related('category').all()
```

## Common Query Methods
- `all()`: Get all objects
- `filter()`: Filter objects by criteria
- `exclude()`: Exclude objects by criteria
- `get()`: Get single object (raises exception if not found or multiple found)
- `first()`: Get first object or None
- `last()`: Get last object or None
- `exists()`: Check if any objects exist
- `count()`: Count objects
- `values()`: Get dictionaries instead of model instances
- `values_list()`: Get tuples of field values
