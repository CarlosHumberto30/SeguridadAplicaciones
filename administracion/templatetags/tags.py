from django import template

register = template.Library()

@register.simple_tag
def increment( cont ):
    return cont+1
