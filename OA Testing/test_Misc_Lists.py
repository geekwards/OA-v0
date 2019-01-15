import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List
import test__data

class test_Misc_Lists(unittest.TestCase):

    def test_misc_list_create_and_isempty(self):
        test_misc_lists = Misc_List.Misc_lists()

        self.assertTrue(test_misc_lists.isempty())

    def test_misc_list_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_misc_lists1),4)
        self.assertEqual(test__data.test_misc_lists1.all_items[0].name,'Test1')
        self.assertEqual(test__data.test_misc_lists1.all_items[1].name,'Test2')
        self.assertEqual(test__data.test_misc_lists1.get_item('Test1').name,'Test1')
        self.assertEqual(test__data.test_misc_lists1.get_item('Test2').name,'Test2')
        self.assertEqual(test__data.test_misc_lists1.get_item('Test1').all_items[0].name,'Testlist 1.1')

    def test_misc_list_update(self):
        self.assertEqual(len(test__data.test_misc_lists1),3)
        self.assertEqual(test__data.test_misc_lists1.all_items[0].name,'Test1')
        self.assertEqual(test__data.test_misc_lists1.all_items[1].name,'Test2')
        test__data.test_misc_lists1.update(test__data.test_misc_list3)
        self.assertEqual(test__data.test_misc_lists1.all_items[1].all_items[0].name,'Testlist 3.1')
        self.assertEqual(test__data.test_misc_lists1.all_items[1].all_items[2].name,'Testlist 3.3')

    def test_misc_list_get_list_item_fail(self):
        self.assertEqual(len(test__data.test_misc_lists1),4)
        self.assertEqual(test__data.test_misc_lists1.all_items[0].name,'Test1')
        self.assertEqual(test__data.test_misc_lists1.all_items[1].name,'Test2')
        test__data.test_misc_lists1.update(test__data.test_misc_list3)
        self.assertEqual(test__data.test_misc_lists1.all_items[1].name,'Test2')
        self.assertEqual(test__data.test_misc_lists1.list_of_items[1].name,'Test2')
        self.assertEqual(test__data.test_misc_lists1.all_items[2].name,'Test2')
        self.assertEqual(test__data.test_misc_lists1.list_of_items[2].name,'Test2')

    def test_misc_list_remove(self):
        self.assertTrue(len(test__data.test_misc_lists1),4)
        test__data.test_misc_lists1.remove(test__data.test_misc_list2)
        self.assertEqual(len(test__data.test_misc_lists1),3)
        self.assertEqual(test__data.test_misc_lists1.get_item('Test3').name,'Test3')

    def test_misc_list_equals(self):
        self.assertTrue(test__data.test_misc_lists1 == test__data.test_misc_lists2)

    def test_misc_list_notequals(self): 
        self.assertFalse(test__data.test_misc_lists1 == test__data.test_misc_lists3)

    def test_misc_list_clone(self):
        clone = test__data.test_misc_lists1.clone()
        self.assertTrue(clone == test__data.test_misc_lists1)
        clone.all_items[1].all_items[1].name = 'modified'
        self.assertFalse(clone == test__data.test_misc_lists1)

if __name__ == '__main__':
    unittest.main(verbosity=2)
