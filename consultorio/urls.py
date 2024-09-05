from django.urls import path, include
from . import views

app_name = 'consultorio' # >>> referenciar como {% url 'consultorio:name' %}

# pacientes
pacientes_patterns = [
    path('', views.index, name='index'),
    # paciente
    path('<int:pk>/', views.paciente_index, name='paciente-index'),
    path('<int:pk>/dados/', views.paciente_dados, name='paciente-dados'),
    path('<int:pk>/fichas/', views.paciente_fichas, name='paciente-fichas'),
    path('<int:pk>/pagamentos/', views.paciente_pagamentos, name='paciente-pagamentos'),
    path('<int:pk>/consultas/', views.paciente_consultas, name='paciente-consultas'),
    # htmx
    path('busca/', views.paciente_search, name='paciente-search'),
    path('add/', views.paciente_add,name='paciente-add', ),
    path('<int:pk>/info/', views.paciente_info, name='paciente-info'),
    path('<int:pk>/endereco/', views.paciente_end, name='paciente-end'),
    path('<int:pk>/contato/', views.paciente_tel, name='paciente-tel'),
    path('<int:pk>/contato/add/', views.paciente_tel_add, name='paciente-tel-add'),
    path('<int:pk>/del/', views.paciente_del,name='paciente-del', ),
]

# dentistas
dentistas_patterns = [
    path('', views.dentistas_index, name='dentistas-index'),
    # htmx
]

# fichas
fichas_patterns = [
    path('', views.fichas_index, name='fichas-index'),
    # htmx
]

# pagamentos
pagamentos_patterns = [
    path('', views.pagamentos_index, name='pagamentos-index'),
    # htmx
]
# agenda
agenda_patterns = [
    path('', views.agenda_index, name='agenda-index'),
    # htmx
]

# htmx
htmx_patterns = [
    path('clear/', views.htmx_clear, name='htmx-clear'), # limpar uma sessao
]

urlpatterns = [
    # login - editar url
    # logout - editar url

    path('', views.home, name='home'),
    path('dentistas/', include(dentistas_patterns)),
    path('pacientes/', include(pacientes_patterns)),
    path('fichas/', include(fichas_patterns)),
    path('pagamentos/', include(pagamentos_patterns)),
    path('agenda/', include(agenda_patterns)),
    path('htmx/', include(htmx_patterns)),
]

































