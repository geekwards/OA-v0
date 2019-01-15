import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Food
import test__data

class test_Foods(unittest.TestCase):
    def test_food_create_and_isempty(self):
        test_foods = Food.Foods()
        self.assertTrue(test_foods.isempty())

    def test_food_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_foods),3)
        self.assertEqual(test__data.test_foods.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_foods.get_item('test3').short_description,'testdesc3')

    def test_food_get_list(self):
        self.assertEqual(len(test__data.test_foods),3)
        self.assertEqual(test__data.test_foods.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_foods.list_of_items[1].name,'test1')

    def test_food_update(self):
        self.assertEqual(len(test__data.test_foods),2)
        self.assertEqual(test__data.test_foods.all_items[0].name,'test1')
        self.assertEqual(test__data.test_foods.all_items[1].name,'test3')
        test__data.test_foods.update(test__data.test_food3)
        self.assertEqual(test__data.test_foods.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_foods.all_items[1].short_description,'testdesc3')

    def test_food_update_new(self):
        self.assertEqual(len(test__data.test_foods),2)
        self.assertEqual(test__data.test_foods.all_items[0].name,'test1')
        self.assertEqual(test__data.test_foods.all_items[1].name,'test3')
        test__data.test_foods.update(test__data.test_food3)
        self.assertEqual(test__data.test_foods.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_foods.all_items[1].name,'test3')

    def test_food_remove(self):
        self.assertEqual(len(test__data.test_foods),3)
        test__data.test_foods.remove(test__data.test_food2)
        self.assertEqual(len(test__data.test_foods),2)
        self.assertEqual(test__data.test_foods.all_items[1].name,'test3')

    def test_food_equals(self):
        self.assertTrue(test__data.test_foods == test__data.test_foods2)

    def test_food_notequals(self):
        self.assertFalse(test__data.test_foods == test__data.test_foods3)

    def test_food_clone(self):
        clone = test__data.test_foods.clone()
        self.assertTrue(test__data.test_foods == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_foods == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
