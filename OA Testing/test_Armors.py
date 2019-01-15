import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Armor
import test__data

class test_Armors(unittest.TestCase):
    def test_armors_create_and_isempty(self):
        test_armors = Armor.Armors()
        self.assertTrue(test_armors.isempty())

    def test_armors_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_armors),3)
        self.assertEqual(test__data.test_armors.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_armors.get_item('test3').short_description,'testdesc3')

    def test_armors_get_list(self):
        self.assertEqual(len(test__data.test_armors),3)
        self.assertEqual(test__data.test_armors.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_armors.list_of_items[1].name,'test1')

    def test_armors_update(self):
        self.assertEqual(len(test__data.test_armors),2)
        self.assertEqual(test__data.test_armors.all_items[0].name,'test1')
        self.assertEqual(test__data.test_armors.all_items[1].name,'test3')
        test__data.test_armors.update(test__data.test_armor3)
        self.assertEqual(test__data.test_armors.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_armors.all_items[1].short_description,'testdesc3')

    def test_armors_update_new(self):
        self.assertEqual(len(test__data.test_armors),2)
        self.assertEqual(test__data.test_armors.all_items[0].name,'test1')
        self.assertEqual(test__data.test_armors.all_items[1].name,'test3')
        test__data.test_armors.update(test__data.test_armor3)
        self.assertEqual(test__data.test_armors.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_armors.all_items[1].name,'test3')

    def test_armors_remove(self):
        self.assertEqual(len(test__data.test_armors),3)
        test__data.test_armors.remove(test__data.test_armor2)
        self.assertEqual(len(test__data.test_armors),2)
        self.assertEqual(test__data.test_armors.all_items[1].name,'test3')

    def test_armors_equals(self):
        self.assertTrue(test__data.test_armors == test__data.test_armors2)

    def test_armors_notequals(self):
        self.assertFalse(test__data.test_armors == test__data.test_armors3)

    def test_armors_clone(self):
        clone = test__data.test_armors.clone()
        self.assertTrue(test__data.test_armors == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_armors == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
