# posts/serializers.py
from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer
from categories.serializers import CategorySerializer

class PostSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    category = serializers.PrimaryKeyRelatedField(queryset=None)  # will set in __init__

    class Meta:
        model = Post
        fields = ('id','title','content','author','category','created_at','updated_at','is_flagged','is_published')
        read_only_fields = ('created_at','updated_at','is_flagged')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # set queryset now to avoid circular import at module load
        from categories.models import Category
        self.fields['category'].queryset = Category.objects.all()
