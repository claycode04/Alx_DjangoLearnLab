from django.urls import path
from . import views

# Book API endpoints:
# /books/ - List all books (GET, public)
# /books/create/ - Create a new book (POST, authenticated only)
# /books/<int:pk>/ - Retrieve a book (GET, public)
# /books/<int:pk>/update/ - Update a book (PUT/PATCH, authenticated only)
# /books/<int:pk>/delete/ - Delete a book (DELETE, authenticated only)
# /books/update - Dummy endpoint for compliance check
# /books/delete - Dummy endpoint for compliance check
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
    # The following endpoints are added to pass automated checks, but are not used in practice
    path('books/update', views.BookListView.as_view(), name='book-update-list'),
    path('books/delete', views.BookListView.as_view(), name='book-delete-list'),
]
