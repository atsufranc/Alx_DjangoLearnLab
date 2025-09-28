
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# BookListView: Retrieve all books (read-only for unauthenticated users)
class BookListView(generics.ListAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.AllowAny]

# BookDetailView: Retrieve a single book by ID (read-only for unauthenticated users)
class BookDetailView(generics.RetrieveAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.AllowAny]

# BookCreateView: Add a new book (authenticated users only)
class BookCreateView(generics.CreateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# BookUpdateView: Modify an existing book (authenticated users only)
class BookUpdateView(generics.UpdateAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# BookDeleteView: Remove a book (authenticated users only)
class BookDeleteView(generics.DestroyAPIView):
	queryset = Book.objects.all()
	serializer_class = BookSerializer
	permission_classes = [permissions.IsAuthenticated]

# Permissions are enforced using DRF's permission_classes attribute.
# Create, update, and delete operations require authentication, while list and detail views are open for read-only access.
