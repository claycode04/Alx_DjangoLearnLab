@echo off
echo Starting Django CRUD Operations Demo...
echo.

echo Step 1: Opening Django Shell and running CRUD operations...
python manage.py shell << EOF
from bookshelf.models import Book

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

print("\n=== RETRIEVE OPERATION ===")
retrieved_book = Book.objects.get(id=book.id)
print(f"✓ Retrieved: {retrieved_book}")
print(f"  Title: {retrieved_book.title}")
print(f"  Author: {retrieved_book.author}")
print(f"  Pages: {retrieved_book.pages}")
print(f"  Cover: {retrieved_book.get_cover_display()}")

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

print("\n=== DELETE OPERATION ===")
book_id = retrieved_book.id
book_title = retrieved_book.title
retrieved_book.delete()
print(f"✓ Deleted: {book_title}")

if not Book.objects.filter(id=book_id).exists():
    print("✓ Confirmed: Book no longer exists in database")
else:
    print("✗ Error: Book still exists")

print("\n=== CRUD OPERATIONS COMPLETED ===")
EOF

echo.
echo CRUD Operations Demo completed successfully!
pause
