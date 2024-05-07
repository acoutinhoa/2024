from django.shortcuts import render, get_object_or_404, redirect
from .models import *

def index(request,tag=None,pk=None):
	ps_list=Ps.objects.filter(visivel=True)
	if tag:
		try:
			tag=Tg.objects.get(tag=tag)
			tag_list=Tg.objects.exclude(pk=tag.pk)
			ps_list=ps_list.filter(tags=tag)
		except:
			return redirect('links:index')
	else:
		tag_list=Tg.objects.all()
	
	if pk:
		try:
			ps=ps_list.get(pk=pk)
		except:
			return redirect('links:index')
	else:
		ps=ps_list[0]


	return render(request, 'links/index.html', {
		'tag':tag, 
		'tag_list':tag_list, 
		'ps':ps, 
		'ps_list':ps_list,
	})


def perfil(request,nome,pk=None,tag=None):
    # projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'links/base.html', {})
