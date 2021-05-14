from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, News
from .forms import NewsForm


def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "News list",
    }
    return render(request, "news_app/index.html", context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        "category": category
    }
    return render(request, "news_app/category.html", context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    context = {"news_item": news_item}
    return render(request, 'news_app/view_news.html', context=context)


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            news = News.objects.create(**form.cleaned_data)
            return redirect(news)
    else:
        form = NewsForm()

    context = {"form": form}
    return render(request, "news_app/add_news.html", context)
