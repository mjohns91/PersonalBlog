from django.shortcuts import render, redirect

from website.models import BlogPost


def home(request):
    """Sends the user to the home page"""
    return render(request, 'home.html', {})

def blog(request):
    """Sends the user to the blogs page"""
    posts = BlogPost.objects.all()
    return render(request, 'blogs.html', {'posts': posts})