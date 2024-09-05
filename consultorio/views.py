from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.db.models.functions import Lower
from .models import *
from .forms import *

##############################################################
# menus

menu = [
    ['início',reverse_lazy('consultorio:home')],
    ['dentistas',reverse_lazy('consultorio:dentistas-index')],
    ['pacientes',reverse_lazy('consultorio:index')],
    ['fichas',reverse_lazy('consultorio:fichas-index')],
    ['pagamentos',reverse_lazy('consultorio:pagamentos-index')],
    ['agenda',reverse_lazy('consultorio:agenda-index')],
]

def gerar_menu_paciente(paciente):
    menu_paciente = [
        ['dados',reverse_lazy('consultorio:paciente-dados', kwargs={'pk': paciente.pk})],
        ['fichas',reverse_lazy('consultorio:paciente-fichas', kwargs={'pk': paciente.pk})],
        ['pagamentos',reverse_lazy('consultorio:paciente-pagamentos', kwargs={'pk': paciente.pk})],
        ['consultas',reverse_lazy('consultorio:paciente-consultas', kwargs={'pk': paciente.pk})],
        ['deletar',reverse_lazy('consultorio:paciente-del', kwargs={'pk': paciente.pk})],
    ]
    return menu_paciente

##############################################################
# index

def home(request):
    ativo='início'
    return render(request, 'consultorio/home.html', {
        'menu':menu,
        'ativo':ativo,
        })

def dentistas_index(request):
    ativo='dentistas'
    return render(request, 'consultorio/dentistas.html', {
        'menu':menu,
        'ativo':ativo,
        })

##############################################################
# index - pacientes

@login_required
def index(request):
    ativo='pacientes'
    total = Paciente.objects.count()
    return render(request, 'consultorio/pacientes.html', {
        'menu':menu,
        'ativo':ativo,
        'total':total,
        })

# buscar pacientes
def paciente_search(request):
    busca = request.POST.get('search')
    pacientes_lista = None
    total=0
    if busca:
        # busca por nome ou (|) busca por codigo
        pacientes_lista = Paciente.objects.filter(nome__icontains=busca) | Paciente.objects.filter(codigo__codigo__icontains=busca)
        pacientes_lista = pacientes_lista.order_by(Lower('nome'))
    else:
        total = Paciente.objects.count()
    return render(request, 'consultorio/pacientes_lista.html', {
        'pacientes_lista': pacientes_lista, 
        'busca': busca,
        'total': total,
        })

# adicionar paciente
@login_required
def paciente_add(request):
    nome = request.POST.get('search')
    novo_paciente = Paciente.objects.create(nome=nome)
    return redirect('consultorio:paciente-index', pk=novo_paciente.pk)

##############################################################

@login_required
def fichas_index(request):
    ativo='fichas'
    return render(request, 'consultorio/fichas.html', {
        'menu':menu,
        'ativo':ativo,
        })

@login_required
def pagamentos_index(request):
    ativo='caixa'
    return render(request, 'consultorio/pagamentos.html', {
        'menu':menu,
        'ativo':ativo,
        })

@login_required
def agenda_index(request):
    ativo='agenda'
    return render(request, 'consultorio/agenda.html', {
        'menu':menu,
        'ativo':ativo,
        })

##############################################################
# pacientes

@login_required
def paciente_index(request, pk):
    ativo='pacientes'
    paciente = get_object_or_404(Paciente,pk=pk)
    return render(request, 'consultorio/paciente_index.html', {
        'menu':menu,
        'paciente':paciente, 
        'ativo':ativo,
        })

@login_required
def paciente_dados(request, pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    menu_paciente = gerar_menu_paciente(paciente)
    ativo_paciente = 'dados'
    return render(request, 'consultorio/paciente_dados.html', {
        'menu_paciente':menu_paciente,
        'ativo_paciente':ativo_paciente,
        'paciente':paciente, 
        })

@login_required
def paciente_fichas(request, pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    menu_paciente = gerar_menu_paciente(paciente)
    ativo_paciente = 'fichas'
    return render(request, 'consultorio/paciente_fichas.html', {
        'menu_paciente':menu_paciente,
        'ativo_paciente':ativo_paciente,
        'paciente':paciente, 
        })

@login_required
def paciente_pagamentos(request, pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    menu_paciente = gerar_menu_paciente(paciente)
    ativo_paciente = 'pagamentos'
    return render(request, 'consultorio/paciente_pagamentos.html', {
        'menu_paciente':menu_paciente,
        'ativo_paciente':ativo_paciente,
        'paciente':paciente, 
        })

@login_required
def paciente_consultas(request, pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    menu_paciente = gerar_menu_paciente(paciente)
    ativo_paciente = 'consultas'
    return render(request, 'consultorio/paciente_consultas.html', {
        'menu_paciente':menu_paciente,
        'ativo_paciente':ativo_paciente,
        'paciente':paciente, 
        })

# deletar paciente
@login_required
@require_http_methods(['DELETE'])
def paciente_del(request,pk):
    paciente=get_object_or_404(Paciente,pk=pk)
    paciente.delete()
    return redirect('consultorio:index',)

##############################################################
# paciente edit dados

def gerar_mensagem(form):
    return "<b>%s</b> atualizado" % ", ".join(form.changed_data)

@login_required
def paciente_info(request, pk, mensagem='', atualizar_nome=False):
    paciente = get_object_or_404(Paciente,pk=pk)
    if request.method == 'POST':
        dados_form = PacienteForm(request.POST, instance=paciente)
        if dados_form.is_valid():
            dados_form.save()
            if dados_form.has_changed():
                mensagem=gerar_mensagem(dados_form)
            if 'nome' in dados_form.changed_data:
                atualizar_nome=True
    else:
        dados_form = PacienteForm(instance=paciente)

    return render(request, 'consultorio/paciente_edit_info.html', {
        'paciente':paciente, 
        'dados_form':dados_form,
        'mensagem':mensagem,
        'atualizar_nome':atualizar_nome,
        })

@login_required
def paciente_end(request, pk, mensagem=''):
    paciente = get_object_or_404(Paciente,pk=pk)
    if request.method == 'POST':
        end_formset = EnderecoFormSet(request.POST, instance=paciente)
        if end_formset.is_valid():
            end_formset.save()
            for form in end_formset:
                if form.has_changed():
                    mensagem+=gerar_mensagem(form)
    else:
        end_formset = EnderecoFormSet(instance=paciente)

    return render(request, 'consultorio/paciente_edit_end.html', {
        'paciente':paciente, 
        'end_formset':end_formset,
        'mensagem':mensagem,
        })

@login_required
def paciente_tel(request, pk, mensagem=""):
    paciente = get_object_or_404(Paciente,pk=pk)
    if request.method == 'POST':
        tel_formset = ContatoFormSet(request.POST, instance=paciente)
        if tel_formset.is_valid():
            tel_formset.save()
            for form in tel_formset:
                if form.has_changed():
                    mensagem+=gerar_mensagem(form)
    tel_formset = ContatoFormSet(instance=paciente)

    return render(request, 'consultorio/paciente_edit_tel.html', {
        'paciente':paciente, 
        'tel_formset':tel_formset,
        'mensagem':mensagem,
        })

@login_required
def paciente_tel_add(request, pk):
    paciente = get_object_or_404(Paciente,pk=pk)
    novo_contato = Contato.objects.create(paciente=paciente)
    return redirect('consultorio:paciente-tel', pk=paciente.pk)

##############################################################
# htmx

def htmx_clear(request):
    return HttpResponse("")


    