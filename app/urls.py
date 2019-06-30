from django.urls import path, include

from repadmProject import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hino', views.hino, name='hino'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('caixa', views.caixa, name='caixa'),
]