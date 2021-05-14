from django import forms

from .models import Category, News


class NewsForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control"})
    )
    content = forms.CharField(
        widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
    )
    # "label" works like "verbose_name" in models
    is_published = forms.BooleanField(label="Is published?:", initial=True)
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        empty_label="Choose category",
        widget=forms.Select(attrs={"class": "form-control"})
    )
