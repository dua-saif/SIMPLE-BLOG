from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),              # list all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # view post details
    path('post/new/', views.post_new, name='post_new'),       # add new post
    path('post/add/', views.add_post, name='add_post'),
]
