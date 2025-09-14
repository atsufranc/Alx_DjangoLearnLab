# Permissions and Groups Setup for Bookshelf App

## Custom Permissions
- The `Book` model defines the following custom permissions in its `Meta` class:
  - `can_view`: Can view book
  - `can_create`: Can create book
  - `can_edit`: Can edit book
  - `can_delete`: Can delete book

## Groups
- Create groups in the Django admin (e.g., Editors, Viewers, Admins).
- Assign the above permissions to these groups as needed:
  - **Editors**: can_create, can_edit, can_view
  - **Viewers**: can_view
  - **Admins**: can_create, can_edit, can_delete, can_view

## Enforcing Permissions in Views
- The following views in `bookshelf/views.py` are protected with permission checks:
  - `book_list`: Requires `can_view`
  - `book_create`: Requires `can_create`
  - `book_edit`: Requires `can_edit`
  - `book_delete`: Requires `can_delete`
- These use the `@permission_required` decorator with `raise_exception=True`.

## Testing
- Assign users to groups via the Django admin.
- Log in as different users and verify access to book list, create, edit, and delete views.

## Notes
- Permissions and groups can be managed via the Django admin interface under the Auth section.
- You can further customize permissions and group assignments as your application grows.
