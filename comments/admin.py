from django.contrib import admin
from .models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'content', 'rating', 'created_at')
    list_filter = ('created_at', 'user', 'product', 'rating')
    search_fields = ('content', 'user__username', 'product__name')
    actions = ['delete_selected']

    def delete_selected(self, request, queryset):
        # Custom delete logic, if needed
        queryset.delete()
        self.message_user(
            request, "Selected comment(s) have been deleted successfully."
        )
    delete_selected.short_description = "Delete selected comments"

    # Optional: If you want to show a read-only page detail
    readonly_fields = ('created_at', 'user', 'product')

    # Optional: To customize the form view in the admin
    fieldsets = (
        (None, {
            'fields': ('user', 'product', 'content', 'rating')
        }),
        ('Date Information', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # This will make the section collapsible
        }),
    )


# Register the admin class with the associated model
admin.site.register(Comment, CommentAdmin)
