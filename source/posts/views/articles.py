from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, FormView

from posts.forms import PostForm, FavoriteForm
from posts.models import Post


class SuccessDetailUrlMixin:
    def get_success_url(self):
        return reverse('post_detail', kwargs={'pk': self.object.pk})


class PostCreate(SuccessDetailUrlMixin, LoginRequiredMixin, CreateView):
    template_name = 'post_create.html'
    form_class = PostForm
    model = Post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    #
    # def post(self, request, *args, **kwargs):
    #     form = self.get_form_class()(request.POST)
    #     if form.is_valid():
    #         description = form.cleaned_data.get('description')
    #         image = form.cleaned_data.get('image')
    #         user = request.user
    #         Post.objects.create(user=user, image=image, description=description)
    #     return redirect('index')


class PostView(DetailView):
    template_name = 'post.html'
    model = Post


# class CustomUserPassesTestMixin(UserPassesTestMixin):
#     groups = []
#
#     def test_func(self):
#         return self.request.user.groups.filter(name__in=self.groups).exists()
#
#
# class ArticleUpdateView(CustomUserPassesTestMixin, LoginRequiredMixin, UpdateView):
#     template_name = 'article_update.html'
#     form_class = ArticleForm
#     model = Article
#     context_object_name = 'article'
#     groups = ['user', 'admin']
#     # permission_required = 'webapp.change_article'
#
#     # def test_func(self):
#     #     return self.request.user.groups.filter(name__in=['admin', 'user']).exists()
#     #
#     # def dispatch(self, request, *args, **kwargs):
#     #     if request.user.groups.filter(name__in=['admin', 'user']).exists():
#     #         raise PermissionDenied
#     #     return super(ArticleUpdateView, self).dispatch(request, *args, **kwargs)
#
#     def get_success_url(self):
#         return reverse('article_detail', kwargs={'pk': self.object.pk})
#
#
# class ArticleDeleteView(LoginRequiredMixin, DeleteView):
#     template_name = 'article_confirm_delete.html'
#     model = Article
#     success_url = reverse_lazy('index')
#
#
# class FavoriteView(LoginRequiredMixin, FormView):
#     form_class = FavoriteForm
#
#     def post(self, request, *args, **kwargs):
#         article = get_object_or_404(Article, pk=kwargs.get('pk'))
#         form = self.get_form_class()(request.POST)
#         if form.is_valid():
#             note = form.cleaned_data.get('note')
#             user = request.user
#             if not Favorite.objects.filter(user=user, article=article).exists():
#                 Favorite.objects.create(user=user, article=article, note=note)
#         return redirect('index')
