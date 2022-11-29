from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from posts.models import Post
from api.serializers import PostSerializer, LikesSerializer
from api.permissions import PermissionPolicyMixin, IsWriteUser


class PostViewSet(PermissionPolicyMixin, viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    permission_classes_per_method = {
        "create": [IsAuthenticated, IsWriteUser],
        "destroy": [IsAuthenticated, IsWriteUser],
        "update": [IsAuthenticated, IsWriteUser],
        "partial_update": [IsAuthenticated, IsWriteUser]
    }
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = LikesSerializer

    def post(self, request, *args, **kwargs):
        post = get_object_or_404(Post, pk=kwargs.get('pk'))
        if post.liked_posts.filter(pk=request.user.id).exists():
            post.liked_posts.remove(request.user)
            return JsonResponse({'answer': 'delete'})
        else:
            post.liked_posts.add(request.user)
            return JsonResponse({'answer': 'add'})
