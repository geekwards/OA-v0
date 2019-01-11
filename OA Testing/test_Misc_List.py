import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List
import test__data
import List_Object


class test_Misc_List(unittest.TestCase):

    def test_create_misc_list(self):
        self.assertEqual(len(test__data.test_misc_list1),3)
        self.assertEqual(test__data.test_misc_list1.name,'Test1')
        self.assertTrue(test__data.test_misc_list1.all_items[0],'Testlist 1.1')
        self.assertTrue(test__data.test_misc_list1.all_items[1],'Testlist 1.2')
        self.assertTrue(test__data.test_misc_list1.all_items[2],'Testlist 1.3')

    def test_misc_list_equals(self):
        self.assertTrue(test__data.test_misc_list1 == test__data.test_misc_list1b)

    def test_misc_list_unequal(self):
        self.assertFalse(test__data.test_misc_list1 == test__data.test_misc_list2)

    def test_misc_list_clone(self):
        clone = test__data.test_misc_list1.clone()
        self.assertTrue(test__data.test_misc_list1 == clone)

        clone.all_items[1].name = 'MODIFIED'
        self.assertFalse(test__data.test_misc_list1 == clone)

    def test_misc_list_add_new(self):
        test__data.test_misc_list2.add_new(List_Object.List_object('Testlist 2.4',''))
        self.assertTrue(test__data.test_misc_list2.all_items[0],'Testlist 2.1')
        self.assertTrue(test__data.test_misc_list2.all_items[1],'Testlist 2.2')
        self.assertTrue(test__data.test_misc_list2.all_items[2],'Testlist 2.3')
        self.assertTrue(test__data.test_misc_list2.all_items[3],'Testlist 2.4')

    def test_misc_list_remove(self):
        test__data.test_misc_list1.remove(test__data.test_misc_list1.all_items[1])
        self.assertTrue(test__data.test_misc_list1.all_items[0],'Testlist 1.1')
        self.assertTrue(test__data.test_misc_list1.all_items[1],'Testlist 1.3')

if __name__ == '__main__':
    unittest.main(verbosity=2)
