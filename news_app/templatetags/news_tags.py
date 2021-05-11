from django import template

from news_app.models import Category

register = template.Library()


@register.simple_tag(name="get_list_of_categories")
def get_categories():
    return Category.objects.all()


@register.inclusion_tag("news_app/categories_list.html")
def show_categories():
    categories = Category.objects.all()
    return {"categories": categories}
