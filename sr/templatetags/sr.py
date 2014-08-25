from django import template
register = template.Library()

from .. import sr as sr_func

@register.simple_tag(name='sr')
def sr_tag(key, *args, **kwargs):
    return sr_func(key, *args, **kwargs)


try:
    from django_jinja import library as jinja_library
    jinja_library.global_function("sr", sr_func)
except ImportError:
    pass
