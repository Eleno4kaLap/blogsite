from django import template
from blog.models import MainSlider, Post

register = template.Library()


@register.inclusion_tag('blog/slider_tpl.html')
def get_slider():
    slider = MainSlider.objects.order_by('-created_at')[:1]
    return {'slider': slider}

@register.inclusion_tag('blog/fixed_posts_tpl.html')
def get_fixed_posts():
    posts = Post.objects.filter(fixed=True)
    return {'posts': posts}