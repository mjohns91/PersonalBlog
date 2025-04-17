from django.http import FileResponse
from django.shortcuts import render, get_object_or_404

import os

from .models import BlogPost, Project


def home(request):
    """Sends the user to the home page"""
    return render(request, 'home.html', {})

def blog(request):
    """Displays all blog posts for a given topic or all if 'all' is given"""
    posts = BlogPost.objects.all()
    topic = 'All'
    topic_slug = 'all'
    context = {"posts": posts, "topic": topic, 'topic_slug': topic_slug}
    return render(request, 'blog.html', context)

def blog_by_topic_htmx(request, topic_slug):
    if topic_slug == "all":
        posts = BlogPost.objects.all()
        topic = "All"
    else:
        topic = BlogPost.objects.get(topic_slug=topic_slug).topic
        posts = BlogPost.objects.filter(topic=topic)

    context = {"posts": posts, "topic": topic, 'topic_slug': topic_slug}
    # Render only the posts partial template for htmx
    return render(request, "partials/blog_posts.html", context)

def blog_post(request, topic_slug, title_slug):
    """Sends the user to a specific blog post"""
    post = get_object_or_404(BlogPost, topic_slug=topic_slug, title_slug=title_slug)
    return render(request, 'blog_post.html', {'post': post})

def projects(request):
    """Sends the user to the projects page"""
    project_list = Project.objects.all()
    return render(request, 'projects.html', {'projects': project_list})

def download_resume(request):
    # Path to the PDF file
    pdf_path = os.path.join('website','static','files','MatthewJohnson_Resume_Mar2025.pdf')
    return FileResponse(open(pdf_path, 'rb'), as_attachment=True, filename='MSJ_resume.pdf')
