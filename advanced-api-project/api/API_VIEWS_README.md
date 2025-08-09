# API Views Documentation for advanced_api_project

This document describes the configuration and behavior of the Book API views in the `api` app.

## Endpoints

- `GET /api/books/` — List all books (public)
- `POST /api/books/` — Create a new book (authenticated users only)
- `GET /api/books/<id>/` — Retrieve a book by ID (public)
- `PUT/PATCH /api/books/<id>/` — Update a book (authenticated users only)
- `DELETE /api/books/<id>/` — Delete a book (authenticated users only)

## View Classes

- **BookListView**: Handles listing and creation of books. Uses DRF's `ListCreateAPIView`.
  - Permissions: Anyone can list, only authenticated users can create.
- **BookDetailView**: Handles retrieve, update, and delete for a single book. Uses DRF's `RetrieveUpdateDestroyAPIView`.
  - Permissions: Anyone can retrieve, only authenticated users can update or delete.

## Permissions

- Read-only access (GET) is allowed for all users.
- Write access (POST, PUT, PATCH, DELETE) is restricted to authenticated users.
- Permissions are enforced using custom `get_permissions` methods in each view.

## Customization

- Views use DRF generic views for efficient CRUD handling.
- Custom permission logic is implemented in `get_permissions`.
- Book creation and update use the serializer's validation (including custom year validation).

## How to Test

- Use Postman, curl, or the Django admin to test endpoints.
- Unauthenticated users can only GET.
- Authenticated users can POST, PUT, PATCH, DELETE.

---

For more details, see the code comments in `api/views.py` and `api/urls.py`.
