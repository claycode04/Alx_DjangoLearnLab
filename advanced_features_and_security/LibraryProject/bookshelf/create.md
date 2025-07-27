# Create Operation - Django CRUD

## Overview
This document demonstrates how to create a new Book instance using Django's ORM in the Django shell.

## Command
```python
from bookshelf.models import Book

# Create a new Book instance
book = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949,
    isbn="9781735467207",
    pages=400,
    cover="soft",
    language="English"
)

# Display the created book
print(book)
print(f"Book ID: {book.id}")
print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Created at: {book.created_at}")
```

## Expected Output
```
Django for Beginners by William S. Vincent
Book ID: 1
Title: Django for Beginners
Author: William S. Vincent
Created at: 2025-07-13 23:15:42.123456+00:00
```

## Alternative Creation Methods

### Method 1: Create and Save
```python
book = Book(
    title="Python Crash Course",
    author="Eric Matthes",
    publication_year=2019,
    isbn="9781593279288",
    pages=544,
    cover="soft",
    language="English"
)
book.save()
print(f"Created book: {book}")
```

### Method 2: get_or_create
```python
book, created = Book.objects.get_or_create(
    isbn="9781593279288",
    defaults={
        'title': "Python Crash Course",
        'author': "Eric Matthes",
        'publication_year': 2019,
        'pages': 544,
        'cover': "soft",
        'language': "English"
    }
)

if created:
    print(f"New book created: {book}")
else:
    print(f"Book already exists: {book}")
```

## Notes
- The `create()` method creates and saves the object in one step
- The `isbn` field must be unique due to the unique constraint
- `created_at` and `updated_at` are automatically populated
- The `__str__` method formats the output as "Title by Author"

## Validation
The model includes several built-in validations:
- `title`: Maximum 200 characters
- `author`: Maximum 100 characters  
- `publication_year`: Must be a positive integer
- `isbn`: Must be unique and maximum 13 characters
- `pages`: Must be a positive integer
- `cover`: Must be either 'hard' or 'soft'
