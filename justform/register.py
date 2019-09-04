from django import forms
from django.forms import fields, widgets

from repository.models import User


class RegisterForm(forms.Form):

    username = fields.CharField(
        max_length=16,
        min_length=3,
        required=True,
        label='Username',
        widget=widgets.TextInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter username'
            }
        ),
        error_messages={
            'required': '用户名不能为空',
        }
    )
    password = fields.CharField(
        required=True,
        max_length=32,
        label='Password',
        widget=widgets.PasswordInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter email'
            }
        )
    )
    email = fields.EmailField(
        required=True,
        label='Email',
        widget=widgets.EmailInput(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter email'
            }
        )
    )
    image = fields.ImageField(
        required=False,
        allow_empty_file=True,
        label='Avatar',
        widget=widgets.FileInput(
            attrs={
                'class': 'custom-file-input', 'id': 'customFile'
            }
        )
    )
    captcha = fields.CharField(
        required=True,
        label='Captcha',
        widget=widgets.Input(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter captcha'
            }
        )
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username):
            raise forms.ValidationError('username already existed')