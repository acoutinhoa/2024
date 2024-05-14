from django import template

register = template.Library()

@register.filter()
def linktags(value):
	'''soma tags pra url'''
	lista=[i for i in value]
	return '+'.join(lista)

@register.filter()
def linktagsadd(value, arg):
	'''junta tags para crar link composto'''
	lista=[]
	if arg:
		for i in arg:
			lista.append(i.tag)
	lista.append(value.tag)
	return '+'.join(lista)

@register.filter()
def linktagsremove(value, arg):
	'''exclui tag da lista pra url'''
	lista=[]
	if arg:
		for i in arg:
			if i != value:
				lista.append(i.tag)
	return '+'.join(lista)

@register.simple_tag
def set(value):
	return value
