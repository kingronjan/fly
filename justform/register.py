from django import forms
from django.forms import fields, widgets


class RegisterForm(forms.Form):

    username = fields.CharField(
        max_length=16,
        min_length=6,
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
        allow_empty_file=True,
        label='Avatar',
        initial='web/avatars/default-avatar.jpg',
        widget=widgets.FileInput(
            attrs={
                'class': 'custom-file-input', 'id': 'customFile'
            }
        )
    )
    captcha = fields.CharField(
        label='Captcha',
        widget=widgets.Input(
            attrs={
                'class': 'form-control', 'placeholder': 'Enter captcha'
            }
        )
    )