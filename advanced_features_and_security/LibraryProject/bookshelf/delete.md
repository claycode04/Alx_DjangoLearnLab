# Delete Operation - Django CRUD

## Overview
This document demonstrates how to delete Book instances using Django's ORM delete methods.

## Basic Delete Commands

### Delete a Single Book Instance
```python
from bookshelf.models import Book

# Get and delete a specific book
try:
    book = Book.objects.get(id=1)
    book_title = book.title  # Store title before deletion
    book_id = book.id
    
    book.delete()
    print(f"Successfully deleted book: '{book_title}' (ID: {book_id})")
    
    # Verify deletion
    if not Book.objects.filter(id=book_id).exists():
        print("Confirmed: Book no longer exists in database")
        
except Book.DoesNotExist:
    print("Book with ID 1 does not exist")
```

### Delete by Specific Criteria
```python
# Delete book by ISBN
try:
    book = Book.objects.get(isbn="9781735467207")
    book_info = f"{book.title} by {book.author}"
    book.delete()
    print(f"Deleted book: {book_info}")
except Book.DoesNotExist:
    print("Book with this ISBN does not exist")
```

## Bulk Delete Operations

### Delete Multiple Records
```python
# Delete all books by a specific author
books_to_delete = Book.objects.filter(author="William S. Vincent")
count = books_to_delete.count()
print(f"Found {count} books by William S. Vincent")

if count > 0:
    # Show books before deletion
    print("Books to be deleted:")
    for book in books_to_delete:
        print(f"- {book}")
    
    # Perform deletion
    deleted_count, deleted_details = books_to_delete.delete()
    print(f"Successfully deleted {deleted_count} books")
    print(f"Deletion details: {deleted_details}")
```

### Delete with Complex Filters
```python
# Delete all books published before 2020 with less than 300 pages
old_short_books = Book.objects.filter(
    publication_year__lt=2020,
    pages__lt=300
)

count = old_short_books.count()
print(f"Found {count} old books with less than 300 pages")

if count > 0:
    deleted_count, _ = old_short_books.delete()
    print(f"Deleted {deleted_count} books")
else:
    print("No books match the deletion criteria")
```

## Advanced Delete Operations

### Delete All Records (Dangerous!)
```python
# Delete ALL books (use with extreme caution!)
total_books = Book.objects.count()
print(f"Total books before deletion: {total_books}")

# Uncomment the next lines to actually delete all books
# deleted_count, _ = Book.objects.all().delete()
# print(f"Deleted all {deleted_count} books")

print("WARNING: Above deletion is commented out for safety")
```

### Conditional Delete with Confirmation
```python
# Delete books with confirmation logic
def safe_delete_books(filter_kwargs, confirm=False):
    books_to_delete = Book.objects.filter(**filter_kwargs)
    count = books_to_delete.count()
    
    if count == 0:
        print("No books found matching the criteria")
        return
    
    print(f"Found {count} books to delete:")
    for book in books_to_delete:
        print(f"- {book}")
    
    if confirm:
        deleted_count, _ = books_to_delete.delete()
        print(f"Successfully deleted {deleted_count} books")
    else:
        print("Deletion not confirmed. No books were deleted.")

# Example usage
safe_delete_books({'cover': 'soft'}, confirm=False)  # Dry run
# safe_delete_books({'cover': 'soft'}, confirm=True)  # Actual deletion
```

## Soft Delete Alternative

### Mark as Deleted Instead of Actual Deletion
```python
# If you want to implement soft delete, you would modify the model first
# and add an 'is_deleted' field, then filter it out in queries

# For demonstration, let's add a field temporarily
# (This would normally be in the model definition)

# Simulate soft delete by updating a field
books_to_soft_delete = Book.objects.filter(author="Test Author")
if books_to_soft_delete.exists():
    # In a real soft delete implementation, you'd set is_deleted=True
    # books_to_soft_delete.update(is_deleted=True)
    print(f"Would soft delete {books_to_soft_delete.count()} books")
```

