from django.db import models
from django.utils.text import slugify

class BlogPost(models.Model):
    """Represents a blog post."""
    title = models.CharField(max_length=200)
    preview = models.TextField(default="not defined")
    content = models.TextField()
    topic = models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    title_slug = models.SlugField(max_length=200, unique=True, blank=True)
    topic_slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title


class Project(models.Model):
    """Represents a project post."""
    title = models.CharField(max_length=200)
    preview = models.TextField(default="not defined")
    content = models.TextField()
    topic = models.CharField(max_length=200)
    posted_date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    github_link = models.URLField(blank=True)
    title_slug = models.SlugField(max_length=200, unique=True, blank=True)
    topic_slug = models.SlugField(max_length=200, unique=True, blank=True)

    def __str__(self):
        return self.title
