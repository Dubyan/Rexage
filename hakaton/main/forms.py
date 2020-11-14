from django.contrib.auth.forms import UserCreationForm
from django import forms


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)

    field_order = ['username', 'password1', 'password2']