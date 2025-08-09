from django.urls import path
from . import views

# URL patterns for Book CRUD operations using generic views.
# /books/ - List all books (GET), Create book (POST, auth required)
# /books/<int:pk>/ - Retrieve (GET), Update (PUT/PATCH, auth required), Delete (DELETE, auth required)
urlpatterns = [
    path('books/', views.BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
]
