from django.contrib import admin
from .models import Comment

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'author', 'is_flagged', 'created_at')
    list_filter = ('is_flagged',)
    search_fields = ('content',)
