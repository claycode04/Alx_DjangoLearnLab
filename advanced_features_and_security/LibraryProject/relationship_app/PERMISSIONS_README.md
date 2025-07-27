# Permissions & Groups Setup Guide for advanced_features_and_security

## Custom Permissions
- Defined in `Book` model (`models.py`):
    - can_view: Can view book
    - can_create: Can create book
    - can_edit: Can edit book
    - can_delete: Can delete book

## Groups
- Create groups in Django admin:
    - Editors: Assign can_create, can_edit
    - Viewers: Assign can_view
    - Admins: Assign all permissions

## Enforcing Permissions
- Views use `@permission_required` decorators (see `views.py`):
    - Only users with the required permission can access each view.

## How to Test
1. Create test users in Django admin.
2. Assign users to groups.
3. Log in as each user and verify access to add, edit, delete, and view book actions.

## Notes
- Permissions and groups can be managed via Django admin.
- See comments in `models.py` and `views.py` for more details.
