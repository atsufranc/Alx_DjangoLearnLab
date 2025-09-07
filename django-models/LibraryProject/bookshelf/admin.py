from django.contrib import admin
from .models import Book 
# Register your models here.

# Register Book model with custom admin options
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Show these fields in the list view
    list_display = ("title", "author", "publication_year")

    # Add search bar for title and author
    search_fields = ("title", "author")

    # Add filters for publication year
    list_filter = ("publication_year",)
