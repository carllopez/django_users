import datetime

from django import template

register = template.Library()

@register.filter
def eligible(value):
    """Eligible filter"""
    today = datetime.datetime.today()
    age = abs(today.date() - value).days / 365
    
    return 'allowed' if age > 13 else 'blocked'

@register.filter
def bizzfuzz(value):
    """Bizzfuzz filter"""
    label = ''
    if value % 3 == 0:
    	label = 'Bizz'
    if value % 5 == 0:
    	label += 'Fuzz'
    if not label:
    	return value
    
    return label