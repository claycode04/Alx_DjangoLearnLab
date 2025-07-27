from django.shortcuts import render
from django.contrib.auth.decorators import permission_required
from .models import Book

# Permissions & Groups Documentation:
# - Permissions enforced in views using @permission_required for Book actions:
#     - can_view: book_list
#     - can_create: add_book
#     - can_edit: edit_book
#     - can_delete: delete_book
# - Assign users to groups (Editors, Viewers, Admins) in Django admin and grant relevant permissions.

@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

@permission_required('bookshelf.can_create', raise_exception=True)
def add_book(request):
    # Implementation for adding a book
    pass

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, pk):
    # Implementation for editing a book
    pass

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, pk):
    # Implementation for deleting a book
    pass
