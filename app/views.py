from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CaixaForm
from django.contrib.auth import get_user_model
from .models import Caixa, Conta, CustomUser

User = get_user_model()

def index(request):
    count = User.objects.count()
    context = {
        'count': count
    }
    return render(request, 'app/index.html', context)


def hino(request):
    return render(request, 'app/hino.html')


def cadastro(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            userRank = int(request.user.rank)
            createdRank = int(request.POST['rank'])
            if userRank >= createdRank:
                form.save()
            else:
                context = {
                    'form': CustomUserCreationForm(),
                    'error': 0
                }
                return render(request, 'app/cadastro.html', context)
            return redirect('index')
    else:
        form = CustomUserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'app/cadastro.html', context)


def caixa(request):
    if request.method == 'POST':
        form = CaixaForm(request.POST)
        if form.is_valid():
            form.save()
            context = {
                "success": "Conta salva com sucesso!",
                "form": CaixaForm()
            }
        else:
            context = {
                "error": "Não foi possível salvar esta conta. Preencha corretamente o formulário.",
                "form": CaixaForm()
            }
        return render(request, 'app/caixa.html', context)
    else:
        form = CaixaForm()
    context = {
        'form': form
    }
    return render(request, 'app/caixa.html', context)


def ourHome(request):
    return render(request, 'app/ourHome.html')


def admin(request):
    context = {}

    if request.method == 'POST':
        deleted_user_id = request.POST.get('username')
        user = CustomUser.objects.get(pk=deleted_user_id)
        user.delete()
        context["success"] = "A moradora foi excluída do sistema!"

    context['caixas'] = list(Caixa.objects.get_queryset())
    context['contas'] = list(Caixa.objects.get_queryset())
    context['users'] = list(CustomUser.objects.get_queryset())
    return render(request, 'app/admin.html', context)


def adminUsers(request):
    context = {}
    if request.method == 'POST':
        deleted_user_id = request.POST.get('username')
        user = CustomUser.objects.get(pk=deleted_user_id)
        user.delete()
        context["success"] = "A moradora foi excluída do sistema!"

    context['users'] = list(CustomUser.objects.get_queryset())
    return render(request, 'app/adminUsers.html', context)


def adminContas(request):
    context = {}
    context['caixas'] = list(Caixa.objects.get_queryset())
    context['contas'] = list(Caixa.objects.get_queryset())
    return render(request, 'app/adminContas.html', context)
