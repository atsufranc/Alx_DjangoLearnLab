from django.urls import path
from .views import BookList, BookViewSet # Import the BookList view
from rest_framework.routers import DefaultRouter    

router = DefaultRouter()
router.register(r'', BookViewSet, basename='book_all')

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),  # Maps to the BookList view
]
urlpatterns += router.urls