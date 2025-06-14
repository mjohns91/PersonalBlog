from django import template

register = template.Library()


@register.filter
def unique_topics(posts):
    """Extract unique topics from a list of posts."""
    seen_topics = set()
    for post in posts:
        if post.topic_slug not in seen_topics:
            seen_topics.add(post.topic_slug)
            yield post.topic_slug
