import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Clothing
import test__data

class test_Garment(unittest.TestCase):
    def test_garment_create(self):
        test_garment = Clothing.Garment('','')
        self.assertTrue(test_garment.isempty())

    def test_garment_equal(self):
        self.assertTrue(test__data.test_garment1 == test__data.test_garment2)

    def test_garment_inequality(self):
        self.assertFalse(test__data.test_garment1 == test__data.test_garment3)

    def test_garment_clone(self):
        clone = test__data.test_garment1.clone()
        self.assertTrue(test__data.test_garment1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality2(self):
        clone = test__data.test_garment1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality3(self):
        clone = test__data.test_garment1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality4(self):
        clone = test__data.test_garment1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality5(self):
        clone = test__data.test_garment1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality6(self):
        clone = test__data.test_garment1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality7(self):
        clone = test__data.test_garment1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality8(self):
        clone = test__data.test_garment1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_inequality9(self):
        clone = test__data.test_garment1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_garment1 == clone)

    def test_garment_isempty_not(self):
        self.assertFalse(test__data.test_garment1.isempty())

    def test_garment_isempty(self):
        self.assertTrue(test__data.test_garment_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
