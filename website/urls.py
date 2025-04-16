from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('blog/topic/<str:topic_slug>/', views.blog_by_topic_htmx, name='blog_by_topic_htmx'),
    path('blog/<slug:topic_slug>/<slug:title_slug>/', views.blog_post, name='blog_post'),
    path('projects/', views.projects, name='projects'),
    path('resume/', views.download_resume, name='download_resume'),
]