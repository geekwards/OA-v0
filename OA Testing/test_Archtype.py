import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype
import test__data

class test_Archtype(unittest.TestCase):
    def test_archtype_create(self):
        test_archtype = Archtype.Archtype('','')
        self.assertTrue(test_archtype.isempty())

    def test_archtype_equal(self):
        self.assertTrue(test__data.test_archtype1 == test__data.test_archtype2)

    def test_archtype_inequality(self):
        self.assertFalse(test__data.test_archtype1 == test__data.test_archtype3)

    def test_archtype_clone(self):
        clone = test__data.test_archtype1.clone()
        self.assertTrue(test__data.test_archtype1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality2(self):
        clone = test__data.test_archtype1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality3(self):
        clone = test__data.test_archtype1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality4(self):
        clone = test__data.test_archtype1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality5(self):
        clone = test__data.test_archtype1.clone()
        clone.proficiency = 'changed prof'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality6(self):
        clone = test__data.test_archtype1.clone()
        clone.str_bonus = 'changed STR'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality7(self):
        clone = test__data.test_archtype1.clone()
        clone.per_bonus = 'changed per'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality8(self):
        clone = test__data.test_archtype1.clone()
        clone.int_bonus = 'changed int'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality9(self):
        clone = test__data.test_archtype1.clone()
        clone.dex_bonus = 'changed dex'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality10(self):
        clone = test__data.test_archtype1.clone()
        clone.cha_bonus = 'changed cha'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality11(self):
        clone = test__data.test_archtype1.clone()
        clone.vit_bonus = 'changed vit'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality12(self):
        clone = test__data.test_archtype1.clone()
        clone.mag_bonus = 'changed mag'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality13(self):
        clone = test__data.test_archtype1.clone()
        clone.stamina_bonus = 'changed stamina'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality14(self):
        clone = test__data.test_archtype1.clone()
        clone.attack_bonus = 'changed attack'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality15(self):
        clone = test__data.test_archtype1.clone()
        clone.reflex_bonus = 'changed reflex'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality16(self):
        clone = test__data.test_archtype1.clone()
        clone.feats = 'changed feats'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality17(self):
        clone = test__data.test_archtype1.clone()
        clone.movement = 'changed movement'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality18(self):
        clone = test__data.test_archtype1.clone()
        clone.skill_points = 'changed skill pts'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_inequality19(self):
        clone = test__data.test_archtype1.clone()
        clone.level_health = 'changed lvl hlth'
        self.assertFalse(test__data.test_archtype1 == clone)

    def test_archtype_isempty_not(self):
        self.assertFalse(test__data.test_archtype1.isempty())

    def test_archtype_isempty(self):
        self.assertTrue(test__data.test_archtype_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
