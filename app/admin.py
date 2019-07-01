from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import (
    CustomUser,
    Caixa,
    Conta
)

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'nome', 'curso', 'periodo')

admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(Caixa)
# admin.site.register(Conta)