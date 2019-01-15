import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_Equipment
import test__data

class test_Misc_Equipment(unittest.TestCase):
    def test_misc_equipment_create_and_isempty(self):
        test_misc_equipment = Misc_Equipment.Misc_equipment()
        self.assertTrue(test_misc_equipment.isempty())

    def test_misc_equipment_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_misc_equipment),3)
        self.assertEqual(test__data.test_misc_equipment.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_misc_equipment.get_item('test3').short_description,'testdesc3')

    def test_misc_equipment_get_list(self):
        self.assertEqual(len(test__data.test_misc_equipment),3)
        self.assertEqual(test__data.test_misc_equipment.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_misc_equipment.list_of_items[1].name,'test1')

    def test_misc_equipment_update(self):
        self.assertEqual(len(test__data.test_misc_equipment),2)
        self.assertEqual(test__data.test_misc_equipment.all_items[0].name,'test1')
        self.assertEqual(test__data.test_misc_equipment.all_items[1].name,'test3')
        test__data.test_misc_equipment.update(test__data.test_misc_equip3)
        self.assertEqual(test__data.test_misc_equipment.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_misc_equipment.all_items[1].short_description,'testdesc3')

    def test_misc_equipment_update_new(self):
        self.assertEqual(len(test__data.test_misc_equipment),2)
        self.assertEqual(test__data.test_misc_equipment.all_items[0].name,'test1')
        self.assertEqual(test__data.test_misc_equipment.all_items[1].name,'test3')
        test__data.test_misc_equipment.update(test__data.test_misc_equip3)
        self.assertEqual(test__data.test_misc_equipment.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_misc_equipment.all_items[1].name,'test3')

    def test_misc_equipment_remove(self):
        self.assertEqual(len(test__data.test_misc_equipment),3)
        test__data.test_misc_equipment.remove(test__data.test_misc_equip2)
        self.assertEqual(len(test__data.test_misc_equipment),2)
        self.assertEqual(test__data.test_misc_equipment.all_items[1].name,'test3')

    def test_misc_equipment_equals(self):
        self.assertTrue(test__data.test_misc_equipment == test__data.test_misc_equipment2)

    def test_misc_equipment_notequals(self):
        self.assertFalse(test__data.test_misc_equipment == test__data.test_misc_equipment3)

    def test_misc_equipment_clone(self):
        clone = test__data.test_misc_equipment.clone()
        self.assertTrue(test__data.test_misc_equipment == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_misc_equipment == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
