import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Race
import test__data

class test_Race(unittest.TestCase):

    def test_race_create(self):
        test_race = Race.Race('')
        self.assertTrue(test_race.isempty())

    def test_race_equal(self):
        self.assertTrue(test__data.test_race1 == test__data.test_race1b)

    def test_race_inequality(self):
        self.assertFalse(test__data.test_race1 == test__data.test_race3)

    def test_race_clone(self):
        clone = test__data.test_race1.clone()
        self.assertTrue(test__data.test_race1 == clone)
        clone.description = 'modified short desc'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality2(self):
        clone = test__data.test_race1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality4(self):
        clone = test__data.test_race1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality6(self):
        clone = test__data.test_race1.clone()
        clone.str_skill_bonus = 'changed STR'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality7(self):
        clone = test__data.test_race1.clone()
        clone.per_skill_bonus = 'changed per'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality8(self):
        clone = test__data.test_race1.clone()
        clone.int_skill_bonus = 'changed int'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality9(self):
        clone = test__data.test_race1.clone()
        clone.dex_skill_bonus = 'changed dex'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality10(self):
        clone = test__data.test_race1.clone()
        clone.cha_skill_bonus = 'changed cha'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality11(self):
        clone = test__data.test_race1.clone()
        clone.vit_skill_bonus = 'changed vit'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality12(self):
        clone = test__data.test_race1.clone()
        clone.mag_skill_bonus = 'changed mag'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality15(self):
        clone = test__data.test_race1.clone()
        clone.reflex_bonus = 'changed reflex'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_inequality16(self):
        clone = test__data.test_race1.clone()
        clone.feats = 'changed feats'
        self.assertFalse(test__data.test_race1 == clone)

    def test_race_isempty_not(self):
        self.assertFalse(test__data.test_race1.isempty())

    def test_race_isempty(self):
        self.assertTrue(test__data.test_race_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
