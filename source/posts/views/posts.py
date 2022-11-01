from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import DetailView, CreateView
from posts.forms import PostForm
from posts.models import Post


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostCreate(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'post/post_create.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)


class PostView(DetailView, LoginRequiredMixin):
    template_name = 'post/post.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        return context
