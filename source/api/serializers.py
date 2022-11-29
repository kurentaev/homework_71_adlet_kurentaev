from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'description', 'image', 'account', 'liked_posts', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']


class LikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'image', 'liked_posts']
        read_only_fields = ['id']
