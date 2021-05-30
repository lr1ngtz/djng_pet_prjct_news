from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.views.generic import CreateView, DetailView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib import messages

from .forms import NewsForm, UserRegistrationForm, UserLoginForm
from .models import Category, News
from .utils import MyMixin


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # automatically login after register
            login(request, user)
            messages.success(request, 'You are registered successfully')
            return redirect('home')
        else:
            messages.error(request, 'Registration Error')
    else:
        form = UserRegistrationForm()
    return render(request, 'news_app/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')

    else:
        form = UserLoginForm
    return render(request, 'news_app/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')


def test(request):
    """In this function we show how built-in pagination works with
    function-based views."""
    objects = ['igor', 'oleg', 'petya', 'vasya', 'pasha', 'artem', 'anton']
    paginator = Paginator(objects, 2)
    page_num = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_num)
    return render(request, 'news_app/test.html', {'page_obj': page_obj})


class HomeNews(MyMixin, ListView):
    """This class-based view works like function 'index'"""
    # # Analogue 'news = News.objects.all()'
    model = News
    template_name = "news_app/home_news_list.html"
    context_object_name = "news"
    mixin_prop = 'string from mixin'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_upper("Main page")
        context['mixin_prop'] = self.get_prop()
        return context

    def get_queryset(self):
        """'select_related' works only with models that have a 'foreign key'
        relation.
        We use 'select_related' to optimize sql-queries, which calls when our
        page is working"""
        return News.objects.filter(is_published=True).select_related('category')


class NewsByCategory(MyMixin, ListView):
    model = News
    template_name = "news_app/home_news_list.html"
    context_object_name = "news"
    allow_empty = False
    paginate_by = 2

    def get_queryset(self):
        return News.objects.filter(
            category_id=self.kwargs["category_id"],
            is_published=True
        ).select_related('category')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = self.get_upper(Category.objects.get(pk=self.kwargs["category_id"]))
        return context


class ViewNews(DetailView):
    model = News
    # template_name = "news_app/news_detail.html"
    context_object_name = "news_item"


class CreateNews(LoginRequiredMixin, CreateView):
    """We use 'LoginRequiredMixin' when we want to hide controller(view)"""
    form_class = NewsForm
    template_name = "news_app/add_news.html"
    # # redirect to admin if we aren't authenticated and trying to go
    # # to '/add_news/
    login_url = '/admin/'  # From LoginRequiredMixin
    # # redirect to '403 Forbidden' if we aren't authenticated and trying to go
    # # to '/add_news/
    # raise_exception = True  # From LoginRequiredMixin
    # # We define 'success_url' if we didn't define
    # # 'get_absolute_url' in our Model
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
