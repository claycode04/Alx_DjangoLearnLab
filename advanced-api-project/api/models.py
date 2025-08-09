
from django.db import models

# Author model represents a book author with a name field.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model represents a book with title, publication year, and a foreign key to Author.
# The foreign key establishes a one-to-many relationship: one Author can have many Books.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
