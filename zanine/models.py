from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Cor(models.Model):
	nome = models.CharField(max_length=100)
	rgb = models.CharField(max_length=15, help_text='>>> separar valores com espaço <br>rgb = 0-255 0-255 0-255 <br>cinza = 0-255 <br>')

	def __str__(self):
		return self.nome

class Tag(models.Model):
	nome = models.CharField(max_length=100)
	cor = models.ForeignKey(Cor, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return self.nome

	class Meta:
		ordering = ['id']

class Local(models.Model):
	cidade = models.CharField(max_length=100)
	pais = models.CharField(max_length=2, choices=[('BR','Brasil'),('FR','França'),('CH','Suíça')], default='BR')
	cor = models.ForeignKey(Cor, blank=True, null=True, on_delete=models.SET_NULL)

	def __str__(self):
		return '%s [%s]' % (self.cidade, self.pais)

	class Meta:
		ordering = ['id']

def data_padrao(data):
	'''padroniza str data'''
	padrao=['1900','00','00']
	data=data.split('/')
	for i,p in enumerate(padrao):
		try:
			d=data[i]
			if len(d)>len(p):
				data[i]=d[:len(p)]
			elif len(d)<len(p):
				data[i]=p[:(len(p)-len(d))]+d
		except:
			data.append(p)
	return '/'.join(data)

class Evento(models.Model):
	tag = models.ForeignKey(Tag, blank=True, null=True, on_delete=models.SET_NULL)
	cidade = models.ForeignKey(Local, blank=True, null=True, on_delete=models.SET_NULL)
	info_pt = models.TextField(blank=True, null=True)
	info_fr = models.TextField(blank=True, null=True)
	
	inicio = models.CharField(max_length=10, help_text='aaaa/mm/dd ou aaaa/mm ou aaaa <br>>>> data do inicio de um periodo <br>>>> ou data de evento pontual')
	fim = models.CharField(max_length=10, blank=True, null=True, help_text='aaaa/mm/dd ou aaaa/mm ou aaaa <br>>>> data do fim de um periodo <br>>>> deixar em branco caso seja um evento pontual')

	def __str__(self):
		return '[%s] %s' % (self.tag, self.info_pt)

	class Meta:
		ordering = ['inicio']

	def save(self, *args, **kwargs):
		# define datas
		self.inicio=data_padrao(self.inicio)
		if self.fim:
			self.fim=data_padrao(self.fim)
		super().save(*args, **kwargs)


class Variavel(models.Model):
	inicio = models.IntegerField(default=1918, help_text='ano <br> início da timeline')
	fim = models.IntegerField(default=2060, help_text='ano <br> fim da timeline')
	largura = models.IntegerField(default=13, help_text='somente números <br> largura (em px) da coluna de cada ano da timeline ')
	altura = models.IntegerField(default=30, help_text='somente números <br> altura (em px) da linha de cada evento da timeline ')
	fonte = models.CharField(max_length=100,default='Courier', help_text='nome da fonte')
	text_size = models.IntegerField(default=12, help_text='somente números <br> tamanho (em px) do texto')
	data_size = models.IntegerField(default=10, help_text='somente números <br> tamanho (em px) do texto da data da timeline')
	padrao = models.BooleanField(default=True, help_text='define estas variaveis como padrão para o desenho da timeline')

	def save(self, *args, **kwargs):
		if self.padrao == True:
			outras_variaveis = Variavel.objects.exclude(id=self.id)
			if outras_variaveis:
				outras_variaveis.update(padrao=False)
		super(Variavel, self).save(*args, **kwargs)

	def __str__(self):
		txt='%s-%s_w=%s_h=%s_%s(%s/%s)' % (self.inicio,self.fim,self.largura,self.altura,self.fonte,self.text_size,self.data_size)
		if self.padrao:
			txt='[padrao] '+txt
		return txt

# class Ps(models.Model): 
# 	u0 = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE)
# 	d0 = models.DateTimeField(auto_now_add=True) # data de criaçao do projeto
# 	# varias imagens ?
# 	imagem = models.ImageField(upload_to=print_filepath, max_length=100,)
# 	visivel = models.BooleanField(default=True) # publico/privado
# 	titulo = models.CharField(max_length=400,blank=True,)
# 	link = models.URLField(max_length=400, blank=True,)
# 	ativo = models.BooleanField(default=True,verbose_name='link original ativo') # se o link ainda está ativo
# 	link2 = models.URLField( # link backup
# 		max_length=400,
# 		blank=True,
# 		verbose_name='internet archive',
# 		help_text='link do <a class="txt" href="https://web.archive.org/">internet archive</a> se o link original estiver indisponível'
# 	)
# 	tags = models.ManyToManyField(Tg, blank=True)
# 	obs = models.TextField(blank=True,verbose_name='detail',)
	
# 	def __str__(self):
# 		return self.titulo

# 	class Meta:
# 		ordering = ['-u0']

# 	def mudar_visibilidade(self):
# 		self.visivel = not self.visivel
# 		self.save()

# 	def save(self, *args, **kwargs):
# 		# link
# 		if not self.link:
# 			nome=self.imagem.name
# 			nome=nome.split('.')
# 			nome='.'.join(nome[:-1])
# 			if ':' in nome:
# 				nome=nome.replace(':','/')
# 			if nome[:4]!='http':
# 				nome='http://'+nome
# 			self.link = nome
# 		# titulo
# 		if not self.titulo:
# 			path=self.link
# 			if path[:4]=='http':
# 				path=path.split('/')[2]
# 			else:
# 				path=path.split('.')[0]
# 			self.titulo=path

# 		super().save(*args, **kwargs)

