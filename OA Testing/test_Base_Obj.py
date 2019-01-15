import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Object
import test__data

class test_Base_Object(unittest.TestCase):

    def test_base_obj_create(self):
        test_base_obj = Base_Object.Item('','')
        self.assertTrue(test_base_obj.isempty())

    def test_base_obj_equal(self):
        self.assertTrue(test__data.test_base_obj1 == test__data.test_base_obj2)

    def test_base_obj_inequality(self):
        self.assertFalse(test__data.test_base_obj1 == test__data.test_base_obj3)

    def test_base_obj_clone(self):
        clone = test__data.test_base_obj1.clone()
        self.assertTrue(test__data.test_base_obj1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_base_obj1 == clone)

    def test_base_obj_inequality2(self):
        clone = test__data.test_base_obj1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_base_obj1 == clone)

    def test_base_obj_inequality3(self):
        clone = test__data.test_base_obj1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_base_obj1 == clone)

    def test_base_obj_isempty_not(self):
        self.assertFalse(test__data.test_base_obj1.isempty())

    def test_base_obj_isempty(self):
        self.assertTrue(test__data.test_base_obj_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
