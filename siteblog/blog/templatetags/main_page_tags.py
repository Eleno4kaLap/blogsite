from django import template
from blog.models import MainSlider, Post
from django.core.cache import cache
register = template.Library()


@register.inclusion_tag('blog/slider_tpl.html')
def get_slider():
    slider = MainSlider.objects.latest('created_at')
    quote = cache.get('quote')
    if quote:
        slider.title = quote['text']
        slider.content = quote['author']
    return {'slider': slider, 'quote': quote}


@register.inclusion_tag('blog/fixed_posts_tpl.html')
def get_fixed_posts():
    posts = Post.objects.filter(fixed=True)
    return {'posts': posts}
