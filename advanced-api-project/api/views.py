
from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer


# BookListView: Lists all books (GET)
class BookListView(generics.ListAPIView):
    """
    List all books. Supports filtering, searching, and ordering.
    Public access.
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
    Handles data validation via serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# BookDetailView: Retrieve a book by ID (GET)
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieve a single book by ID. Public access.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]

# BookUpdateView: Update a book (PUT/PATCH)
class BookUpdateView(generics.UpdateAPIView):
    """
    Update a book. Only authenticated users can update.
    Handles data validation via serializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

# BookDeleteView: Delete a book (DELETE)
class BookDeleteView(generics.DestroyAPIView):
    """
    Delete a book. Only authenticated users can delete.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]

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
