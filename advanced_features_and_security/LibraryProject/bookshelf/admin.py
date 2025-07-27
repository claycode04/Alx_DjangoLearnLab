from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Book, Library, CustomUser


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Book model.
    Customizes the display and functionality of Book management in Django admin.
    """
    # Display fields in the admin list view
    list_display = ('title', 'author', 'publication_year', 'isbn', 'pages', 'cover', 'language')
    
    # Add filters in the right sidebar
    list_filter = ('publication_year', 'cover', 'language', 'created_at')
    
    # Enable search functionality
    search_fields = ('title', 'author', 'isbn')
    
    # Add pagination (show 20 books per page)
    list_per_page = 20
    
    # Fields to display in the detail view
    fields = ('title', 'author', 'publication_year', 'isbn', 'pages', 'cover', 'language')
    
    # Read-only fields (timestamps)
    readonly_fields = ('created_at', 'updated_at')
    
    # Organize fields in fieldsets for better structure
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'publication_year')
        }),
        ('Publication Details', {
            'fields': ('isbn', 'pages', 'cover', 'language')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Collapsible section
        }),
    )
    
    # Enable bulk actions
    actions = ['mark_as_hardcover', 'mark_as_softcover']
    
    def mark_as_hardcover(self, request, queryset):
        """Bulk action to mark selected books as hardcover."""
        updated = queryset.update(cover='hard')
        self.message_user(request, f'{updated} books marked as hardcover.')
    mark_as_hardcover.short_description = "Mark selected books as hardcover"
    
    def mark_as_softcover(self, request, queryset):
        """Bulk action to mark selected books as softcover."""
        updated = queryset.update(cover='soft')
        self.message_user(request, f'{updated} books marked as softcover.')
    mark_as_softcover.short_description = "Mark selected books as softcover"


@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the Library model.
    """
    list_display = ('name', 'location', 'book_count')
    search_fields = ('name', 'location')
    filter_horizontal = ('books',)  # Better interface for many-to-many relationships
    
    def book_count(self, obj):
        """Display the number of books in each library."""
        return obj.books.count()
    book_count.short_description = 'Number of Books'


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    list_display = ['username', 'email', 'date_of_birth', 'is_staff', 'is_superuser']
    search_fields = ['username', 'email']

admin.site.register(CustomUser, CustomUserAdmin)
