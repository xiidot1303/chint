from django import template
register = template.Library()

@register.filter
def residue(a, b):
    return a%b