from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "status", "created_on")
    list_filter = ("status", "created_on")
    search_fields = ("name", "slug")
