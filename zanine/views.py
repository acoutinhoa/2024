from django.shortcuts import render, get_object_or_404, redirect
from random import choice
from .models import *

def tl(request, tipo):
	tipos=['cidades','tags']
	if not tipo:
		tipo=choice(tipos)

	variaveis, created=Variavel.objects.get_or_create(padrao=True)

	cidades=Cidade.objects.all()
	tags=Tag.objects.all()
	cores=Cor.objects.all()

	# Name.objects.exclude(alias__isnull=True)
	eventos=Evento.objects.exclude(visivel=False)
	por_cidade=eventos.order_by('cidade','inicio')
	por_tag=eventos.order_by('tag','inicio')

	if tipo==tipos[0]:
		eventos=por_cidade
		legenda=por_tag
		lh=Tag.objects.exclude(evento__isnull=True).count()
	
		if eventos.filter(tag__isnull=True):
			lh+=1

	elif tipo==tipos[1]:
		eventos=por_tag
		legenda=por_cidade
		lh=Cidade.objects.exclude(evento__isnull=True).count()

		if eventos.filter(cidade__isnull=True):
			lh+=1

	return render(request, 'zanine/index.html', {
	'eventos':eventos, 
	'legenda':legenda, 
	'lh':lh,
	'tipos':tipos,
	'tipo':tipo,
	'variaveis':variaveis,
	'cidades':cidades,
	'tags':tags,
	'cores':cores,	
})

