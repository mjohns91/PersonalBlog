from django.contrib import admin
from .models import BlogPost, Project

class BlogPostAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'title_slug': ('title',),
        'topic_slug': ('topic',),
    }

class ProjectAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'title_slug': ('title',),
        'topic_slug': ('topic',),
    }

# Register your models here.
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Project, ProjectAdmin)