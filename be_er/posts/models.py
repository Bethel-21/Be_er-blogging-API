from django.db import models
from django.contrib.auth.models import User
from categories.models import Category

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=200)
    content = models.TextField()
    featured_image = models.ImageField(upload_to="featured_images/", null=True, blank=True)
    gallery = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models .DateTimeField(auto_now=True)

    def __str__(self):
        return self.title