from __future__ import unicode_literals

import sys
if sys.version_info[0] > 2:
    basestring = (str,)

from django.conf import settings


def sr(key, *args, **kwargs):
    keys = key.split('.')
    sr_value = getattr(settings, 'SR', {})

    for step in keys:
        try:
            sr_value = sr_value.get(step)
        except (KeyError, AttributeError):
            raise KeyError("Not valid key: {0}".format(key))

    if isinstance(sr_value, basestring):
        try:
            return sr_value.format(*args, **kwargs)
        except (ValueError, IndexError):
            raise ValueError("Not valid parameters for key {0}".format(key))
    return sr_value
