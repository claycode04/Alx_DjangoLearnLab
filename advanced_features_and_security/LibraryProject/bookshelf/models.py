from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    """
    Model representing a book in the library system.
    """
    title = models.CharField(max_length=200, help_text="Enter the book title")
    author = models.CharField(max_length=100, help_text="Enter the author's name")
    publication_year = models.PositiveIntegerField(help_text="Enter the publication year")
    isbn = models.CharField(max_length=13, unique=True, help_text="Enter the 13-character ISBN")
    pages = models.PositiveIntegerField(help_text="Enter the number of pages")
    cover = models.CharField(
        max_length=10,
        choices=[('hard', 'Hardcover'), ('soft', 'Softcover')],
        default='soft',
        help_text="Select cover type"
    )
    language = models.CharField(max_length=50, default='English', help_text="Enter the language")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['title']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('book-detail', args=[str(self.id)])


class Library(models.Model):
    """
    Model representing a library branch.
    """
    name = models.CharField(max_length=100, help_text="Enter the library name")
    location = models.CharField(max_length=200, help_text="Enter the library location")
    books = models.ManyToManyField(Book, blank=True, help_text="Select books in this library")

    class Meta:
        verbose_name_plural = 'Libraries'

    def __str__(self):
        return f"{self.name} - {self.location}"


class Librarian(models.Model):
    """
    Model representing a librarian.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Librarian: {self.user.get_full_name() or self.user.username}"
