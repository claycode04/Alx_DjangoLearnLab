#!/usr/bin/env python
"""
Admin Interface Demo Script
This script demonstrates the Django admin interface configuration for the Library Project.
"""

import os
import sys
import django

# Add the project directory to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book, Library
from django.contrib.auth.models import User
from django.db import IntegrityError


def create_sample_data():
    """Create sample books and libraries for testing the admin interface."""
    
    print("Creating sample data for admin interface testing...")
    
    # Sample books data
    books_data = [
        {
            'title': 'Django for Beginners',
            'author': 'William S. Vincent',
            'publication_year': 2022,
            'isbn': '9781735467207',
            'pages': 400,
            'cover': 'soft',
            'language': 'English'
        },
        {
            'title': 'Two Scoops of Django 3.x',
            'author': 'Daniel Roy Greenfeld',
            'publication_year': 2020,
            'isbn': '9780692915729',
            'pages': 532,
            'cover': 'hard',
            'language': 'English'
        },
        {
            'title': 'Python Crash Course',
            'author': 'Eric Matthes',
            'publication_year': 2019,
            'isbn': '9781593279288',
            'pages': 560,
            'cover': 'soft',
            'language': 'English'
        },
        {
            'title': 'Clean Code',
            'author': 'Robert C. Martin',
            'publication_year': 2008,
            'isbn': '9780132350884',
            'pages': 464,
            'cover': 'hard',
            'language': 'English'
        },
        {
            'title': 'The Pragmatic Programmer',
            'author': 'David Thomas',
            'publication_year': 2019,
            'isbn': '9780135957059',
            'pages': 352,
            'cover': 'soft',
            'language': 'English'
        }
    ]
    
    # Create books
    created_books = []
    for book_data in books_data:
        try:
            book, created = Book.objects.get_or_create(
                isbn=book_data['isbn'],
                defaults=book_data
            )
            if created:
                created_books.append(book)
                print(f"✓ Created book: {book.title}")
            else:
                print(f"- Book already exists: {book.title}")
        except IntegrityError as e:
            print(f"✗ Error creating book {book_data['title']}: {e}")
    
    # Sample libraries data
    libraries_data = [
        {
            'name': 'Central Library',
            'location': 'Downtown Main Street'
        },
        {
            'name': 'Tech Library',
            'location': 'University Campus'
        },
        {
            'name': 'Community Library',
            'location': 'Suburban District'
        }
    ]
    
    # Create libraries
    created_libraries = []
    for library_data in libraries_data:
        library, created = Library.objects.get_or_create(
            name=library_data['name'],
            defaults=library_data
        )
        if created:
            created_libraries.append(library)
            print(f"✓ Created library: {library.name}")
        else:
            print(f"- Library already exists: {library.name}")
    
    # Assign books to libraries
    if created_libraries and Book.objects.exists():
        all_books = Book.objects.all()
        for library in created_libraries:
            # Assign random books to each library
            if library.name == 'Central Library':
                library.books.add(*all_books[:3])
            elif library.name == 'Tech Library':
                library.books.add(*all_books.filter(title__icontains='Django'))
                library.books.add(*all_books.filter(title__icontains='Python'))
            elif library.name == 'Community Library':
                library.books.add(*all_books[2:])
            
            print(f"✓ Assigned books to {library.name}")
    
    print(f"\nSample data creation completed!")
    print(f"Total books: {Book.objects.count()}")
    print(f"Total libraries: {Library.objects.count()}")


def display_admin_info():
    """Display information about the admin interface setup."""
    
    print("\n" + "="*60)
    print("DJANGO ADMIN INTERFACE SETUP")
    print("="*60)
    
    print("\n1. ADMIN CONFIGURATION FEATURES:")
    print("   - Custom list display for Book model")
    print("   - Search functionality (title, author, ISBN)")
    print("   - Filtering options (year, cover, language)")
    print("   - Bulk actions for cover type changes")
    print("   - Organized fieldsets in detail view")
    print("   - Pagination (20 items per page)")
    
    print("\n2. MODELS REGISTERED:")
    print("   - Book (with custom BookAdmin)")
    print("   - Library (with custom LibraryAdmin)")
    
    print("\n3. ACCESSING THE ADMIN:")
    print("   - URL: http://127.0.0.1:8000/admin/")
    print("   - Create superuser: python manage.py createsuperuser")
    print("   - Run server: python manage.py runserver")
    
    print("\n4. AVAILABLE ACTIONS:")
    print("   - Add/Edit/Delete books and libraries")
    print("   - Search books by title, author, or ISBN")
    print("   - Filter books by publication year, cover type, language")
    print("   - Bulk change cover types")
    print("   - Manage library-book relationships")
    
    # Check if superuser exists
    if User.objects.filter(is_superuser=True).exists():
        print("\n✓ Superuser account exists - you can access the admin")
    else:
        print("\n⚠ No superuser found - create one with: python manage.py createsuperuser")


def main():
    """Main function to demonstrate admin interface setup."""
    
    print("Django Admin Interface Demo")
    print("Library Project - Book Management System")
    print("-" * 50)
    
    # Display admin information
    display_admin_info()
    
    # Create sample data
    create_sample_data()
    
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    print("1. Ensure you have a superuser account:")
    print("   python manage.py createsuperuser")
    print("\n2. Run the development server:")
    print("   python manage.py runserver")
    print("\n3. Access the admin interface:")
    print("   http://127.0.0.1:8000/admin/")
    print("\n4. Log in and explore the Book and Library management features!")
    print("\n5. Try the following in the admin:")
    print("   - Search for books by title or author")
    print("   - Filter books by publication year")
    print("   - Use bulk actions to change cover types")
    print("   - Add new books and libraries")
    print("   - Assign books to libraries")


if __name__ == "__main__":
    main()
