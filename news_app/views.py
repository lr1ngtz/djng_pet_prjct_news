from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import NewsForm
from .models import Category, News


class HomeNews(ListView):
    """This class-based view works like function 'index'"""
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


class NewsByCategory(ListView):
    model = News
    template_name = "news_app/home_news_list.html"
    context_object_name = "news"
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"],
            is_published=True
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = Category.objects.get(pk=self.kwargs["category_id"])
        return context


class ViewNews(DetailView):
    model = News
    # template_name = "news_app/news_detail.html"
    context_object_name = "news_item"


class CreateNews(CreateView):
    form_class = NewsForm
    template_name = "news_app/add_news.html"
    # We define 'success_url' if we didn't define
    # 'get_absolute_url' in our Model
    # success_url = reverse_lazy("home")


# def index(request):
#     news = News.objects.all()
#     context = {
#         "news": news,
#         "title": "News list",
#     }
#     return render(request, "news_app/index.html", context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        "category": category
    }
    return render(request, "news_app/category.html", context=context)


# def view_news(request, news_id):
#     # news_item = News.objects.get(pk=news_id)
#     news_item = get_object_or_404(News, pk=news_id)
#     context = {"news_item": news_item}
#     return render(request, 'news_app/view_news.html', context=context)


# def add_news(request):
#     if request.method == "POST":
#         form = NewsForm(request.POST)
#         if form.is_valid():
#             # # It's for non-related forms "forms.Form"
#             # news = News.objects.create(**form.cleaned_data)
#             news = form.save()
#             return redirect(news)
#     else:
#         form = NewsForm()

#     context = {"form": form}
#     return render(request, "news_app/add_news.html", context)
