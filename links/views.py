from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.views.decorators.clickjacking import xframe_options_exempt
from django.db.models.functions import Lower
from django.contrib.auth.models import User
from .models import *
from .forms import *

def index(request,nome=None, tag=None,pk=None):
	# pessoas
	perfil=None
	owner=False
	if nome:
		perfil=get_object_or_404(User, username=nome)
		if request.user==perfil:
			owner=True

	# lista total de links
	if nome:
		ps_list=Ps.objects.filter(u0=perfil)
		if request.user != perfil:
			ps_list=ps_list.filter(visivel=True)
	else:
		ps_list=Ps.objects.filter(visivel=True)

	# filtro e lista de tags
	tag_set=[]
	if tag:
		for t in tag.split('+'):
			try:
				t=Tg.objects.get(tag=t)
				tag_set.append(t)
				ps_list=ps_list.filter(tags=t) # filtra a lista de links
			except: # se tiver uma tag zuada
				if nome:
					return redirect('links:perfil', nome=nome) 
				else:
					return redirect('links:index') 

	# cria a lista de tags a partir da lista de links que já foi filtrada
	tag_list=Tg.objects.filter(ps__in=ps_list).distinct().order_by(Lower('tag'))

	# randomiza um link	
	if not pk and ps_list:
		pk=ps_list.order_by('?')[0].pk

	# reordena lista de prints
	ps_list=ps_list.order_by('-d0')

	return render(request, 'links/index.html', {
		'tag_set':tag_set, 
		'tag_list':tag_list, 
		'ps_list':ps_list,
		'perfil':perfil,
		'pk':pk,
		'nome':nome,
		'owner':owner,
	})

@xframe_options_exempt
def ps_info(request, pk, nome=None):
	ps=get_object_or_404(Ps, pk=pk)
	owner=False
	if request.user==ps.u0:
		owner=True
	return render(request, 'links/link-info.html', {
		'ps':ps, 
		'nome':nome,
		'owner':owner,
	})

@login_required
@xframe_options_exempt
def ps_edit(request, pk, nome):
	ps=get_object_or_404(Ps, pk=pk)
	if request.user==ps.u0:
		if request.method == "POST":
			form = PsForm(request.POST, request.FILES, instance=ps)
			if form.is_valid():
				form.save()
				return redirect('links:ps-info', pk=pk, nome=nome)
		else:
			form = PsForm(instance=ps)
	return render(request, 'links/link_edit.html', {'form': form,})

@login_required
def ps_add(request):
	ps_list=Ps.objects.filter(u0=request.user).order_by('-d0')

	if request.method == "POST":
		form = PsForm(request.POST, request.FILES)
		if form.is_valid():
			ps = form.save(commit=False)
			ps.u0 = request.user
			ps.save()
			form.save_m2m() # pra salvar o many2many field
			return redirect('links:index-link', pk=ps.pk)
	else:
		form = PsForm()
	return render(request, 'links/link_edit.html', {'form': form, 'ps_list':ps_list,})

# def proprietario(user,pk):
# 	return request.user == ps.u0

# @user_passes_test(proprietario, login_url="/login/")
@login_required
def ps_delete(request, pk):
	ps = get_object_or_404(Ps, pk=pk)
	# verifica se o user é o dono do link antes de deletar
	if request.user == ps.u0:
		ps.delete()
	return redirect(request.META.get('HTTP_REFERER'))

