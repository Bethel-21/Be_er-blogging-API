from rest_framework import serializers
from .models import Post
from categories.models import Category
from users.models import User

class PostSerializer(serializers.ModelSerializer):
    # PrimaryKeyRelatedField needs a queryset at declaration
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at', 'updated_at', 'is_flagged']

    def create(self, validated_data):
        # Set the author from the request
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['author'] = request.user
        return super().create(validated_data)
