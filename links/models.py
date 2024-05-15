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
	titulo = models.CharField(max_length=400,blank=True,)
	link = models.URLField(max_length=400, blank=True,)
	ativo = models.BooleanField(default=True,verbose_name='link original ativo') # se o link ainda está ativo
	link2 = models.URLField( # link backup
		max_length=400,
		blank=True,
		verbose_name='internet archive',
		help_text='link do <a class="txt" href="https://web.archive.org/">internet archive</a> se o link original estiver indisponível'
	)
	tags = models.ManyToManyField(Tg, blank=True)
	obs = models.TextField(blank=True,verbose_name='detail',)
	
	def __str__(self):
		return self.titulo

	class Meta:
		ordering = ['-u0']

	def mudar_visibilidade(self):
		self.visivel = not self.visivel
		self.save()

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

