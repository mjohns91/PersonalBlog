from django.shortcuts import render, get_object_or_404

from website.models import BlogPost, Project


def home(request):
    """Sends the user to the home page"""
    return render(request, 'home.html', {})

def blog_all(request):
    """Displays all blog posts"""
    posts = BlogPost.objects.all()
    return render(request, 'blog.html', {'posts': posts})

def blog_by_topic(request, target_topic):
    """Displays all blog posts for a given topic"""
    if target_topic == 'all':
        return blog_all(request)
    topic = target_topic.capitalize()
    all_topics = BlogPost.objects.values_list('topic', flat=True).distinct()
    posts = BlogPost.objects.filter(topic=target_topic)
    return render(request, 'blog_by_topic.html', {'topic': topic, 'posts': posts, 'all_topics': all_topics})

def blog_post(request, post_topic, post_title):
    """Sends the user to a specific blog post"""
    post = get_object_or_404(BlogPost, title=post_title)
    return render(request, 'blog_post.html', {'post': post})

def projects(request):
    """Sends the user to the projects page"""
    project_list = Project.objects.all()
    return render(request, 'projects.html', {'projects': project_list})