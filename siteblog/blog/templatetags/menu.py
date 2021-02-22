from django import template
from blog.models import Category
from django.core.cache import cache

register = template.Library()

@register.inclusion_tag('blog/menu_tpl.html')
def show_menu(menu_class='menu'):
    categories = cache.get_or_set('categories', Category.objects.all(), 60)
    # categories = Category.objects.all()
    return {'categories': categories, 'menu_class': menu_class}