# -*- coding: utf-8 -*-
from setuptools import setup

description = """
Django settings resolver.
"""

setup(
    name = "django-sr",
    url = "https://github.com/jespino/django-sr",
    author = "Jesús Espino",
    author_email = "jespinog@gmail.com",
    version=':versiontools:sr:',
    packages = [
        "sr",
        "sr.templatetags",
    ],
    description = description.strip(),
    install_requires=[],
    setup_requires = [
        'versiontools >= 1.8',
    ],
    zip_safe=False,
    include_package_data = False,
    package_data = {},
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "Environment :: Web Environment",
        "Framework :: Django",
    ],
)
