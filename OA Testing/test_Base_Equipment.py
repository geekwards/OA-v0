import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Equipment
import test__data

class test_Base_equipment(unittest.TestCase):
    def test_equip_create_and_isempty(self):
        test_base_equipment = Base_Equipment.Base_equipment()
        self.assertTrue(test_base_equipment.isempty())

    def test_equip_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_base_equipment),3)
        self.assertEqual(test__data.test_base_equipment.get_item('test1').short_description,'testshortdesc1')
        self.assertEqual(test__data.test_base_equipment.get_item('test3').short_description,'testshortdesc3')

    def test_equip_get_list(self):
        self.assertEqual(len(test__data.test_base_equipment),3)
        self.assertEqual(test__data.test_base_equipment.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_base_equipment.list_of_items[1].name,'test1')

    def test_equip_update(self):
        self.assertEqual(len(test__data.test_base_equipment),2)
        self.assertEqual(test__data.test_base_equipment.all_items[0].name,'test1')
        self.assertEqual(test__data.test_base_equipment.all_items[1].name,'test3')
        test__data.test_base_equipment.update(test__data.test_base_equip3)
        self.assertEqual(test__data.test_base_equipment.list_of_items[1].short_description,'testshortdesc3')
        self.assertEqual(test__data.test_base_equipment.all_items[1].short_description,'testshortdesc3')

    def test_equip_update_new(self):
        self.assertEqual(len(test__data.test_base_equipment),2)
        self.assertEqual(test__data.test_base_equipment.all_items[0].name,'test1')
        self.assertEqual(test__data.test_base_equipment.all_items[1].name,'test3')
        test__data.test_base_equipment.update(test__data.test_base_equip3)
        self.assertEqual(test__data.test_base_equipment.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_base_equipment.all_items[1].name,'test3')

    def test_equip_remove(self):
        self.assertEqual(len(test__data.test_base_equipment),3)
        test__data.test_base_equipment.remove(test__data.test_base_equip2)
        self.assertEqual(len(test__data.test_base_equipment),2)
        self.assertEqual(test__data.test_base_equipment.all_items[1].name,'test3')

    def test_equip_equals(self):
        self.assertTrue(test__data.test_base_equipment == test__data.test_base_equipment2)

    def test_equip_notequals(self):
        self.assertFalse(test__data.test_base_equipment == test__data.test_base_equipment3)

    def test_equip_clone(self):
        clone = test__data.test_base_equipment.clone()
        self.assertTrue(test__data.test_base_equipment == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_base_equipment == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
