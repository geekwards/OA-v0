import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Weapon
import test__data

class test_Weapons(unittest.TestCase):
    def test_weapons_create_and_isempty(self):
        test_weapons = Weapon.Weapons()
        self.assertTrue(test_weapons.isempty())

    def test_weapons_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_weapons),3)
        self.assertEqual(test__data.test_weapons.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_weapons.get_item('test3').short_description,'testdesc3')

    def test_weapons_get_list(self):
        self.assertEqual(len(test__data.test_weapons),3)
        self.assertEqual(test__data.test_weapons.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_weapons.list_of_items[1].name,'test1')

    def test_weapons_update(self):
        self.assertEqual(len(test__data.test_weapons),2)
        self.assertEqual(test__data.test_weapons.all_items[0].name,'test1')
        self.assertEqual(test__data.test_weapons.all_items[1].name,'test3')
        test__data.test_weapons.update(test__data.test_weapon3)
        self.assertEqual(test__data.test_weapons.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_weapons.all_items[1].short_description,'testdesc3')

    def test_weapons_update_new(self):
        self.assertEqual(len(test__data.test_weapons),2)
        self.assertEqual(test__data.test_weapons.all_items[0].name,'test1')
        self.assertEqual(test__data.test_weapons.all_items[1].name,'test3')
        test__data.test_weapons.update(test__data.test_weapon3)
        self.assertEqual(test__data.test_weapons.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_weapons.all_items[1].name,'test3')

    def test_weapons_remove(self):
        self.assertEqual(len(test__data.test_weapons),3)
        test__data.test_weapons.remove(test__data.test_weapon2)
        self.assertEqual(len(test__data.test_weapons),2)
        self.assertEqual(test__data.test_weapons.all_items[1].name,'test3')

    def test_weapons_equals(self):
        self.assertTrue(test__data.test_weapons == test__data.test_weapons2)

    def test_weapons_notequals(self):
        self.assertFalse(test__data.test_weapons == test__data.test_weapons3)

    def test_weapons_clone(self):
        clone = test__data.test_weapons.clone()
        self.assertTrue(test__data.test_weapons == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_weapons == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
