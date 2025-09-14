from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, UserProfile, Author, Book, Library, Librarian

class CustomUserAdmin(BaseUserAdmin):
	model = CustomUser
	list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'date_of_birth')
	list_filter = ('is_staff', 'is_active', 'date_of_birth')
	search_fields = ('email', 'first_name', 'last_name')
	ordering = ('email',)
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'date_of_birth', 'profile_photo', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
	)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(UserProfile)
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)
