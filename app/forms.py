from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    nome = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    curso = forms.CharField(max_length=255)
    periodo = forms.IntegerField()
    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'nome', 'curso', 'periodo')

class CustomUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'nome', 'curso', 'periodo')
