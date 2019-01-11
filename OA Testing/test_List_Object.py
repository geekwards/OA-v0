import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import List_Object
import test__data

class test_List_Object(unittest.TestCase):

    def test_create_list_object(self):
        self.assertEqual(test__data.test_object1.name,'Testing')
        self.assertEqual(test__data.test_object1.short_description,'Test description')

    def test_archtype_equal(self):
        self.assertTrue(test__data.test_object1 == test__data.test_object2)

if __name__ == '__main__':
    unittest.main(verbosity=2)
