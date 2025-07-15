#!/usr/bin/env python
"""
Django CRUD Operations Demo Script
This script demonstrates Create, Read, Update, Delete operations on the Book model.
Run this script in the Django shell environment.
"""

from bookshelf.models import Book
from django.utils import timezone
from django.db import models

def demo_crud_operations():
    """Demonstrate all CRUD operations with the Book model."""
    
    print("=" * 60)
    print("DJANGO CRUD OPERATIONS DEMO")
    print("=" * 60)
    
    # ========== CREATE OPERATIONS ==========
    print("\n1. CREATE OPERATIONS")
    print("-" * 30)
    
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
    print(f"✓ Created book 1: {book1}")
    
    # Create second book
    book2 = Book.objects.create(
        title="Python Crash Course",
        author="Eric Matthes",
        publication_year=2019,
        isbn="9781593279288",
        pages=544,
        cover="hard",
        language="English"
    )
    print(f"✓ Created book 2: {book2}")
    
    # Create third book using different method
    book3 = Book(
        title="Two Scoops of Django",
        author="Daniel Roy Greenfeld",
        publication_year=2020,
        isbn="9780981467344",
        pages=532,
        cover="soft",
        language="English"
    )
    book3.save()
    print(f"✓ Created book 3: {book3}")
    
    # ========== READ/RETRIEVE OPERATIONS ==========
    print("\n2. READ/RETRIEVE OPERATIONS")
    print("-" * 30)
    
    # Get all books
    all_books = Book.objects.all()
    print(f"📚 Total books in database: {all_books.count()}")
    for book in all_books:
        print(f"  - {book}")
    
    # Get specific book by ID
    try:
        specific_book = Book.objects.get(id=1)
        print(f"📖 Book with ID 1: {specific_book}")
        print(f"   Pages: {specific_book.pages}")
        print(f"   Cover: {specific_book.get_cover_display()}")
    except Book.DoesNotExist:
        print("❌ Book with ID 1 not found")
    
    # Filter books
    django_books = Book.objects.filter(title__icontains="django")
    print(f"🔍 Books with 'django' in title: {django_books.count()}")
    for book in django_books:
        print(f"  - {book}")
    
    # Books published after 2020
    recent_books = Book.objects.filter(publication_year__gte=2020)
    print(f"📅 Recent books (2020+): {recent_books.count()}")
    for book in recent_books:
        print(f"  - {book} ({book.publication_year})")
    
    # ========== UPDATE OPERATIONS ==========
    print("\n3. UPDATE OPERATIONS")
    print("-" * 30)
    
    # Update single book
    book_to_update = Book.objects.get(id=1)
    original_title = book_to_update.title
    book_to_update.title = "Django for Beginners: Build websites with Python and Django"
    book_to_update.pages = 450
    book_to_update.save()
    print(f"✏️ Updated book 1:")
    print(f"   Old title: {original_title}")
    print(f"   New title: {book_to_update.title}")
    print(f"   New pages: {book_to_update.pages}")
    
    # Bulk update
    updated_count = Book.objects.filter(author="Eric Matthes").update(
        language="English (US)"
    )
    print(f"📝 Bulk updated {updated_count} books by Eric Matthes")
    
    # Update with F() expression
    Book.objects.filter(id=2).update(pages=models.F('pages') + 56)
    updated_book = Book.objects.get(id=2)
    print(f"➕ Added 56 pages to book 2, now has {updated_book.pages} pages")
    
    # ========== DELETE OPERATIONS ==========
    print("\n4. DELETE OPERATIONS")
    print("-" * 30)
    
    # Show current count
    print(f"📊 Books before deletion: {Book.objects.count()}")
    
    # Delete specific book
    book_to_delete = Book.objects.get(id=3)
    deleted_title = book_to_delete.title
    book_to_delete.delete()
    print(f"🗑️ Deleted book: {deleted_title}")
    
    # Verify deletion
    if not Book.objects.filter(id=3).exists():
        print("✓ Confirmed: Book 3 no longer exists")
    
    # Show remaining books
    remaining_books = Book.objects.all()
    print(f"📊 Books after deletion: {remaining_books.count()}")
    for book in remaining_books:
        print(f"  - {book}")
    
    # ========== ADVANCED OPERATIONS ==========
    print("\n5. ADVANCED OPERATIONS")
    print("-" * 30)
    
    # Get or create
    book, created = Book.objects.get_or_create(
        isbn="9781492052088",
        defaults={
            'title': "Learning Python",
            'author': "Mark Lutz",
            'publication_year': 2021,
            'pages': 1648,
            'cover': "hard",
            'language': "English"
        }
    )
    
    if created:
        print(f"🆕 Created new book: {book}")
    else:
        print(f"📚 Book already exists: {book}")
    
    # Update or create
    book, created = Book.objects.update_or_create(
        isbn="9781492052088",
        defaults={
            'title': "Learning Python: 5th Edition",
            'author': "Mark Lutz",
            'publication_year': 2022,
            'pages': 1700,
            'cover': "hard",
            'language': "English"
        }
    )
    
    if created:
        print(f"🆕 Created book: {book}")
    else:
        print(f"📝 Updated book: {book}")
    
    # Final statistics
    print("\n" + "=" * 60)
    print("FINAL STATISTICS")
    print("=" * 60)
    
    total_books = Book.objects.count()
    total_pages = Book.objects.aggregate(
        total_pages=models.Sum('pages')
    )['total_pages']
    
    avg_pages = Book.objects.aggregate(
        avg_pages=models.Avg('pages')
    )['avg_pages']
    
    print(f"📊 Total books: {total_books}")
    print(f"📄 Total pages: {total_pages}")
    print(f"📈 Average pages per book: {avg_pages:.1f}")
    
    # Show all books with details
    print(f"\n📚 All books in library:")
    for book in Book.objects.all():
        print(f"  📖 {book}")
        print(f"     ISBN: {book.isbn}")
        print(f"     Pages: {book.pages}")
        print(f"     Cover: {book.get_cover_display()}")
        print(f"     Language: {book.language}")
        print(f"     Created: {book.created_at.strftime('%Y-%m-%d %H:%M')}")
        print()

if __name__ == "__main__":
    demo_crud_operations()
