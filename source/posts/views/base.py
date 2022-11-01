from django.views.generic import ListView
from posts.models import Post


class IndexView(ListView):
    template_name = 'post/index.html'
    model = Post
    context_object_name = 'posts'
    ordering = ('-created_at',)
