import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Armor
import test__data

class test_Armor(unittest.TestCase):
    def test_armor_create(self):
        test_armor = Armor.Armor('','')
        self.assertTrue(test_armor.isempty())

    def test_armor_equal(self):
        self.assertTrue(test__data.test_armor1 == test__data.test_armor2)

    def test_armor_inequality(self):
        self.assertFalse(test__data.test_armor1 == test__data.test_armor3)

    def test_armor_clone(self):
        clone = test__data.test_armor1.clone()
        self.assertTrue(test__data.test_armor1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality2(self):
        clone = test__data.test_armor1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality3(self):
        clone = test__data.test_armor1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality4(self):
        clone = test__data.test_armor1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality5(self):
        clone = test__data.test_armor1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality6(self):
        clone = test__data.test_armor1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality7(self):
        clone = test__data.test_armor1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality8(self):
        clone = test__data.test_armor1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_inequality9(self):
        clone = test__data.test_armor1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_armor1 == clone)

    def test_armor_isempty_not(self):
        self.assertFalse(test__data.test_armor1.isempty())

    def test_armor_isempty(self):
        self.assertTrue(test__data.test_armor_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
