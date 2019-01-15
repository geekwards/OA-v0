import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Object
import test__data

class test_Base_Obj_Set(unittest.TestCase):
    def test_base_obj_create_and_isempty(self):
        test_base_obj_set = Base_Object.Set_of_Items()
        self.assertTrue(test_base_obj_set.isempty())

    def test_base_obj_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_base_obj_set),3)
        self.assertEqual(test__data.test_base_obj_set.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_base_obj_set.get_item('test3').short_description,'testdesc3')

    def test_base_obj_get_list(self):
        self.assertEqual(len(test__data.test_base_obj_set),3)
        self.assertEqual(test__data.test_base_obj_set.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_base_obj_set.list_of_items[1].name,'test1')

    def test_base_obj_update(self):
        self.assertEqual(len(test__data.test_base_obj_set),2)
        self.assertEqual(test__data.test_base_obj_set.all_items[0].name,'test1')
        self.assertEqual(test__data.test_base_obj_set.all_items[1].name,'test3')
        test__data.test_base_obj_set.update(test__data.test_base_obj3)
        self.assertEqual(test__data.test_base_obj_set.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_base_obj_set.all_items[1].short_description,'testdesc3')

    def test_base_obj_update_new(self):
        self.assertEqual(len(test__data.test_base_obj_set),2)
        self.assertEqual(test__data.test_base_obj_set.all_items[0].name,'test1')
        self.assertEqual(test__data.test_base_obj_set.all_items[1].name,'test3')
        test__data.test_base_obj_set.update(test__data.test_base_obj3)
        self.assertEqual(test__data.test_base_obj_set.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_base_obj_set.all_items[1].name,'test3')

    def test_base_obj_remove(self):
        self.assertEqual(len(test__data.test_base_obj_set),3)
        test__data.test_base_obj_set.remove(test__data.test_base_obj2)
        self.assertEqual(len(test__data.test_base_obj_set),2)
        self.assertEqual(test__data.test_base_obj_set.all_items[1].name,'test3')

    def test_base_obj_equals(self):
        self.assertTrue(test__data.test_base_obj_set == test__data.test_base_obj_set2)

    def test_base_obj_notequals(self):
        self.assertFalse(test__data.test_base_obj_set == test__data.test_base_obj_set3)

    def test_base_obj_clone(self):
        clone = test__data.test_base_obj_set.clone()
        self.assertTrue(test__data.test_base_obj_set == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_base_obj_set == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
