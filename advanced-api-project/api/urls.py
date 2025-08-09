from django.urls import path
from . import views

# Book API endpoints:
# /books/ - List all books (GET)
# /books/create/ - Create a new book (POST, auth required)
# /books/<int:pk>/ - Retrieve a book (GET)
# /books/<int:pk>/update/ - Update a book (PUT/PATCH, auth required)
# /books/<int:pk>/delete/ - Delete a book (DELETE, auth required)
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/create/', views.BookCreateView.as_view(), name='book-create'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('books/<int:pk>/update/', views.BookUpdateView.as_view(), name='book-update'),
    path('books/<int:pk>/delete/', views.BookDeleteView.as_view(), name='book-delete'),
]
