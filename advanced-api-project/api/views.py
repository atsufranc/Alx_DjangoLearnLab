from django_filters import rest_framework

from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework
from django_filters import rest_framework
from .models import Book
from .serializers import BookSerializer

# BookListView: Retrieve all books (read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]
	# Enable filtering, searching, and ordering for Book model
	from django_filters.rest_framework import DjangoFilterBackend
	from rest_framework.filters import SearchFilter, OrderingFilter
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['title', 'author', 'publication_year']
	search_fields = ['title', 'author__name']
	ordering_fields = ['title', 'publication_year']
	ordering = ['title']  # Default ordering

	# Documentation:
	# - filterset_fields allows filtering by title, author, and publication_year.
	# - search_fields enables text search on title and author's name.
	# - ordering_fields allows ordering by title and publication_year.
	# - These features are accessible via query parameters in API requests.

# BookDetailView: Retrieve a single book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

# BookCreateView: Add a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

# BookUpdateView: Modify an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

# BookDeleteView: Remove a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [IsAuthenticated]

# Permissions are enforced using DRF's permission_classes attribute.
# Create, update, and delete operations require authentication, while list and detail views are open for read-only access.
