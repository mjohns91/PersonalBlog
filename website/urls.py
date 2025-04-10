from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog_all, name='blog_all'),
    path('blog/<str:target_topic>/', views.blog_by_topic, name='blog_by_topic'),
    path('blog/<str:post_topic>/<str:post_title>/', views.blog_post, name='blog_post'),
    path('projects/', views.projects, name='projects'),
]