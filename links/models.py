from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.functions import Lower

# tag
class Tg(models.Model): 
	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL) # rever on_delete
	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
	tag = models.SlugField(max_length=200, unique=True, help_text='only letters, numbers, underscores or hyphens') # criar um padrao
	
	def __str__(self):
		return self.tag

	class Meta:
		ordering = [Lower('tag')]

def print_filepath(instance, filename):
    return 'links/{0}/{1}'.format(instance.u0.pk, filename)

# printscreen
class Ps(models.Model): 
	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
	# varias imagens ?
	imagem = models.ImageField(upload_to=print_filepath, max_length=100,)
	visivel = models.BooleanField(default=True) # publico/privado
	titulo = models.CharField(max_length=400,blank=True,help_text='se em branco, o titulo será gerado a partir do link')
	link = models.URLField(max_length=400, blank=True, help_text='se em branco, o link será gerado a partir do nome da imagem')
	ativo = models.BooleanField(default=True) # se o link ainda existe
	link2 = models.URLField(max_length=400,blank=True,help_text='link do internet archive, caso o link não exista mais') # link backup
	tags = models.ManyToManyField(Tg)
	obs = models.TextField(blank=True)
	
	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['?']

	def save(self, *args, **kwargs):
		# link
		if not self.link:
			nome=self.imagem.name
			nome=nome.split('.')
			nome='.'.join(nome[:-1])
			if ':' in nome:
				nome=nome.replace(':','/')
			if nome[:4]!='http':
				nome='http://'+nome
			self.link = nome
		# titulo
		if not self.titulo:
			path=self.link
			if path[:4]=='http':
				path=path.split('/')[2]
			else:
				path=path.split('.')[0]
			self.titulo=path

		super().save(*args, **kwargs)

