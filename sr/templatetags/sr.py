from sr import sr

from django import template
register = template.Library()

@register.simple_tag(name='sr')
def sr_tag(key, *args, **kwargs):
    return sr(key, *args, **kwargs)
