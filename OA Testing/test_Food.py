import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Food
import test__data

class test_Food(unittest.TestCase):
    def test_food_create(self):
        test_food = Food.Food('','')
        self.assertTrue(test_food.isempty())

    def test_food_equal(self):
        self.assertTrue(test__data.test_food1 == test__data.test_food2)

    def test_food_inequality(self):
        self.assertFalse(test__data.test_food1 == test__data.test_food3)

    def test_food_clone(self):
        clone = test__data.test_food1.clone()
        self.assertTrue(test__data.test_food1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality2(self):
        clone = test__data.test_food1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality3(self):
        clone = test__data.test_food1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality4(self):
        clone = test__data.test_food1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality5(self):
        clone = test__data.test_food1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality6(self):
        clone = test__data.test_food1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality7(self):
        clone = test__data.test_food1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality8(self):
        clone = test__data.test_food1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_inequality9(self):
        clone = test__data.test_food1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_food1 == clone)

    def test_food_isempty_not(self):
        self.assertFalse(test__data.test_food1.isempty())

    def test_food_isempty(self):
        self.assertTrue(test__data.test_food_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
