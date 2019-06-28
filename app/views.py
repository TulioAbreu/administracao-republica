from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'app/index.html')


def hino(request):
    return render(request, 'app/hino.html')


def cadastro(request):
    return render(request, 'app/cadastro.html')


def login(request):
    return render(request, 'app/login.html')


def caixa(request):
    return render(request, 'app/caixa.html')