import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List


class test_Misc_List(unittest.TestCase):

    def test_create_Misc_List(self):
        test_object = Misc_List.Misclist('Testing')

        self.assertEqual(test_object.name,'Testing')

    def test_archtype_equal(self):
        test_object = Misc_List.Misclist('Testing')
        test_object2 = Misc_List.Misclist('Testing')

        self.assertTrue(test_object.equals(test_object2))
 

    def test_archtype_clone(self):
        test_object = Misc_List.Misclist('Testing')
        test_object2 = test_object.clone()

        self.assertTrue(test_object.equals(test_object2))

    def test_archtype_add_new(self):
        self.assertTrue(False)

    def test_archtype_remove(self):
        self.assertTrue(False)

if __name__ == '__main__':
    unittest.main(verbosity=2)
