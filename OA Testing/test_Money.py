import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Money
import test__data

class test_Money(unittest.TestCase):
    def test_money_create(self):
        test_money = Money.Money('','')
        self.assertTrue(test_money.isempty())

    def test_money_equal(self):
        self.assertTrue(test__data.test_money1 == test__data.test_money2)

    def test_money_inequality(self):
        self.assertFalse(test__data.test_money1 == test__data.test_money3)

    def test_money_clone(self):
        clone = test__data.test_money1.clone()
        self.assertTrue(test__data.test_money1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality2(self):
        clone = test__data.test_money1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality3(self):
        clone = test__data.test_money1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality4(self):
        clone = test__data.test_money1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality5(self):
        clone = test__data.test_money1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality6(self):
        clone = test__data.test_money1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality7(self):
        clone = test__data.test_money1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality8(self):
        clone = test__data.test_money1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_inequality9(self):
        clone = test__data.test_money1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_money1 == clone)

    def test_money_isempty_not(self):
        self.assertFalse(test__data.test_money1.isempty())

    def test_money_isempty(self):
        self.assertTrue(test__data.test_money_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
