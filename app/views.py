from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm, CaixaForm, escolherMesForm
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
        action = request.POST.get('action')
        if action == 'catar':
            deleted_user_id = request.POST.get('id_conta')
            user = CustomUser.objects.get(pk=deleted_user_id)
            user.delete()
            context["success"] = "A moradora foi excluída do sistema!"
        elif action == 'subir':
            rankup_user_id = request.POST.get('id_conta')
            user = CustomUser.objects.get(pk=rankup_user_id)
            int_rank = int(user.rank)
            if int_rank < 5:
                int_rank += 1
                user.rank = str(int_rank)
                user.save()
        elif action == 'descer':
            rankup_user_id = request.POST.get('id_conta')
            user = CustomUser.objects.get(pk=rankup_user_id)
            int_rank = int(user.rank)
            if int_rank > 1:
                int_rank -= 1
                user.rank = str(int_rank)
                user.save()
    context['users'] = list(CustomUser.objects.get_queryset())
    return render(request, 'app/adminUsers.html', context)


def adminCaixinhaMes(request):
    context = {}
    if request.method == 'POST':
        mes_selecionado = request.POST.get('mes')
        context['mes'] = 1
        context['users'] = list(CustomUser.objects.get_queryset())
        context['valor'] = sum([conta.preco for conta in list(Conta.objects.get_queryset()) 
                                if int(mes_selecionado) == int(conta.mes.mes)])/CustomUser.objects.count()
    context['form'] = escolherMesForm()
    return render(request, 'app/adminCaixinhaMes.html', context)


def adminContas(request):
    context = {}
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'pagarConta':
            conta_paga_id = request.POST.get('id_conta')
            conta = Conta.objects.get(pk=conta_paga_id)
            conta.setPaid = True
            conta.save()
            context['success'] = "Sucesso ao alterar o estado da conta!"
        elif action == 'excluirContas':
            objectList = list(Conta.objects.get_queryset())
            for obj in objectList:
                obj.delete()
            context['success'] = "Todas contas foram excluídas do sistema!"

    context['caixas'] = list(Caixa.objects.get_queryset())
    context['contas'] = list(Conta.objects.get_queryset())
    return render(request, 'app/adminContas.html', context)
