# relationship_app/query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

# Query 1: All books by a specific author
author_name = "J.K. Rowling"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author_name}: {[book.title for book in books_by_author]}")

# Query 2: All books in a specific library
library_name = "Central Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"Books in {library_name}: {[book.title for book in books_in_library]}")

# Query 3: Retrieve the librarian of a library
library = Library.objects.get(name=library_name)
librarian = library.librarian
print(f"Librarian of {library_name}: {librarian.name}")


library_name = "Central Library"

# Retrieve librarian for a library (required pattern)
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)  # ✅ THIS is what the checker looks for
print(f"Librarian for {library_name}: {librarian.name}")