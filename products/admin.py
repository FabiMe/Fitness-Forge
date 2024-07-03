from django.contrib import admin
from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "name",
        "category",
        "price",
        "is_mystery_box",
        "rating",
        "image",
    )
    list_filter = (
        "is_mystery_box",
        "category",
    )
    search_fields = ("name", "description", "sku")
    # Allow direct editing of these fields
    list_editable = ("is_mystery_box", "price", "rating")
    ordering = ("sku",)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "friendly_name",
        "name",
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
