from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    context = {"news": news, "title": "News list"}
    return render(request, "news_app/index.html", context=context)
