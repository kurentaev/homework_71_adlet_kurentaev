from django.urls import path
from posts.views.base import IndexView
from posts.views.posts import PostView, PostCreate
from posts.views.comments import CommentAddView, post_like, subscribe


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('instasram/', IndexView.as_view(), name='home'),
    path('instasram/post/<int:pk>', PostView.as_view(), name='post_detail'),
    path('instasram/post/add/', PostCreate.as_view(), name='post_add'),
    path('instasram/post/comment/add/<int:pk>', CommentAddView.as_view(), name='comment_add'),
    path('instasram/post/like/<int:pk>', post_like, name='post_like'),
    path('instasram/subscription/<int:pk>', subscribe, name='subscribe'),
]
