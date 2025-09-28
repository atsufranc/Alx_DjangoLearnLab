from django.urls import path
from .views import BookListView, BookDetailView, BookCreateView, BookUpdateView, BookDeleteView


urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('books/create/', BookCreateView.as_view(), name='book-create'),
        path('books/update/<int:pk>/', BookUpdateView.as_view(), name='book-update'),
        path('books/delete/<int:pk>/', BookDeleteView.as_view(), name='book-delete'),
]

# Each endpoint is mapped to a specific view for CRUD operations.
# Permissions are enforced in the views to restrict access as required.
