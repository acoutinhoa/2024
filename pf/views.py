from django.shortcuts import render
from django.utils import timezone
from .models import *

def index(request):
    lista = Projeto.objects.filter(visivel=True).order_by('-d0')
    return render(request, 'pf/index.html', {'lista':lista})