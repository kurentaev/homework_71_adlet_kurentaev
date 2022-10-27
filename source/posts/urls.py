from django.urls import path
from posts.views.base import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
]
