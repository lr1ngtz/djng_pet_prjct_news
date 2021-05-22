from django import template
from django.db.models import Count

from ..models import Category

register = template.Library()


@register.simple_tag(name="get_list_of_categories")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("news_app/categories_list.html")
def show_categories():
    # categories = Category.objects.all()
    categories = Category.objects.annotate(cnt=Count('news')).filter(cnt__gt=0)
    return {"categories": categories}
