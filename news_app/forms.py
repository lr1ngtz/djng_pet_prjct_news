from django import forms

from .models import Category, News


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        # # All fields from our model
        # fields = '__all__'
        fields = ["title", "content", "is_published", "category"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "content": forms.Textarea(attrs={
                "class": "form-control", "rows": 5
            }),
            "category": forms.Select(attrs={"class": "form-control"}),
        }


# class NewsForm(forms.Form):
#     """This form (which is non-related with database) is better to use for
#     operations that will not work with our database.
#     For example: if our form will send emails or etc.."""
#     title = forms.CharField(
#         max_length=150,
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )
#     content = forms.CharField(
#         widget=forms.Textarea(attrs={"class": "form-control", "rows": 5})
#     )
#     # "label" works like "verbose_name" in models
#     is_published = forms.BooleanField(label="Is published?:", initial=True)
#     category = forms.ModelChoiceField(
#         queryset=Category.objects.all(),
#         empty_label="Choose category",
#         widget=forms.Select(attrs={"class": "form-control"})
#     )
