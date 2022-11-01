from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import CreateView
from posts.models import Post, Comment
from posts.forms import CommentForm
from accounts.models import Account


def post_like(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.liked_posts.filter(id=request.user.id).exists():
        post.liked_posts.remove(request.user)
    else:
        post.liked_posts.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))


def subscribe(request, pk):
    account = get_object_or_404(Account, id=request.POST.get('user_id'))
    if account == request.user:
        pass
    elif account.subscriptions.filter(id=request.user.id).exists():
        account.subscriptions.remove(request.user)
    else:
        account.subscriptions.add(request.user)
    return HttpResponseRedirect(reverse('profile', args=[str(pk)]))


class CommentAddView(LoginRequiredMixin, CreateView):
    template_name = 'comment/comment_create.html'
    form_class = CommentForm
    model = Comment

    def form_valid(self, form):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.account = self.request.user
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        form.save_m2m()
        return redirect('post_detail', pk=post.pk)
