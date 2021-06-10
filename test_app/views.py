from django.shortcuts import render

from test_app.models import Rubric


def test(request):
    rubrics = Rubric.objects.all()
    return render(request, 'test_app/test.html', {'rubrics': rubrics})


def get_rubric(request):
    pass
