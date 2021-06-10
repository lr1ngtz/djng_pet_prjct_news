from django.urls import path

from test_app.views import test, get_rubric

urlpatterns = [
    path('', test, name='test'),
    path('rubric/<int:pk>/', get_rubric, name='rubric'),
]
