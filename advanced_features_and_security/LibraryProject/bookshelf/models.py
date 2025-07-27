from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, User
from django.urls import reverse

# Custom user model and manager for bookshelf app
class CustomUserManager(BaseUserManager):
    def create_user(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        if not username:
            raise ValueError('The Username must be set')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, date_of_birth=date_of_birth, profile_photo=profile_photo, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email=None, password=None, date_of_birth=None, profile_photo=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, email, password, date_of_birth, profile_photo, **extra_fields)

class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True, blank=True)
    profile_photo = models.ImageField(upload_to='profile_photos/', null=True, blank=True)

    objects = CustomUserManager()

    def __str__(self):
        return self.username

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
        permissions = [
            ("can_view", "Can view book"),
            ("can_create", "Can create book"),
            ("can_edit", "Can edit book"),
            ("can_delete", "Can delete book"),
        ]
        # Documentation:
        # Custom permissions are defined for Book: can_view, can_create, can_edit, can_delete.
        # These permissions can be assigned to groups (Editors, Viewers, Admins) via Django admin.
        # Use @permission_required('bookshelf.can_edit', raise_exception=True) in views to enforce access control.

    def __str__(self):
        return f"{self.title} by {self.author}"

    def get_absolute_url(self):
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
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    library = models.ForeignKey(Library, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Librarian: {self.user.get_full_name() or self.user.username}"
