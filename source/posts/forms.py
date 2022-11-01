from django import forms
from posts.models import Post, Comment


class PostForm(forms.ModelForm):
    description = forms.CharField(required=True)

    class Meta:
        model = Post
        exclude = ('account', 'liked_posts')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ('account', 'post')


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label='Find')


