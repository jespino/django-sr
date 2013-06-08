# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys

from django.utils import unittest
from django.conf import settings
from django.template import Template, Context
from django_jinja.base import env

from sr import sr
from sr.templatetags.sr import *


# Python 2.7 compatibility fix
if sys.version_info[0] < 3:
    unittest.TestCase.assertRaisesRegex = unittest.TestCase.assertRaisesRegexp


class TestSequenceFunctions(unittest.TestCase):
    def test_sr_not_valid_key(self):
        self.assertRaisesRegex(Exception, "Not valid key: not-valid-key.not-valid-subkey", sr, "not-valid-key.not-valid-subkey")
        self.assertRaisesRegex(Exception, "Not valid key: test1.not-valid-subkey", sr, "test1.not-valid-subkey")
        self.assertRaisesRegex(Exception, "Not valid key: test2.test3.test4", sr, "test2.test3.test4")

    def test_sr_not_valid_params(self):
        self.assertRaisesRegex(Exception, "Not valid parameters for key test4.test4", sr, "test4.test4", "param")

    def test_sr_valid_key(self):
        self.assertEqual(sr('test1'), 'Test1')
        self.assertEqual(sr('test2.test3'), 'Test3')
        self.assertEqual(sr('test4.test4', 'testing', 'testing2'), 'Test4 testing testing2')

    def test_sr_django_templatetag(self):
        result = Template("{% load sr %}{% sr 'test1' %}").render(Context())
        self.assertEqual(result, 'Test1')
        result = Template("{% load sr %}{% sr 'test2.test3' %}").render(Context())
        self.assertEqual(result, 'Test3')
        result = Template("{% load sr %}{% sr 'test4.test4' 'testing' 'testing2' %}").render(Context())
        self.assertEqual(result, 'Test4 testing testing2')

    def test_sr_django_jinja_global_function(self):
        result = env.from_string("{{ sr('test1') }}").render()
        self.assertEqual(result, 'Test1')
        result = env.from_string("{{ sr('test2.test3') }}").render()
        self.assertEqual(result, 'Test3')
        result = env.from_string("{{ sr('test4.test4', 'testing', 'testing2') }}").render()
        self.assertEqual(result, 'Test4 testing testing2')
