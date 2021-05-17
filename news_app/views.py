from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .models import Category, News
from .forms import NewsForm


class HomeNews(ListView):
    # # Analogue 'news = News.objects.all()'
    model = News
    template_name = "news_app/home_news_list.html"
    context_object_name = "news"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Main page"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


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
            # # It's for non-related forms "forms.Form"
            # news = News.objects.create(**form.cleaned_data)
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()

    context = {"form": form}
    return render(request, "news_app/add_news.html", context)
