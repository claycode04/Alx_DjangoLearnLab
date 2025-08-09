# API Testing Documentation

This document describes the testing strategy and test cases for the Book API endpoints in `test_views.py`.

## How to Run Tests

- Run all tests for the API app:
  ```bash
  python manage.py test api
  ```
- Tests use Django's built-in test framework and a separate test database.

## What is Tested

- **CRUD Operations:**
  - List all books
  - Retrieve a single book
  - Create, update, and delete a book (with and without authentication)
- **Filtering:**
  - Filter books by title and author
- **Searching:**
  - Search books by title or author name
- **Ordering:**
  - Order books by title and publication year
- **Permissions:**
  - Ensure only authenticated users can create, update, or delete books

## Test Structure

- Each test simulates an API request and checks the response status code and data.
- Authentication is tested by logging in and out as needed.
- The test database is reset for each test run, so tests are isolated and repeatable.

---

See `api/test_views.py` for detailed test code and comments.
