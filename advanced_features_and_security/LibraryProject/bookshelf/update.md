# Update Operation - Django CRUD

## Overview
This document demonstrates how to update Book instances using Django's ORM update methods.

## Basic Update Commands

### Update a Single Book Instance
```python
from bookshelf.models import Book

# Get the book to update
try:
    book = Book.objects.get(id=1)
    print(f"Original title: {book.title}")
    
    # Update the title
    book.title = "Nineteen Eighty-Four"
    book.save()
    
    print(f"Updated title: {book.title}")
    print(f"Updated at: {book.updated_at}")
    
except Book.DoesNotExist:
    print("Book with ID 1 does not exist")
```

### Update Multiple Fields
```python
# Get book by ISBN and update multiple fields
try:
    book = Book.objects.get(isbn="9781735467207")
    
    # Store original values
    original_title = book.title
    original_pages = book.pages
    
    # Update multiple fields
    book.title = "Django for Beginners: Learn web development with Django"
    book.pages = 450
    book.cover = "hard"
    book.save()
    
    print(f"Title updated from '{original_title}' to '{book.title}'")
    print(f"Pages updated from {original_pages} to {book.pages}")
    print(f"Cover changed to: {book.get_cover_display()}")
    
except Book.DoesNotExist:
    print("Book not found")
```

## Bulk Update Operations

### Update Multiple Records at Once
```python
# Update all books by a specific author
updated_count = Book.objects.filter(author="William S. Vincent").update(
    language="English (US)"
)
print(f"Updated {updated_count} books")

# Update all softcover books to hardcover
updated_count = Book.objects.filter(cover="soft").update(cover="hard")
print(f"Changed {updated_count} books to hardcover")

# Add 50 pages to all books published before 2020
updated_count = Book.objects.filter(publication_year__lt=2020).update(
    pages=models.F('pages') + 50
)
print(f"Added 50 pages to {updated_count} books")
```

### Update with F() expressions
```python
from django.db import models

# Increment pages for a specific book using F() expression
book = Book.objects.get(id=1)
Book.objects.filter(id=1).update(pages=models.F('pages') + 25)

# Refresh the book instance to see the updated value
book.refresh_from_db()
print(f"Book now has {book.pages} pages")
```

## Advanced Update Operations

### Update or Create
```python
# Update book if exists, create if it doesn't
book, created = Book.objects.update_or_create(
    isbn="9781593279288",
    defaults={
        'title': "Python Crash Course: 3rd Edition",
        'author': "Eric Matthes",
        'publication_year': 2023,
        'pages': 600,
        'cover': "hard",
        'language': "English"
    }
)

if created:
    print(f"Created new book: {book}")
else:
    print(f"Updated existing book: {book}")
```

### Conditional Updates
```python
# Update only if certain conditions are met
books_to_update = Book.objects.filter(
    publication_year__lt=2020,
    pages__lt=300
)

if books_to_update.exists():
    updated_count = books_to_update.update(
        title=models.Concat(models.F('title'), models.Value(' - Classic Edition'))
    )
    print(f"Updated {updated_count} classic books")
else:
    print("No books match the update criteria")
```

## Field-Specific Updates

### Update Text Fields
```python
# Update title with string manipulation
book = Book.objects.get(id=1)
book.title = book.title.upper()  # Convert to uppercase
book.save()
print(f"Title in uppercase: {book.title}")

# Reset to proper case
book.title = "Django for Beginners"
book.save()
```

### Update Choice Fields
```python
# Update cover type
book = Book.objects.get(id=1)
print(f"Current cover: {book.get_cover_display()}")

book.cover = "hard" if book.cover == "soft" else "soft"
book.save()
print(f"New cover: {book.get_cover_display()}")
```

### Update Date Fields
```python
from django.utils import timezone

# Note: created_at is auto_now_add, so it can't be updated
# updated_at is auto_now, so it updates automatically

# Force update the updated_at timestamp
book = Book.objects.get(id=1)
book.save(update_fields=['updated_at'])
print(f"Timestamp updated to: {book.updated_at}")
```

## Expected Output Examples
```
Original title: Django for Beginners
Updated title: Django for Beginners: Build websites with Python and Django
Updated at: 2025-07-13 23:20:15.789012+00:00

Title updated from 'Django for Beginners' to 'Django for Beginners: Learn web development with Django'
Pages updated from 400 to 450
Cover changed to: Hardcover

Updated 1 books
Changed 0 books to hardcover
Added 50 pages to 1 books

Book now has 475 pages

Updated existing book: Python Crash Course: 3rd Edition by Eric Matthes
```

## Performance Considerations

### Efficient Updates
```python
# Good: Bulk update (single database query)
Book.objects.filter(author="John Doe").update(language="English")

# Avoid: Individual updates (multiple database queries)
# for book in Book.objects.filter(author="John Doe"):
#     book.language = "English"
#     book.save()
```

### Update Specific Fields Only
```python
# Only update specific fields to optimize performance
book = Book.objects.get(id=1)
book.title = "New Title"
book.save(update_fields=['title'])  # Only updates title field
```

## Error Handling
```python
try:
    book = Book.objects.get(id=999)
    book.title = "Non-existent Book"
    book.save()
except Book.DoesNotExist:
    print("Cannot update: Book does not exist")
except Exception as e:
    print(f"Update failed: {e}")
```

## Important Notes
- Always use `save()` after modifying individual instances
- Use `update()` for bulk operations - it's more efficient
- `update()` doesn't trigger model `save()` method or signals
- `updated_at` field is automatically updated when using `save()`
- Use `F()` expressions for atomic updates and to avoid race conditions
