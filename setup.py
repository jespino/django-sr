# -*- coding: utf-8 -*-
from setuptools import setup
import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'tests.settings'

description = """
Django settings resolver.
"""

setup(
    name = "django-sr",
    url = "https://github.com/jespino/django-sr",
    author = "Jesús Espino",
    author_email = "jespinog@gmail.com",
    version='0.0.4',
    packages = [
        "sr",
        "sr.templatetags",
    ],
    description = description.strip(),
    install_requires=['django >= 1.3.0'],
    zip_safe=False,
    include_package_data = False,
    package_data = {},
    test_suite = 'nose.collector',
    tests_require = ['nose >= 1.2.1', 'django >= 1.3.0'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "License :: OSI Approved :: BSD License",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
