# first_app/templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='gte')
def gte(value, arg):
    return value >= arg

@register.filter(name='gt')
def gt(value, arg):
    return value > arg

@register.filter(name='lt')
def lt(value, arg):
    return value < arg
