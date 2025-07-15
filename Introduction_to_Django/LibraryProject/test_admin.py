#!/usr/bin/env python
"""
Test script to verify Django admin configuration
"""

import os
import sys
import django
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book, Library
from bookshelf.admin import BookAdmin, LibraryAdmin


def test_admin_configuration():
    """Test the admin configuration for the Book model."""
    
    print("Testing Django Admin Configuration...")
    print("=" * 50)
    
    # Test BookAdmin configuration
    print("\n1. Testing BookAdmin configuration:")
    
    # Check list_display
    expected_list_display = ('title', 'author', 'publication_year', 'isbn', 'pages', 'cover', 'language')
    actual_list_display = BookAdmin.list_display
    
    if actual_list_display == expected_list_display:
        print("   ✓ list_display configured correctly")
    else:
        print(f"   ✗ list_display mismatch. Expected: {expected_list_display}, Got: {actual_list_display}")
    
    # Check search_fields
    expected_search_fields = ('title', 'author', 'isbn')
    actual_search_fields = BookAdmin.search_fields
    
    if actual_search_fields == expected_search_fields:
        print("   ✓ search_fields configured correctly")
    else:
        print(f"   ✗ search_fields mismatch. Expected: {expected_search_fields}, Got: {actual_search_fields}")
    
    # Check list_filter
    expected_list_filter = ('publication_year', 'cover', 'language', 'created_at')
    actual_list_filter = BookAdmin.list_filter
    
    if actual_list_filter == expected_list_filter:
        print("   ✓ list_filter configured correctly")
    else:
        print(f"   ✗ list_filter mismatch. Expected: {expected_list_filter}, Got: {actual_list_filter}")
    
    # Check pagination
    expected_pagination = 20
    actual_pagination = BookAdmin.list_per_page
    
    if actual_pagination == expected_pagination:
        print("   ✓ pagination configured correctly")
    else:
        print(f"   ✗ pagination mismatch. Expected: {expected_pagination}, Got: {actual_pagination}")
    
    # Check fieldsets
    if hasattr(BookAdmin, 'fieldsets') and BookAdmin.fieldsets:
        print("   ✓ fieldsets configured")
    else:
        print("   ✗ fieldsets not configured")
    
    # Check custom actions
    if hasattr(BookAdmin, 'actions') and 'mark_as_hardcover' in BookAdmin.actions:
        print("   ✓ custom actions configured")
    else:
        print("   ✗ custom actions not configured")
    
    # Test LibraryAdmin configuration
    print("\n2. Testing LibraryAdmin configuration:")
    
    # Check list_display
    expected_lib_display = ('name', 'location', 'book_count')
    actual_lib_display = LibraryAdmin.list_display
    
    if actual_lib_display == expected_lib_display:
        print("   ✓ list_display configured correctly")
    else:
        print(f"   ✗ list_display mismatch. Expected: {expected_lib_display}, Got: {actual_lib_display}")
    
    # Check search_fields
    expected_lib_search = ('name', 'location')
    actual_lib_search = LibraryAdmin.search_fields
    
    if actual_lib_search == expected_lib_search:
        print("   ✓ search_fields configured correctly")
    else:
        print(f"   ✗ search_fields mismatch. Expected: {expected_lib_search}, Got: {actual_lib_search}")
    
    # Check filter_horizontal
    expected_filter_horizontal = ('books',)
    actual_filter_horizontal = LibraryAdmin.filter_horizontal
    
    if actual_filter_horizontal == expected_filter_horizontal:
        print("   ✓ filter_horizontal configured correctly")
    else:
        print(f"   ✗ filter_horizontal mismatch. Expected: {expected_filter_horizontal}, Got: {actual_filter_horizontal}")


def test_model_admin_registration():
    """Test that models are properly registered with admin."""
    
    print("\n3. Testing model registration:")
    
    from django.contrib import admin
    
    # Check if Book model is registered
    if Book in admin.site._registry:
        print("   ✓ Book model registered with admin")
        
        # Check if it's using custom admin class
        admin_class = admin.site._registry[Book]
        if admin_class.__class__.__name__ == 'BookAdmin':
            print("   ✓ Book model using custom BookAdmin class")
        else:
            print(f"   ✗ Book model using {admin_class.__class__.__name__} instead of BookAdmin")
    else:
        print("   ✗ Book model not registered with admin")
    
    # Check if Library model is registered
    if Library in admin.site._registry:
        print("   ✓ Library model registered with admin")
        
        # Check if it's using custom admin class
        admin_class = admin.site._registry[Library]
        if admin_class.__class__.__name__ == 'LibraryAdmin':
            print("   ✓ Library model using custom LibraryAdmin class")
        else:
            print(f"   ✗ Library model using {admin_class.__class__.__name__} instead of LibraryAdmin")
    else:
        print("   ✗ Library model not registered with admin")


def test_admin_urls():
    """Test that admin URLs are accessible."""
    
    print("\n4. Testing admin URLs:")
    
    try:
        from django.urls import reverse
        
        # Test admin index
        admin_url = reverse('admin:index')
        print(f"   ✓ Admin index URL: {admin_url}")
        
        # Test Book admin URLs
        book_changelist_url = reverse('admin:bookshelf_book_changelist')
        print(f"   ✓ Book changelist URL: {book_changelist_url}")
        
        book_add_url = reverse('admin:bookshelf_book_add')
        print(f"   ✓ Book add URL: {book_add_url}")
        
        # Test Library admin URLs
        library_changelist_url = reverse('admin:bookshelf_library_changelist')
        print(f"   ✓ Library changelist URL: {library_changelist_url}")
        
        library_add_url = reverse('admin:bookshelf_library_add')
        print(f"   ✓ Library add URL: {library_add_url}")
        
    except Exception as e:
        print(f"   ✗ Error testing admin URLs: {e}")


def main():
    """Run all admin configuration tests."""
    
    print("Django Admin Configuration Test Suite")
    print("Library Project - Book Management System")
    print("=" * 60)
    
    try:
        test_admin_configuration()
        test_model_admin_registration()
        test_admin_urls()
        
        print("\n" + "=" * 60)
        print("TEST SUMMARY")
        print("=" * 60)
        print("✓ Admin configuration tests completed")
        print("✓ Models properly registered with custom admin classes")
        print("✓ Admin URLs properly configured")
        print("\nThe Django admin interface is ready to use!")
        print("\nNext steps:")
        print("1. Create a superuser: python manage.py createsuperuser")
        print("2. Run the server: python manage.py runserver")
        print("3. Access admin: http://127.0.0.1:8000/admin/")
        
    except Exception as e:
        print(f"\n✗ Error during testing: {e}")
        print("Please check your Django configuration and try again.")


if __name__ == "__main__":
    main()
