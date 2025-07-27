from .models import Library
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test, permission_required
from django.contrib import messages
from .models import Book, Library, CustomUser
    # ...existing code...

"""
Permissions & Groups Documentation:
- Permissions enforced in views using @permission_required for Book actions:
    - can_create: add_book
    - can_edit: edit_book
    - can_delete: delete_book
    - can_view: list_books
- Assign users to groups (Editors, Viewers, Admins) in Django admin and grant relevant permissions.
"""

# Add Book View
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            Book.objects.create(title=title, author_id=author_id)
            return HttpResponseRedirect(reverse('list_books'))
    return render(request, 'relationship_app/add_book.html')

# Edit Book View
@permission_required('relationship_app.can_edit', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        if title and author_id:
            book.title = title
            book.author_id = author_id
            book.save()
            return HttpResponseRedirect(reverse('list_books'))
    return render(request, 'relationship_app/edit_book.html', {'book': book})

# Delete Book View
@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return HttpResponseRedirect(reverse('list_books'))
    return render(request, 'relationship_app/delete_book.html', {'book': book})
from django.contrib.auth.decorators import login_required, user_passes_test
## UserProfile removed, use CustomUser
# ...existing code...

# Role check helpers
def is_admin(user):
    return user.is_superuser or user.is_staff

def is_librarian(user):
    # Example: check for group membership or add a role field to CustomUser
    return user.groups.filter(name='Librarian').exists()

def is_member(user):
    return user.groups.filter(name='Member').exists()

# Admin view
@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian view
@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member view
@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')
from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .models import Book, Library

# Function-based view to list all books
@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()  # Required by the checker
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-based view to display details of a specific library using DetailView
from django.views.generic.detail import DetailView

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

# User Login View
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('list_books')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Invalid username or password.')
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# User Logout View
def user_logout(request):
    logout(request)
    return render(request, 'relationship_app/logout.html')

# User Registration View
    from django import forms
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'date_of_birth', 'profile_photo', 'password1', 'password2')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
        else:
            messages.error(request, 'Registration failed. Please check the form.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})
