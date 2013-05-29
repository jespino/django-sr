from sr import sr as sr_func

from django import template
register = template.Library()


@register.simple_tag(name='sr')
def sr_tag(key, *args, **kwargs):
    return sr_func(key, *args, **kwargs)

try:
    from django_jinja.base import Library
    jinja_register = Library()

    @jinja_register.global_function
    def sr(key, *args, **kwargs):
        return sr_func(key, *args, **kwargs)
except ImportError:
    pass