## Cascade Delete Behavior

### Understanding Related Object Deletion
```python
from bookshelf.models import Library, Librarian
from django.contrib.auth.models import User

# Create test data to demonstrate cascade behavior
user = User.objects.create_user(username="testlibrarian", email="test@library.com")
library = Library.objects.create(name="Test Library", location="Test City")
librarian = Librarian.objects.create(user=user, library=library)

print(f"Created librarian: {librarian}")
print(f"Associated user: {user}")
print(f"Associated library: {library}")

# When we delete the user, the librarian will also be deleted (CASCADE)
user_id = user.id
librarian_id = librarian.id

user.delete()

# Check if librarian still exists
if not Librarian.objects.filter(id=librarian_id).exists():
    print("Librarian was automatically deleted due to CASCADE relationship")

# Library still exists because it's SET_NULL relationship
if Library.objects.filter(id=library.id).exists():
    print("Library still exists (SET_NULL relationship)")
```

## Error Handling and Safety

### Safe Delete with Try-Catch
```python
def safe_delete_book(book_id):
    try:
        book = Book.objects.get(id=book_id)
        book_info = f"{book.title} by {book.author}"
        book.delete()
        return f"Successfully deleted: {book_info}"
    except Book.DoesNotExist:
        return f"Book with ID {book_id} does not exist"
    except Exception as e:
        return f"Error deleting book: {e}"

# Test the safe delete function
result = safe_delete_book(1)
print(result)

result = safe_delete_book(999)  # Non-existent ID
print(result)
```

### Backup Before Delete
```python
import json
from django.core import serializers

# Create backup before bulk delete
books_to_backup = Book.objects.filter(publication_year__lt=2020)

if books_to_backup.exists():
    # Create JSON backup
    backup_data = serializers.serialize('json', books_to_backup)
    
    # Save to file (in real scenario)
    # with open('book_backup.json', 'w') as f:
    #     f.write(backup_data)
    
    print(f"Backed up {books_to_backup.count()} books")
    print("Backup data length:", len(backup_data))
    
    # Now safe to delete
    # deleted_count, _ = books_to_backup.delete()
    # print(f"Deleted {deleted_count} books after backup")
```

## Expected Output Examples
```
Successfully deleted book: 'Django for Beginners' (ID: 1)
Confirmed: Book no longer exists in database

Found 1 books by William S. Vincent
Books to be deleted:
- Django for Beginners by William S. Vincent
Successfully deleted 1 books
Deletion details: {'bookshelf.Book': 1}

Found 0 old books with less than 300 pages
No books match the deletion criteria

Total books before deletion: 2
WARNING: Above deletion is commented out for safety

Found 1 books to delete:
- Python Crash Course by Eric Matthes
Deletion not confirmed. No books were deleted.

Successfully deleted: Python Crash Course by Eric Matthes
Book with ID 999 does not exist
```

## Important Safety Notes

⚠️ **DANGER ZONE - Always be careful with delete operations!**

1. **Always backup important data before bulk deletions**
2. **Test delete operations on development data first**
3. **Use transactions for complex delete operations**
4. **Consider soft delete for important records**
5. **Be aware of cascade relationships**
6. **Use filters carefully to avoid deleting wrong records**

## Performance Considerations

```python
# Efficient: Bulk delete
Book.objects.filter(author="Unwanted Author").delete()

# Inefficient: Individual deletes
# for book in Book.objects.filter(author="Unwanted Author"):
#     book.delete()  # Multiple database hits
```

## Recovery Options

If you accidentally delete data:
1. **Database backups**: Restore from recent backup
2. **Version control**: If using fixtures or migrations
3. **Soft delete**: Implement is_deleted field instead of actual deletion
4. **Audit logs**: Track all delete operations for accountability
