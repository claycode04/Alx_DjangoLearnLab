
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer

# BookListView: Lists all books (GET) and allows creation (POST) for authenticated users.
class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']  # Filtering by these fields
    search_fields = ['title', 'author__name']  # Search by book title or author name
    ordering_fields = ['title', 'publication_year', 'author']  # Allow ordering by these fields
    ordering = ['title']  # Default ordering

    # Allow anyone to view, but only authenticated users can create
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    # Documentation:
    # - Filtering: /api/books/?title=BookTitle&author=1&publication_year=2020
    # - Searching: /api/books/?search=keyword (searches title and author name)
    # - Ordering: /api/books/?ordering=title or /api/books/?ordering=-publication_year
    # Multiple filters/search/orderings can be combined in a single request.

# BookDetailView: Retrieve, update, or delete a book by ID.
class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    # Allow anyone to view, but only authenticated users can update/delete
    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

# Documentation:
# - BookListView handles GET (list all books) and POST (create book) requests.
#   - POST is restricted to authenticated users.
# - BookDetailView handles GET (retrieve), PUT/PATCH (update), and DELETE requests for a single book.
#   - Update and delete are restricted to authenticated users.
# - Custom get_permissions methods enforce these rules.
