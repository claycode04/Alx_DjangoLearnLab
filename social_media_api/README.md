# Social Media API

This project is a Django REST Framework (DRF) powered API for a social media platform. It includes user authentication, user profiles, and is ready for further features like posts, comments, follows, notifications, and likes.

## Setup Instructions

### 1. Install Dependencies

```
pip install django djangorestframework djangorestframework-simplejwt
```

### 2. Project Structure

- `social_media_api/` (Django project root)
- `accounts/` (Django app for user management)

### 3. Initial Setup

```
django-admin startproject social_media_api
cd social_media_api
python manage.py startapp accounts
```

### 4. Add to `INSTALLED_APPS` in `settings.py`:

```
'rest_framework',
'rest_framework.authtoken',
'accounts',
```

### 5. Custom User Model

- The custom user model extends `AbstractUser` and adds:
  - `bio` (TextField)
  - `profile_picture` (ImageField, optional)
  - `followers` (ManyToManyField to self, symmetrical=False)

### 6. Authentication

- Uses DRF's Token Authentication.
- Endpoints:
  - `/api/accounts/register/` — Register a new user (returns token)
  - `/api/accounts/login/` — Login (returns token)
  - `/api/accounts/profile/` — Get/update user profile (requires authentication)

### 7. Migrations & Run Server

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 8. Testing

- Use Postman or similar tools to test registration and login endpoints.
- Tokens are returned on successful registration/login.

## User Model Overview

- Username, email, password (standard fields)
- Bio: Short user bio
- Profile picture: Optional image
- Followers: Many-to-many relationship with other users

## Next Steps

- Implement posts, comments, follows, notifications, and likes.
- Add deployment configuration for production.

---

For more details, see the code in the `accounts` app and the project settings.
