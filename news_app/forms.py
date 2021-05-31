from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField
import re

from .models import News


class ContactForm(forms.Form):
    subject = forms.CharField(
        label='Subject',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'autocomplete': 'off'
            })
    )
    content = forms.CharField(
        label='Content',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5})
    )
    captcha = CaptchaField()


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        # help_text='Some prompt for field',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'autocomplete': 'off'
            })
    )
    password = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username',
        # help_text='Some prompt for field',
        widget=forms.TextInput(attrs={
            'class': 'form-control', 'autocomplete': 'off'
            })
    )
    email = forms.EmailField(
        label='Email Address',
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     'username': forms.TextInput(attrs={'class': 'form-control'}),
        #     'email': forms.EmailInput(attrs={'class': 'form-control'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        # }


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

    def clean_title(self):
        """Custom validator that doesn't allow to create a title which starts
        with a number!"""
        title = self.cleaned_data["title"]
        if re.match(r"\d", title):
            raise ValidationError("Title mustn't start with a number!")
        return title


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
