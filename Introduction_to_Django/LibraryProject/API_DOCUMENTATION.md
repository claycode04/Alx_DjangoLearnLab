# Django Library Project - API Documentation

## Overview
This document outlines the REST API endpoints for the Django Library Management System.

## Authentication
All API endpoints require authentication using Django's session authentication or token-based authentication.

### Authentication Headers
```
Authorization: Token your-api-token-here
```

## Base URL
```
http://localhost:8000/api/
```

## Endpoints

### Books

#### List Books
```http
GET /api/books/
```

**Response:**
```json
{
    "count": 25,
    "next": "http://localhost:8000/api/books/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "title": "Django for Beginners",
            "author": "William Vincent",
            "isbn": "978-1735467207",
            "publication_date": "2022-01-01",
            "available": true,
            "category": "Programming",
            "created_at": "2025-01-01T10:00:00Z"
        }
    ]
}
```

#### Create Book
```http
POST /api/books/
Content-Type: application/json

{
    "title": "Advanced Django",
    "author": "John Doe",
    "isbn": "978-1234567890",
    "publication_date": "2025-01-01",
    "category": "Programming"
}
```

#### Get Book Details
```http
GET /api/books/{id}/
```

#### Update Book
```http
PUT /api/books/{id}/
Content-Type: application/json

{
    "title": "Updated Title",
    "author": "Updated Author",
    "isbn": "978-0987654321",
    "publication_date": "2025-01-01",
    "category": "Programming"
}
```

#### Delete Book
```http
DELETE /api/books/{id}/
```

### Users

#### User Profile
```http
GET /api/users/profile/
```

#### Update Profile
```http
PUT /api/users/profile/
Content-Type: application/json

{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john@example.com"
}
```

### Borrowing

#### Borrow Book
```http
POST /api/borrowing/
Content-Type: application/json

{
    "book_id": 1,
    "due_date": "2025-02-01"
}
```

#### Return Book
```http
POST /api/borrowing/{id}/return/
```

#### User's Borrowed Books
```http
GET /api/borrowing/my-books/
```

## Error Responses

### 400 Bad Request
```json
{
    "error": "Invalid data provided",
    "details": {
        "title": ["This field is required."]
    }
}
```

### 401 Unauthorized
```json
{
    "error": "Authentication credentials were not provided."
}
```

### 404 Not Found
```json
{
    "error": "Book not found"
}
```

### 500 Internal Server Error
```json
{
    "error": "Internal server error occurred"
}
```

## Rate Limiting
- Anonymous users: 100 requests/hour
- Authenticated users: 1000 requests/hour

## Pagination
All list endpoints support pagination with the following parameters:
- `page`: Page number (default: 1)
- `page_size`: Items per page (default: 20, max: 100)

## Filtering and Search
Books can be filtered using query parameters:
- `title`: Filter by title (case-insensitive)
- `author`: Filter by author (case-insensitive)
- `category`: Filter by category
- `available`: Filter by availability (true/false)
- `search`: Full-text search across title and author

Example:
```http
GET /api/books/?search=django&category=Programming&available=true
```

## Ordering
Results can be ordered using the `ordering` parameter:
- `title`: Order by title
- `-title`: Order by title (descending)
- `publication_date`: Order by publication date
- `-publication_date`: Order by publication date (descending)

Example:
```http
GET /api/books/?ordering=-publication_date
```
