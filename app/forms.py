from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from .models import Caixa
from .models import Conta

User = get_user_model()


class escolherMesForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['mes']


class CustomUserCreationForm(UserCreationForm):
    RANK_CHOICES = (
        (1, "Bixo"),
        (2,"Semi-bicho"),
        (3, "Morador"),
        (4,"Vice-decana"),
        (5, "Decana")
    )
    nome = forms.CharField(max_length=255)
    email = forms.EmailField(max_length=255)
    curso = forms.CharField(max_length=255)
    periodo = forms.IntegerField()
    rank = forms.CharField(widget=forms.Select(choices=RANK_CHOICES))

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'nome', 'curso', 'periodo', 'rank')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm):
        model = CustomUser
        fields = ('username', 'email', 'nome', 'curso', 'periodo')


class CaixaForm(ModelForm):
    class Meta:
        model = Conta
        fields = ['mes', 'nome', 'preco', 'setPaid']