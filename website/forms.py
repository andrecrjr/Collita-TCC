from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, label="Primeiro nome", required=True, help_text='Obrigatório')
    last_name = forms.CharField(max_length=30, label="Ultimo nome")
    email = forms.EmailField(max_length=254, help_text='Obrigatório')

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
