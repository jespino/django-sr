__version__ = (0, 0, 2)
import sys
if sys.version_info[0] > 2:
    basestring = (str,)

try:
    from django.conf import settings
except ImportError:
    pass

def sr(key, *args, **kwargs):
    keys = key.split('.')
    sr_value = getattr(settings, 'SR', {})
    for step in keys:
        try:
            sr_value = sr_value.get(step)
        except:
            raise Exception("Not valid key: {0}".format(key))

    if isinstance(sr_value, basestring):
        try:
            return sr_value.format(*args, **kwargs)
        except:
            raise Exception("Not valid parameters for key {0}".format(key))
    return sr_value
