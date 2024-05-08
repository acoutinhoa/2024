from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def index(request,tag=None,pk=None):
	ps_list=Ps.objects.filter(visivel=True)

	if tag:
		tags=tag.split('+')
		tag=[]
		for t in tags:
			try:
				t=Tg.objects.get(tag=t)
				tag.append(t)
				ps_list=ps_list.filter(tags=t)
			except:
				return redirect('links:index')

	if pk:
		try:
			ps=ps_list.get(pk=pk)
		except:
			return redirect('links:index')
	elif ps_list:
		ps=ps_list[0]
	else:
		ps=None

	tag_list=Tg.objects.filter(ps__in=ps_list).distinct()
	if tag:
		for t in tag:
			tag_list=tag_list.exclude(tag=t)

	return render(request, 'links/index.html', {
		'tag':tag, 
		'tag_list':tag_list, 
		'ps':ps, 
		'ps_list':ps_list,
	})


def perfil(request,nome,pk=None,tag=None):
    # projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'links/base.html', {})
