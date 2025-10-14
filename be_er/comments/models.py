# comments/models.py
from django.db import models
from core.models import TimeStampedModel
from django.conf import settings
from posts.models import Post

class Comment(TimeStampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name='comments')
    content = models.TextField()
    is_flagged = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
