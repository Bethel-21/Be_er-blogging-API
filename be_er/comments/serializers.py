# comments/serializers.py
from rest_framework import serializers
from .models import Comment
from users.serializers import UserSerializer

class CommentSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=None)

    class Meta:
        model = Comment
        fields = ('id','post','author','content','created_at','updated_at','is_flagged')
        read_only_fields = ('author','created_at','updated_at','is_flagged')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from posts.models import Post
        self.fields['post'].queryset = Post.objects.all()
