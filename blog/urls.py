from django.urls import path
# from .views import home
from .views import (
    BlogListView,
    BlogDetailView,
    ProfileDetailView,
    ProfileListView,
    CommentCreateView,
    CommentListView,
    MyBlogListCreateView,
    MyBlogDetailView
)


urlpatterns = [
    # path('', home, name='home'),
    path('blogs/', BlogListView.as_view(), name='blog-list'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('blogs/<int:blog_id>/comment/', CommentListView.as_view(), name='comment-list'),
    path('blogs/<int:blog_id>/comment/add/', CommentCreateView.as_view(), name='comment-add'),
    path('profiles/', ProfileListView.as_view(), name='profile-list'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile-detail'),
    path('my-blogs/', MyBlogListCreateView.as_view(), name='my-blog-list'),
    path('my-blogs/<int:pk>/', MyBlogDetailView.as_view(), name='my-blog-detail'),
]
