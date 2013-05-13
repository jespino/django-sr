import unittest
from django.conf import settings
from sr import sr

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        settings.SR = {
            'test1': 'Test1',
            'test2': {
                'test3': 'Test3',
            },
            'test4': {
                'test4': 'Test4 {0} {1}',
            }
        }

    def test_sr_not_valid_key(self):
        self.assertRaisesRegexp(Exception, "Not valid key: not-valid-key.not-valid-subkey", sr, "not-valid-key.not-valid-subkey")
        self.assertRaisesRegexp(Exception, "Not valid key: test1.not-valid-subkey", sr, "test1.not-valid-subkey")
        self.assertRaisesRegexp(Exception, "Not valid key: test2.test3.test4", sr, "test2.test3.test4")

    def test_sr_not_valid_params(self):
        self.assertRaisesRegexp(Exception, "Not valid parameters for key test4.test4", sr, "test4.test4", "param")

    def test_sr_valid_key(self):
        self.assertEqual(sr('test1'), 'Test1')
        self.assertEqual(sr('test2.test3'), 'Test3')
        self.assertEqual(sr('test4.test4', 'testing', 'testing2'), 'Test4 testing testing2')

if __name__ == '__main__':
    unittest.main()
