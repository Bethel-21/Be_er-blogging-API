from django.contrib import admin
from .models import Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')  # shows these fields in the admin list view
    search_fields = ('name',)              # lets you search by name in the admin
