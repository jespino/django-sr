Django Settings Resolver
========================

Django settings resolver easy the definition of variables on the settings file
identified by a "code".

How to install
--------------

You can also install it with: ``pip install django-sr``


Configuration
-------------

Add the sr app to your installed apps and define your settings SR variable as a dictionary.

Example::

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
    },
    ...
  }

Usage
-----

You can use this directly from templates with the sr template tag. Example::

  {% load sr %}
  <span class="phone">{% sr footer.phone %}</span>
  <span class="other">{% sr footer.other_text "text" %}</span>

You can use it directly from your code. Example::

  from sr import sr
  logo_alt = sr('header.logo.alt')  # Logo image
  other_text = sr('footer.other_text', 'parameter')  # Text with parameters parameter
