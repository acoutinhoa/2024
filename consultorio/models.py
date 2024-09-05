from django.conf import settings
from django.db import models
from django.utils import timezone
from random import choice
from string import punctuation, capwords
from django.contrib.auth.models import User


class Dentista(models.Model):
	genero = models.CharField(max_length=1, choices=[('m','Dr.'),('f','Dra.')]) # criar um padrao
	nome = models.CharField(max_length=150, unique=True)
	cro = models.CharField(max_length=20, unique=True)
		
	def __str__(self):
		return '%s %s' % (self.genero, self.nome)

class Funcionario(models.Model):
	genero = models.CharField(max_length=1, choices=[('m','ele/dele'),('f','ela/dela')]) # criar um padrao
	nome = models.CharField(max_length=150, unique=True)
	funcao = models.CharField(max_length=100)
		
	def __str__(self):
		return self.nome


def duas_letras(nome):
	nome = nome.split()
	letras = nome.pop(0)[0]
	for n in nome:
		if n not in ['de','da','das','do','dos', 'e',]:
			letras += n[0]
			break
	return letras

class Paciente(models.Model):
	# dados
	nome = models.CharField(max_length=300)
	nascimento = models.DateField(blank=True, null=True) # validar data
	cpf = models.CharField(unique=True, blank=True, null=True, max_length=14) # validar cpf
	obs = models.TextField(blank=True, null=True, verbose_name='referências')
	# sistema
	d0 = models.DateTimeField(auto_now_add=True) # data de cadastro no sistema
	dentistas = models.ManyToManyField(Dentista, blank=True) # definir automaticamente a partir da agenda
	
	def gerar_codigo(self):
		if Codigo.objects.filter(paciente=self).exists():
			codigo = Codigo.objects.get(paciente=self)
		else:
			codigo = Codigo.objects.create(letras=duas_letras(self.nome),paciente=self)
		return codigo

	def __str__(self):
		return self.nome

	def save(self, *args, **kwargs):
		# self.nome=self.nome.upper() # nome todo em maiusculo
		self.nome=capwords(self.nome) # primeira letra maiuscula
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['nome',]


class Codigo(models.Model):
	paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name='codigo')
	letras = models.CharField(max_length=2)
	ordem = models.PositiveIntegerField(blank=True)
	codigo = models.CharField(max_length=6, blank=True, null=True, editable=False)

	def __str__(self):
		return self.codigo

	def save(self, *args, **kwargs):
		self.letras = self.letras.upper()
		if not self.ordem:
			lista=Codigo.objects.filter(letras=self.letras).exclude(pk=self.pk).order_by('-ordem')
			if lista:
				ordem=lista[0].ordem
				self.ordem = ordem+1
			else:
				self.ordem = 1
		self.codigo=self.letras+str(self.ordem)
		super().save(*args, **kwargs)

	class Meta:
		ordering = ['letras','ordem']

class Contato(models.Model):
	paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='contatos')
	ddd = models.CharField(max_length=2, default='35')
	numero = models.CharField(max_length=9, blank=True, null=True)
	tipo = models.CharField(max_length=10, choices=[('whatsapp','WhatsApp'), ('celular', 'celular'), ('fixo', 'fixo'), ('trabalho', 'trabalho')], default='whatsapp')
	nome = models.CharField(max_length=100, blank=True, null=True)

	def __str__(self):
		return '[%s] +%s %s %s' % (self.paciente.codigo, self.pais, self.ddd, self.numero)

class Endereco(models.Model):
	paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE, related_name='endereco')
	cep = models.CharField(max_length=9, blank=True, null=True)
	rua = models.CharField(max_length=200, blank=True, null=True)
	numero = models.CharField(max_length=8, blank=True, null=True)
	complemento = models.CharField(max_length=20, blank=True, null=True)
	bairro = models.CharField(max_length=70, blank=True, null=True)
	cidade = models.CharField(max_length=200, default='Três Corações')
	estado = models.CharField(max_length=2, default='MG')
	pais = models.CharField(max_length=50, default='Brasil')

	def __str__(self):
		return '[%s] %s, %s - %s' % (self.paciente.codigo, self.rua, self.numero, self.bairro)




#############################################################
# teste pra criar nome de pacientes

