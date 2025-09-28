
# API Views Documentation

# BookListView: Handles GET requests to retrieve all books. Open to unauthenticated users (read-only).
#   - Supports filtering by title, author, and publication_year using query parameters (e.g., ?title=...&author=...&publication_year=...).
#   - Supports searching by title and author name using ?search=...
#   - Supports ordering by title and publication_year using ?ordering=title or ?ordering=publication_year
# BookDetailView: Handles GET requests to retrieve a single book by ID. Open to unauthenticated users (read-only).
# BookCreateView: Handles POST requests to create a new book. Restricted to authenticated users.
# BookUpdateView: Handles PUT/PATCH requests to update an existing book. Restricted to authenticated users.
# BookDeleteView: Handles DELETE requests to remove a book. Restricted to authenticated users.

# Permissions are enforced using DRF's permission_classes attribute in each view.
# URL patterns for these views are defined in api/urls.py and included in the main project urls.py.
# For more details, see comments in api/views.py and api/urls.py.
