import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Weapon
import test__data

class test_Weapon(unittest.TestCase):
    def test_weapon_create(self):
        test_weapon = Weapon.Weapon('','')
        self.assertTrue(test_weapon.isempty())

    def test_weapon_equal(self):
        self.assertTrue(test__data.test_weapon1 == test__data.test_weapon2)

    def test_weapon_inequality(self):
        self.assertFalse(test__data.test_weapon1 == test__data.test_weapon3)

    def test_weapon_clone(self):
        clone = test__data.test_weapon1.clone()
        self.assertTrue(test__data.test_weapon1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality2(self):
        clone = test__data.test_weapon1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality3(self):
        clone = test__data.test_weapon1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality4(self):
        clone = test__data.test_weapon1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality5(self):
        clone = test__data.test_weapon1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality6(self):
        clone = test__data.test_weapon1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality7(self):
        clone = test__data.test_weapon1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality8(self):
        clone = test__data.test_weapon1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_inequality9(self):
        clone = test__data.test_weapon1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_weapon1 == clone)

    def test_weapon_isempty_not(self):
        self.assertFalse(test__data.test_weapon1.isempty())

    def test_weapon_isempty(self):
        self.assertTrue(test__data.test_weapon_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
