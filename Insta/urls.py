from django.contrib import admin
from django.urls import path, include
from Insta.views import HelloDjango
from  Insta.views import PostsView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

urlpatterns = [

    path('', HelloDjango.as_view(), name='home'),
    path('posts/', PostsView.as_view(), name = 'posts'),
    path('post/<int:pk>',PostDetailView.as_view(), name='post_detail'),
    path('post/new', PostCreateView.as_view(), name='make_post'),
    path('posts/update/<int:pk>/', PostUpdateView.as_view(), name='post_update'),
    path('posts/delete/<int:pk>/', PostDeleteView.as_view(), name='post_delete'),

]