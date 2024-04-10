from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import *

def index(request):
    lista = Projeto.objects.filter(visivel=True).order_by('-d0')
    return render(request, 'pf/index.html', {'lista':lista})

def info(request,pk):
    projeto = get_object_or_404(Projeto, pk=pk)
    return render(request, 'pf/info.html', {'projeto':projeto})

