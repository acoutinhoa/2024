from django.shortcuts import render, get_object_or_404, redirect
from random import choice
from .models import *

def tl(request, tipo):
	tipos=['cidades','tags']
	if not tipo:
		tipo=choice(tipos)

	variaveis, created=Variavel.objects.get_or_create(padrao=True)

	# Name.objects.exclude(alias__isnull=True)
	eventos=Evento.objects.exclude(visivel=False)
	por_cidade=eventos.order_by('cidade','inicio')
	por_tag=eventos.order_by('tag','inicio')

	if tipo==tipos[0]:
		eventos=por_cidade
		legenda=por_tag
		lh=Tag.objects.all().count()
	elif tipo==tipos[1]:
		eventos=por_tag
		legenda=por_cidade
		lh=Local.objects.all().count()

	return render(request, 'zanine/index.html', {
	'eventos':eventos, 
	'legenda':legenda, 
	'lh':lh,
	'tipos':tipos,
	'tipo':tipo,
	'variaveis':variaveis,
})

