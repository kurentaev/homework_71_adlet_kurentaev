from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, SAFE_METHODS
from posts.models import Post
from api.serializers import PostSerializer, LikesSerializer
from rest_framework.views import APIView


class PostViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_permissions(self):
        if self.request.method in SAFE_METHODS:
            return []
        return super().get_permissions()


class LikeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = LikesSerializer


class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    model = Post

    def post(self, request, *args, **kwargs):
        post_pk = kwargs.get('pk')
        post = get_object_or_404(Post, pk=post_pk)
        if post.liked_posts.filter(pk=request.user.id).exists():
            post.liked_posts.remove(request.user)
            return JsonResponse({'answer': 'delete'})
        else:
            post.liked_posts.add(request.user)
            return JsonResponse({'answer': 'add'})
