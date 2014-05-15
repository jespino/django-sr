Django Settings Resolver
========================

.. image:: https://travis-ci.org/jespino/django-sr.png?branch=master
    :target: https://travis-ci.org/jespino/django-sr

.. image:: https://coveralls.io/repos/jespino/django-sr/badge.png?branch=master
    :target: https://coveralls.io/r/jespino/django-sr?branch=master

.. image:: https://pypip.in/v/django-sr/badge.png
    :target: https://crate.io/packages/django-sr

.. image:: https://pypip.in/d/django-sr/badge.png
    :target: https://crate.io/packages/django-sr


The siple way to resolve some data defined on settings. You can easy to use it on
any part of you python code on your django project.

Also, this exposeses templatetags for django template engine and jinja template enjine
for easy use it from templates. See examples to better understand how it works.


How to install
--------------

You can also install it with: ``pip install django-sr``


Configuration
-------------

Add the sr app to your installed apps and define your settings :code:`SR` variable as a dictionary.

Example:

.. code-block:: python

    # settings.py
    SR = {
        'footer': {
            'phone': '+34 987654321',
            'address': 'Foo Bar Street, 32',
            'other_text': 'Text with parameters {0}',
        },
        'header': {
            'logo': {
                'alt': 'Logo image',
                'src': 'http://foo.bar/images/logo.png'
            }
        }
    }


Usage examples
--------------

Use it directly from your code.

.. code-block:: python

    from sr import sr
    logo_alt = sr('header.logo.alt')  # Logo image
    other_text = sr('footer.other_text', 'parameter')  # Text with parameters parameter


Also, from django templates with the ``sr`` template tag:

.. code-block:: django

    {% load sr %}
    <span class="phone">{% sr 'footer.phone' %}</span>
    <span class="other">{% sr 'footer.other_text' 'text' %}</span>


And you can use it from jinja templates using the ``sr`` global function:

.. code-block:: jinja

    <span class="phone">{{ sr('footer.phone') }}</span>
    <span class="other">{{ sr('footer.other_text', 'text') }}</span>


For jinja template integration for django you need use `django-jinja <https://github.com/niwibe/django-jinja>`_
