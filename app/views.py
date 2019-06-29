from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm

def index(request):
    return render(request, 'app/index.html')


def hino(request):
    return render(request, 'app/hino.html')


def cadastro(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = UserCreationForm()
	return render(request, 'app/cadastro.html', {
		'form': form	
	})


def login(request):
    return render(request, 'app/login.html')


def caixa(request):
    return render(request, 'app/caixa.html')

