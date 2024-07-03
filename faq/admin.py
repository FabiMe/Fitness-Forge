from django.contrib import admin

from .models import FAQ


class FAQAdmin(admin.ModelAdmin):
    list_display = ["question", "created_by", "created_at", "updated_at"]
    search_fields = ["question", "answer"]
    list_filter = ["created_at"]


admin.site.register(FAQ, FAQAdmin)
