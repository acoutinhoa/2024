from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import *
from .forms import *

def index(request):
    lista = Projeto.objects.filter(visivel=True).order_by('-d0')
    return render(request, 'pf/index.html', {'lista':lista})

def info(request,pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'pf/info.html', {'projeto':projeto})

def add(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.u0 = request.user
            projeto.save()
            return redirect('info', pk=projeto.pk)
    else:
        form = ProjetoForm()
    return render(request, 'pf/edit.html', {'form': form})

def edit(request, pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    if request.method == "POST":
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            # projeto = form.save(commit=False)
            # post.author = request.user
            # post.published_date = timezone.now()
            # post.save()
            form.save()
            return redirect('info', pk=projeto.pk)
    else:
        form = ProjetoForm(instance=projeto)
    return render(request, 'pf/edit.html', {'form': form})


