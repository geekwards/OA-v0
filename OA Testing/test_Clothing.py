import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Clothing
import test__data

class test_Clothing(unittest.TestCase):
    def test_clothing_create_and_isempty(self):
        test_clothing = Clothing.Clothing()
        self.assertTrue(test_clothing.isempty())

    def test_clothing_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_clothing),3)
        self.assertEqual(test__data.test_clothing.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_clothing.get_item('test3').short_description,'testdesc3')

    def test_clothing_get_list(self):
        self.assertEqual(len(test__data.test_clothing),3)
        self.assertEqual(test__data.test_clothing.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_clothing.list_of_items[1].name,'test1')

    def test_clothing_update(self):
        self.assertEqual(len(test__data.test_clothing),2)
        self.assertEqual(test__data.test_clothing.all_items[0].name,'test1')
        self.assertEqual(test__data.test_clothing.all_items[1].name,'test3')
        test__data.test_clothing.update(test__data.test_garment3)
        self.assertEqual(test__data.test_clothing.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_clothing.all_items[1].short_description,'testdesc3')

    def test_clothing_update_new(self):
        self.assertEqual(len(test__data.test_clothing),2)
        self.assertEqual(test__data.test_clothing.all_items[0].name,'test1')
        self.assertEqual(test__data.test_clothing.all_items[1].name,'test3')
        test__data.test_clothing.update(test__data.test_garment3)
        self.assertEqual(test__data.test_clothing.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_clothing.all_items[1].name,'test3')

    def test_clothing_remove(self):
        self.assertEqual(len(test__data.test_clothing),3)
        test__data.test_clothing.remove(test__data.test_garment2)
        self.assertEqual(len(test__data.test_clothing),2)
        self.assertEqual(test__data.test_clothing.all_items[1].name,'test3')

    def test_clothing_equals(self):
        self.assertTrue(test__data.test_clothing == test__data.test_clothing2)

    def test_clothing_notequals(self):
        self.assertFalse(test__data.test_clothing == test__data.test_clothing3)

    def test_clothing_clone(self):
        clone = test__data.test_clothing.clone()
        self.assertTrue(test__data.test_clothing == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_clothing == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
