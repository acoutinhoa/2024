from django import template

register = template.Library()


@register.simple_tag
def set(value):
	return value

@register.filter()
def nobreaks(value):
	'''troca enter por espaco '''
	return value.replace('<br>', ' ')

# @register.filter()
# def linktagsadd(value, arg):
# 	'''junta tags para crar link composto'''
# 	lista=[]
# 	if arg:
# 		for i in arg:
# 			lista.append(i.tag)
# 	lista.append(value.tag)
# 	return '+'.join(lista)

# @register.filter()
# def linktagsremove(value, arg):
# 	'''exclui tag da lista pra url'''
# 	lista=[]
# 	if arg:
# 		for i in arg:
# 			if i != value:
# 				lista.append(i.tag)
# 	return '+'.join(lista)

