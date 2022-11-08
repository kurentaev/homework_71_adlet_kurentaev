from django.views.generic import ListView
from posts.models import Post
from accounts.models import Account


class IndexView(ListView):
    template_name = 'post/index.html'
    model = Post
    ordering = ('-created_at',)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.id is None:
            return context
        else:
            account = Account.objects.get(pk=self.request.user.id).subscriptions.all()
            posts = Post.objects.filter(account__in=account)
            context['posts'] = posts
            return context
