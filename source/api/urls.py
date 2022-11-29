from django.urls import path, include
from rest_framework import routers
from api.views import PostViewSet, LikeViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('likes', LikeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='api_token_auth'),
    path('posts/like/<int:pk>/', LikeViewSet.as_view({'get': 'post'}), name='likes'),
]
