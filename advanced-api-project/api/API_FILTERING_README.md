# Filtering, Searching, and Ordering in Book API

The Book API supports advanced query capabilities using Django REST Framework and django-filter.

## Filtering
- Filter by title, author, or publication_year:
  - `/api/books/?title=SomeTitle`
  - `/api/books/?author=1` (author is the ID)
  - `/api/books/?publication_year=2020`
- Combine filters: `/api/books/?title=SomeTitle&publication_year=2020`

## Searching
- Search by book title or author name:
  - `/api/books/?search=keyword`

## Ordering
- Order by title, publication_year, or author:
  - `/api/books/?ordering=title`
  - `/api/books/?ordering=-publication_year` (descending)
- Multiple ordering fields: `/api/books/?ordering=author,title`

## Implementation
- `BookListView` uses DRF's `DjangoFilterBackend`, `SearchFilter`, and `OrderingFilter`.
- See `api/views.py` for configuration and code comments.
- `django_filters` is added to `INSTALLED_APPS` and DRF's `DEFAULT_FILTER_BACKENDS` is set in `settings.py`.

---

Test these features using Postman, curl, or your browser.
