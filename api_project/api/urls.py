from django.urls import path, include
from .views import BookList, BookViewSet # Import the BookList view
from rest_framework.routers import DefaultRouter    

router = DefaultRouter()
router.register(r'book_all', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
    path('', include(router.urls)),  # Include the router URLs
]
