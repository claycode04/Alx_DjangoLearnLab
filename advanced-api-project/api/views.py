
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer



# All views below use Django REST Framework's permission_classes to protect endpoints by user roles.

# BookListView: Lists all books (GET)
class BookListView(generics.ListAPIView):
    """
    List all books. Supports filtering, searching, and ordering.
    Public access. Uses DRF permission_classes for role-based protection.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author']
    ordering = ['title']
    permission_classes = [permissions.AllowAny]

# BookCreateView: Create a new book (POST)
class BookCreateView(generics.CreateAPIView):
    """
    Create a new book. Only authenticated users can create.
    Handles data validation via serializer. Uses DRF permission_classes for role-based protection.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# BookDetailView: Retrieve a book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID. Public access. Uses DRF permission_classes for role-based protection.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# BookUpdateView: Update a book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    """
    Update a book. Only authenticated users can update.
    Handles data validation via serializer. Uses DRF permission_classes for role-based protection.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# BookDeleteView: Delete a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book. Only authenticated users can delete. Uses DRF permission_classes for role-based protection.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Documentation:
# - BookListView: GET /api/books/ (public, supports filtering, searching, ordering)
# - BookCreateView: POST /api/books/create/ (authenticated only)
# - BookDetailView: GET /api/books/<id>/ (public)
# - BookUpdateView: PUT/PATCH /api/books/<id>/update/ (authenticated only)
# - BookDeleteView: DELETE /api/books/<id>/delete/ (authenticated only)
# Filtering: /api/books/?title=BookTitle&author=1&publication_year=2020
# Searching: /api/books/?search=keyword
# Ordering: /api/books/?ordering=title or /api/books/?ordering=-publication_year
