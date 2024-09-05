from django import template

register = template.Library()

import json
from django.utils.safestring import mark_safe
from django.core import serializers
from django.utils.encoding import is_protected_type
from django.core.serializers.json import DjangoJSONEncoder


@register.simple_tag
def set(value):
	return value

@register.filter()
def nobreaks(value):
	'''troca enter por espaco '''
	return value.replace('<br>', ' ')

@register.filter
def queryset_as_json(qs):
    """
    Sample usage:
        {{user.list_tipi_movimento|queryset_as_json}}
    """
    json_data = serializers.serialize("json", qs)
    return mark_safe(json_data)

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

