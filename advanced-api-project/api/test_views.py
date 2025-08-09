from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITestCase(APITestCase):
    """
    Unit tests for Book API endpoints, including CRUD, filtering, searching, ordering, and permissions.
    """
    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpass')
        # Create authors
        self.author1 = Author.objects.create(name='Author One')
        self.author2 = Author.objects.create(name='Author Two')
        # Create books
        self.book1 = Book.objects.create(title='Alpha', publication_year=2020, author=self.author1)
        self.book2 = Book.objects.create(title='Beta', publication_year=2021, author=self.author2)
        self.book3 = Book.objects.create(title='Gamma', publication_year=2020, author=self.author1)

    def test_list_books(self):
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Alpha')

    def test_create_book_requires_auth(self):
        url = reverse('book-list')
        data = {'title': 'Delta', 'publication_year': 2022, 'author': self.author1.id}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        # Now authenticate
        self.client.login(username='testuser', password='testpass')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_update_book_requires_auth(self):
        url = reverse('book-detail', args=[self.book1.id])
        data = {'title': 'Alpha Updated', 'publication_year': 2020, 'author': self.author1.id}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username='testuser', password='testpass')
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Alpha Updated')

    def test_delete_book_requires_auth(self):
        url = reverse('book-detail', args=[self.book1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.client.login(username='testuser', password='testpass')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_title(self):
        url = reverse('book-list') + '?title=Alpha'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Alpha')

    def test_filter_books_by_author(self):
        url = reverse('book-list') + f'?author={self.author1.id}'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 2)

    def test_search_books(self):
        url = reverse('book-list') + '?search=Beta'
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Beta')

    def test_order_books_by_title(self):
        url = reverse('book-list') + '?ordering=title'
        response = self.client.get(url)
        titles = [book['title'] for book in response.data]
        self.assertEqual(titles, sorted(titles))

    def test_order_books_by_publication_year_desc(self):
        url = reverse('book-list') + '?ordering=-publication_year'
        response = self.client.get(url)
        years = [book['publication_year'] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))

# To run these tests:
# python manage.py test api
#
# These tests cover CRUD, filtering, searching, ordering, and permissions for the Book API.
# See code comments for details on each test scenario.
