from django.urls import path
from posts.views.base import IndexView
from posts.views.articles import PostView, PostCreate

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('instasram/', IndexView.as_view(), name='home'),
    path('instasram/post/<int:pk>', PostView.as_view(), name='post_detail'),
    path('instasram/post/add/', PostCreate.as_view(), name='post_add'),
]
