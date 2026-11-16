from django.urls import path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, get_posts, generate_post, summarize_post_view
from .views import (
    UserCreateAPIView,
    CategoryCreateAPIView,
    PostCreateAPIView,
    CommentCreateAPIView,
)

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('posts/get_post/', get_posts, name='get_post'),
    path('posts/generate/', generate_post, name='generate_post'),
    path('posts/<int:post_id>/summarize/', summarize_post_view, name='summarize_post'),
    path('users/', UserCreateAPIView.as_view(), name='user-create'),
    path('categories/', CategoryCreateAPIView.as_view(), name='category-create'),
    path('posts/', PostCreateAPIView.as_view(), name='post-create'),
    path('comments/', CommentCreateAPIView.as_view(), name='comment-create'),
] 
urlpatterns += router.urls
