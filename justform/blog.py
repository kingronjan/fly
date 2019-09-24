from django import forms
from django.forms import fields, widgets

from repository.models import Blog


class BlogForm(forms.Form):
    title = forms.CharField(
        max_length=32,
        label='Blog title',
        help_text='Input a title of your blog, max 32 character',
        widget=widgets.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    summary = forms.CharField(
        max_length=128,
        widget=widgets.Textarea(
            attrs={'class': 'form-control'}
        ),
        label='Blog summary',
        help_text='Summary of your blog, max 128 character'
    )
