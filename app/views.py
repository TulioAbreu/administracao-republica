from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

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
    return render(request, 'app/caixa.html')

def ourHome(request):
    return render(request, 'app/ourHome.html')
