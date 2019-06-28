from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hino', views.hino, name='hino'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('caixa', views.caixa, name='caixa'),
]