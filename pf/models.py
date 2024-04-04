from django.conf import settings
from django.db import models
from django.utils import timezone

# from django.utils.text import slugify
# from django.conf.global_settings import LANGUAGES
# from django.utils.translation import gettext_lazy as _
# from django.utils.translation import get_language

# from django.core.exceptions import ValidationError




# class Grupo(models.Model):
# 	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
# 	d0 = models.DateTimeField(defaul=timezone.now) # data de criaçao do projeto
# 	editado = models.DateTimeField(auto_now=True) # ultima ediçao
# 	nome = models.CharField(max_length=200)
# 	equipe = models.ManyToManyField(User, through='Convite')
# 	adm = entra aqui?
	
# 	def salvar >>> define o u0 como adm automaticamente

# 	def __str__(self):
# 		return self.nome

# class Convite(models.Model):
# 	# só adm pode convidar
# 	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
# 	d0 = models.DateTimeField(defaul=timezone.now) # data de criaçao do projeto
# 	grupo = models.ForeignKey(Grupo)
# 	convidade = email
# 	adm = models.BooleanField


# class Lingua(models.Model):
# 	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
# 	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
# 	sigla = models.CharField(max_length=7, default=)
# 	def __str__(self):
# 		return self.sigla
# 	# salvar: tudo maiuscula ou tudo minuscula?


class Tag(models.Model):
	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
	tag = models.CharField(max_length=100, unique=True) # criar um padrao
	# slug = models.SlugField(max_length=100, unique=True)
	# Lingua = models.ForeignKey(Lingua, on_delete=models.CASCADE)
	
	def __str__(self):
		return self.tag

	# def criar_slug(self):


class Projeto(models.Model):
	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
	editado = models.DateTimeField(auto_now=True) # ultima ediçao
	visivel = models.BooleanField(default=False) # publico/privado  >>> pode dar acesso a um usuario especifico?
	# perfil = grupo
	titulo = models.CharField(max_length=200)
	texto = models.TextField()
	tags = models.ManyToManyField(Tag, blank=True)
	# inicio = models.DateField(blank=True, null=True) # rever
	# fim = models.DateField(blank=True, null=True) # rever
	# equipe = users
	# imagens
	# videos
	# proceso (prints?)
	# etapas (tempo) # acho que isso vai ser uma coisa separada - talvez vinculado com o processo?
	
	def publicar(self):
		self.visivel=True
		self.save()

	def __str__(self):
		return self.titulo

# class Tempo(models.Model):
# 	# tem que entender como isso vai se relacionar no projeto total
# 	# proximo passo



