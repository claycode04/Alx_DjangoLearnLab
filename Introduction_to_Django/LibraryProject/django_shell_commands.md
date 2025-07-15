# Django CRUD Operations - Step by Step Commands

## Step 1: Start Django Shell
```bash
python manage.py shell
```

## Step 2: Import the Model
```python
from bookshelf.models import Book
```

## Step 3: CREATE - Create a Book Instance
```python
# Create first book
book1 = Book.objects.create(
    title="Django for Beginners",
    author="William S. Vincent",
    publication_year=2022,
    isbn="9781735467207",
    pages=400,
    cover="soft",
    language="English"
)
print(f"Created: {book1}")
print(f"Book ID: {book1.id}")
```

## Step 4: RETRIEVE - Get the Book
```python
# Retrieve the book we just created
retrieved_book = Book.objects.get(id=1)
print(f"Retrieved: {retrieved_book}")
print(f"Title: {retrieved_book.title}")
print(f"Author: {retrieved_book.author}")
print(f"Pages: {retrieved_book.pages}")
print(f"ISBN: {retrieved_book.isbn}")
```

## Step 5: UPDATE - Update the Book Title
```python
# Update the title
book_to_update = Book.objects.get(id=1)
original_title = book_to_update.title
book_to_update.title = "Django for Beginners: Build websites with Python and Django"
book_to_update.save()

print(f"Original title: {original_title}")
print(f"Updated title: {book_to_update.title}")
print(f"Updated at: {book_to_update.updated_at}")
```

## Step 6: DELETE - Delete the Book
```python
# Delete the book
book_to_delete = Book.objects.get(id=1)
book_title = book_to_delete.title
book_to_delete.delete()

print(f"Deleted book: {book_title}")

# Verify deletion
if not Book.objects.filter(id=1).exists():
    print("Confirmed: Book has been deleted")
else:
    print("Error: Book still exists")
```

## Complete Script to Run in Django Shell
```python
# Complete CRUD operations script
from bookshelf.models import Book

# CREATE
print("=== CREATE OPERATION ===")
book = Book.objects.create(
    title="Django for Beginners",
    author="William S. Vincent",
    publication_year=2022,
    isbn="9781735467207",
    pages=400,
    cover="soft",
    language="English"
)
print(f"✓ Created: {book}")
print(f"  ID: {book.id}")
print(f"  Created at: {book.created_at}")

# RETRIEVE
print("\n=== RETRIEVE OPERATION ===")
retrieved_book = Book.objects.get(id=book.id)
print(f"✓ Retrieved: {retrieved_book}")
print(f"  Title: {retrieved_book.title}")
print(f"  Author: {retrieved_book.author}")
print(f"  Pages: {retrieved_book.pages}")
print(f"  Cover: {retrieved_book.get_cover_display()}")

# UPDATE
print("\n=== UPDATE OPERATION ===")
original_title = retrieved_book.title
retrieved_book.title = "Django for Beginners: Build websites with Python and Django"
retrieved_book.pages = 450
retrieved_book.save()
print(f"✓ Updated book:")
print(f"  Old title: {original_title}")
print(f"  New title: {retrieved_book.title}")
print(f"  New pages: {retrieved_book.pages}")
print(f"  Updated at: {retrieved_book.updated_at}")

# DELETE
print("\n=== DELETE OPERATION ===")
book_id = retrieved_book.id
book_title = retrieved_book.title
retrieved_book.delete()
print(f"✓ Deleted: {book_title}")

# Verify deletion
if not Book.objects.filter(id=book_id).exists():
    print("✓ Confirmed: Book no longer exists in database")
else:
    print("✗ Error: Book still exists")

print("\n=== CRUD OPERATIONS COMPLETED ===")
```

## Running the Commands

1. **Open Django Shell:**
   ```bash
   python manage.py shell
   ```

2. **Copy and paste the complete script above into the shell**

3. **Or run individual commands one by one for better understanding**

## Expected Output
```
=== CREATE OPERATION ===
✓ Created: Django for Beginners by William S. Vincent
  ID: 1
  Created at: 2025-07-13 23:30:45.123456+00:00

=== RETRIEVE OPERATION ===
✓ Retrieved: Django for Beginners by William S. Vincent
  Title: Django for Beginners
  Author: William S. Vincent
  Pages: 400
  Cover: Softcover

=== UPDATE OPERATION ===
✓ Updated book:
  Old title: Django for Beginners
  New title: Django for Beginners: Build websites with Python and Django
  New pages: 450
  Updated at: 2025-07-13 23:30:50.789012+00:00

=== DELETE OPERATION ===
✓ Deleted: Django for Beginners: Build websites with Python and Django
✓ Confirmed: Book no longer exists in database

=== CRUD OPERATIONS COMPLETED ===
```
