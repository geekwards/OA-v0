import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype

test_archtype = Archtype.Archtype('test','testdesc')
test_archtype.description = "This is a test description."
test_archtype.proficiency = "Test proficiency"
test_archtype.str_bonus = 0
test_archtype.per_bonus = 1
test_archtype.int_bonus = 2
test_archtype.dex_bonus = 3
test_archtype.cha_bonus = 4
test_archtype.vit_bonus = 5
test_archtype.mag_bonus = 6
test_archtype.stamina_bonus = 7
test_archtype.attack_bonus = 8
test_archtype.reflex_bonus = 9
test_archtype.feats = 10
test_archtype.movement = 11
test_archtype.skill_points = 12
test_archtype.level_health = "more health"

class test_Archtype(unittest.TestCase):

    def test_archtype_create(self):
        test_archtype = Archtype.Archtype('','')

        self.assertTrue(test_archtype.isempty())

    def test_archtype_equal(self):
        test_archtype2 = Archtype.Archtype('test','testdesc')
        test_archtype2.description = "This is a test description."
        test_archtype2.proficiency = "Test proficiency"
        test_archtype2.str_bonus = 0
        test_archtype2.per_bonus = 1
        test_archtype2.int_bonus = 2
        test_archtype2.dex_bonus = 3
        test_archtype2.cha_bonus = 4
        test_archtype2.vit_bonus = 5
        test_archtype2.mag_bonus = 6
        test_archtype2.stamina_bonus = 7
        test_archtype2.attack_bonus = 8
        test_archtype2.reflex_bonus = 9
        test_archtype2.feats = 10
        test_archtype2.movement = 11
        test_archtype2.skill_points = 12
        test_archtype2.level_health = "more health"

        self.assertTrue(test_archtype.equals(test_archtype2))

    def test_archtype_inequality(self):
        test_archtype2 = Archtype.Archtype('','')

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_clone(self):
        test_archtype2 = test_archtype.clone()

        self.assertTrue(test_archtype.equals(test_archtype2))

    def test_archtype_inequality2(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.name = 'changed name'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality2(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.name = 'changed name'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality3(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.short_description = 'changed shortdesc'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality4(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.description = 'changed desc'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality5(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.proficiency = 'changed prof'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality6(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.str_bonus = 'changed STR'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality7(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.per_bonus = 'changed per'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality8(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.int_bonus = 'changed int'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality9(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.dex_bonus = 'changed dex'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality10(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.cha_bonus = 'changed cha'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality11(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.vit_bonus = 'changed vit'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality12(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.mag_bonus = 'changed mag'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality13(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.stamina_bonus = 'changed stamina'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality14(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.attack_bonus = 'changed attack'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality15(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.reflex_bonus = 'changed reflex'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality16(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.feats = 'changed feats'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality17(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.movement = 'changed movement'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality18(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.skill_points = 'changed skill pts'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_inequality19(self):
        test_archtype2 = test_archtype.clone()
        test_archtype2.level_health = 'changed lvl hlth'

        self.assertFalse(test_archtype.equals(test_archtype2))

    def test_archtype_isempty_not(self):
        self.assertFalse(test_archtype.isempty())

    def test_archtype_isempty(self):
        test_archtype = Archtype.Archtype('','')

        self.assertTrue(test_archtype.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
