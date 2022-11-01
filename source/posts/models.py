from django.contrib.auth import get_user_model
from django.db import models
from posts.managers import PostProjectManager


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )

    class Meta:
        abstract = True


class Post(BaseModel):
    description = models.CharField(
        verbose_name='Description',
        null=False,
        blank=False,
        max_length=200
    )
    image = models.ImageField(
        verbose_name='Image',
        null=False,
        blank=False,
        upload_to='posts'
    )
    account = models.ForeignKey(
        verbose_name='Author',
        to=get_user_model(),
        related_name='posts',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    liked_posts = models.ManyToManyField(
        verbose_name='Liked posts',
        to=get_user_model(),
        related_name='user_likes'
    )

    objects = PostProjectManager()

    def __str__(self):
        return f"{self.account}"

    class Meta:
        db_table = "post"
        verbose_name = "Post"
        verbose_name_plural = "Post"


class Comment(BaseModel):
    account = models.ForeignKey(
        verbose_name='Author',
        to=get_user_model(),
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        verbose_name='Post',
        to='posts.Post',
        related_name='comments',
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )
    text = models.CharField(
        verbose_name='Text',
        null=False,
        blank=False,
        max_length=200
    )

    objects = PostProjectManager()

    def __str__(self):
        return f"{self.account}"

    class Meta:
        db_table = "comment"
        verbose_name = "Comment"
        verbose_name_plural = "Comments"
