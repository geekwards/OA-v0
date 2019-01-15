import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Equipment
import test__data

class test_Base_Equip(unittest.TestCase):
    def test_equip_create(self):
        test_equip = Base_Equipment.Equip('','')
        self.assertTrue(test_equip.isempty())

    def test_equip_equal(self):
        self.assertTrue(test__data.test_base_equip1 == test__data.test_base_equip2)

    def test_equip_inequality(self):
        self.assertFalse(test__data.test_base_equip1 == test__data.test_base_equip3)

    def test_equip_clone(self):
        clone = test__data.test_base_equip1.clone()
        self.assertTrue(test__data.test_base_equip1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality2(self):
        clone = test__data.test_base_equip1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality3(self):
        clone = test__data.test_base_equip1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_v_inequality4(self):
        clone = test__data.test_base_equip1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality5(self):
        clone = test__data.test_base_equip1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality6(self):
        clone = test__data.test_base_equip1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality7(self):
        clone = test__data.test_base_equip1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality8(self):
        clone = test__data.test_base_equip1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_inequality9(self):
        clone = test__data.test_base_equip1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_base_equip1 == clone)

    def test_equip_isempty_not(self):
        self.assertFalse(test__data.test_base_equip1.isempty())

    def test_equip_isempty(self):
        self.assertTrue(test__data.test_base_equip_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