lorem = '''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut eu tristique orci. Suspendisse tempor tristique felis, eget sagittis quam pulvinar ut. Praesent lacus augue, hendrerit vel lectus nec, laoreet molestie turpis. Nam at neque nec nulla eleifend porta. Cras blandit id est eleifend bibendum. Morbi accumsan tellus volutpat efficitur faucibus. Vivamus consectetur facilisis dictum. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Phasellus ultricies lectus lorem, nec feugiat lorem consequat eu. Duis semper ex id elementum maximus. Nam hendrerit purus vitae ligula molestie dignissim. Aenean odio lectus, tristique sed luctus at, cursus at mi. Mauris ut finibus quam. Integer efficitur mauris ac fermentum molestie. Sed porta sit amet nisl id gravida. Nullam placerat eros ac lorem commodo mattis.
Vivamus at porta massa. Donec porta venenatis arcu, non tincidunt justo efficitur at. Morbi nec libero a quam porta sodales vel et est. Morbi in rutrum nibh, a fermentum libero. Praesent feugiat tellus at turpis convallis, in elementum dui venenatis. Donec quis massa consequat, pharetra lorem eu, rhoncus urna. Sed quis libero sagittis, maximus dui a, sollicitudin ipsum. Aliquam cursus accumsan turpis non posuere. Quisque at diam enim. Sed rutrum justo non scelerisque porttitor. Ut finibus venenatis leo a porttitor. Vivamus at diam dictum, lacinia odio id, posuere nisi. Quisque finibus interdum consequat.
Donec pellentesque arcu ut facilisis rhoncus. Integer pharetra diam vitae nibh pulvinar aliquet. Duis leo dolor, elementum quis rhoncus sed, ullamcorper maximus ligula. Nam maximus pellentesque risus, a ultricies ante tempus sit amet. Sed bibendum, tellus sit amet aliquam rutrum, arcu turpis interdum augue, nec fermentum erat odio ut sapien. Etiam id urna in urna tristique facilisis eget vel elit. Sed eget augue at mauris mattis placerat. Morbi et magna nibh. Vestibulum bibendum rhoncus massa, eu tincidunt sapien bibendum sed. Pellentesque purus nisi, interdum eu odio sit amet, sodales iaculis quam. Curabitur interdum vehicula quam non volutpat. Maecenas sit amet turpis vel felis fermentum cursus. Curabitur euismod vitae diam lobortis porttitor. Maecenas vestibulum, diam vel lacinia molestie, risus est tempor urna, eget ultricies tortor metus nec arcu. Praesent nulla risus, tempor a lorem eget, eleifend mollis est. Duis blandit erat leo, vel lacinia enim dapibus vitae.
Ut sit amet convallis tortor, vitae euismod ante. Vivamus condimentum scelerisque hendrerit. Etiam nunc mi, scelerisque eu dui non, tempus volutpat ligula. Fusce luctus mi leo, vitae tempor turpis pellentesque non. Quisque sed cursus sapien. Mauris consequat felis a vulputate feugiat. Phasellus iaculis vel nibh et dignissim. Suspendisse lobortis pellentesque massa eget volutpat. Etiam tempor dictum turpis, quis feugiat tortor hendrerit ac. Aliquam interdum tellus purus, scelerisque posuere est aliquet convallis. Sed eros enim, ullamcorper in placerat at, laoreet vitae orci. Suspendisse cursus ex eu elit luctus porta. Praesent malesuada arcu eu enim consectetur, eget scelerisque turpis interdum. Vivamus id quam et dolor aliquam facilisis nec ac mauris. Fusce id justo fermentum, molestie nunc non, accumsan metus.
Nam porttitor urna sit amet ligula viverra vestibulum non ut magna. Aliquam quis vestibulum augue. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Phasellus faucibus non sapien ac accumsan. Suspendisse at sagittis orci. Nullam fringilla massa orci, nec pellentesque lorem rutrum dignissim. Nunc a varius purus. Praesent id est congue, tincidunt augue vitae, imperdiet ex. Nullam convallis, sem in condimentum gravida, eros velit tristique quam, a tristique nunc nisl a odio. Vivamus sodales dapibus mauris vel hendrerit. Duis tempor orci quis lobortis auctor. Curabitur euismod tellus in aliquam condimentum.
Nam volutpat nunc vel porttitor faucibus. Cras accumsan arcu eget tristique suscipit. In sollicitudin purus nec augue aliquam tincidunt. Sed odio justo, fringilla id aliquam vitae, luctus sed erat. Aliquam commodo lorem nec lacus ornare, posuere finibus lacus porta. Morbi quis vulputate massa. Curabitur rhoncus tempus dui in facilisis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Proin luctus massa ac suscipit volutpat. Proin ullamcorper vehicula dui. Maecenas gravida pharetra pretium.
Phasellus sed urna sem. Phasellus convallis, diam rhoncus suscipit rhoncus, nibh nunc imperdiet purus, hendrerit convallis ex sem in lorem. In bibendum dui vitae hendrerit tempus. Suspendisse ornare magna sed urna lacinia porta. Nullam vehicula dignissim placerat. Pellentesque ullamcorper risus vitae porttitor bibendum. Pellentesque sollicitudin mauris sit amet lacus malesuada ornare. Donec arcu arcu, rhoncus et porttitor et, malesuada et lorem. Nam id ex sollicitudin, malesuada ex quis, sagittis dolor. Curabitur ornare pharetra sem. Sed dictum accumsan turpis in varius. Nunc scelerisque enim lacus, at mattis nulla sagittis quis. Nullam placerat cursus sapien, quis porttitor nunc rutrum at. Nullam lobortis felis non ipsum tincidunt gravida. Sed quis lobortis mi. Duis condimentum condimentum est eu dapibus.
Morbi luctus ligula justo, vitae pretium tortor scelerisque ornare. Mauris maximus id nulla at interdum. Curabitur at varius velit. Donec vel nulla turpis. Proin iaculis ex neque, eu commodo velit tincidunt vel. Mauris nec euismod quam. Suspendisse quis dolor aliquam lectus faucibus sodales. Quisque consequat fermentum ante sollicitudin aliquet. Etiam congue porta nunc a feugiat. Morbi ac turpis at ante tincidunt ultricies. Quisque sodales libero non cursus egestas. Aenean a turpis sem. Praesent vestibulum nibh tellus, eget tristique purus tempus vitae. Integer ultricies enim vel nibh aliquet, quis tincidunt nulla viverra. Suspendisse venenatis, massa nec interdum tincidunt, nunc sem dictum augue, in maximus risus dolor at enim.
Praesent non arcu diam. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut interdum dignissim purus, at gravida nisi tristique eu. Etiam rhoncus ac diam eu scelerisque. Proin vitae urna ut justo varius ullamcorper. Curabitur velit ex, suscipit vel malesuada sed, venenatis sit amet neque. Nunc porttitor nibh metus, a posuere lorem tristique hendrerit. Mauris aliquam ultricies quam, quis sodales mauris fermentum sed. Mauris a turpis nisl. Cras viverra est velit, vitae iaculis diam elementum in. Vivamus efficitur, tellus eu molestie laoreet, enim magna facilisis neque, eu tincidunt velit erat vel justo. Suspendisse urna elit, aliquet at dapibus id, porta eu nulla. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam at imperdiet lorem. Aenean a nulla non nibh fringilla placerat.
Mauris sodales orci vitae turpis ornare posuere. Vivamus pellentesque felis nisi, vel mattis lacus imperdiet eu. Maecenas sollicitudin non nulla eget auctor. Etiam vitae mollis lacus, in molestie ipsum. Aenean elit tellus, gravida a libero et, venenatis sodales ligula. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut vestibulum faucibus neque id varius. Vestibulum scelerisque eget enim non elementum. Fusce pharetra ullamcorper consectetur. 
'''
lorem_lista=lorem.split()

def escolhe_palavra(lista_txt):
	palavra=choice(lista_txt)
	if palavra[-1] in punctuation:
		palavra=palavra[:-1]
	return palavra

def cria_nome():
	nome=''
	n2=choice(range(3,5))
	for j in range(n2):
		if j:
			nome+=' '
		palavra=''
		if not j or j==n2-1:
		    while len(palavra)<=3:
		        palavra=escolhe_palavra(lorem_lista)
		else:
		    palavra=escolhe_palavra(lorem_lista)
		nome+=palavra
	return nome

#############################################################


