from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # print(dir(request))
    return HttpResponse('QWEQWEQWEQWE')


def test(request):
    return HttpResponse('<h1>test page</h1>')
