import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_MiscEquip

class test_Manage_Misc_Equip(unittest.TestCase):
    def test_misc_equip_load_and_get(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        loaded = misc_equip_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_misc_equip_save_update(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        loaded = misc_equip_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshrtdesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        misc_equip_manager.save_one(clone)
        loaded2 = misc_equip_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_Armor)

    def test_misc_equip_save_new(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        loaded = misc_equip_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        misc_equip_manager.save_one(clone)
        loaded2 = misc_equip_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshrtdesc2')
        self.assertEqual(len(loaded2),num_Armor + 1)

    def test_misc_equip_save(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        copy2(app_config.test_file_path + app_config.test_misc_equip_filename,app_config.test_file_path + app_config.test_misc_equip_filename + '2')
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        loaded = misc_equip_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        misc_equip_manager.save_one(loaded.all_items[0])
        misc_equip_manager.save_one(loaded.all_items[1])
        misc_equip_manager.save_one(loaded.all_items[2])
        misc_equip_manager.save_all(app_config.test_file_path + app_config.test_misc_equip_filename + '2',app_config.test_file_path + app_config.test_backup_misc_equip_filename)
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename + '2')
        loaded2 = misc_equip_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_misc_equip_remove(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        num_Armor = len(misc_equip_manager.get_current_set())
        misc_equip_manager.remove_item(misc_equip_manager.get_current_set().all_items[1])
        self.assertEqual(len(misc_equip_manager.get_current_set()),num_Armor - 1)

    def test_misc_equip_launch_edit(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        gui = misc_equip_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_misc_equip_launch_list(self):
        misc_equip_manager = Manage_MiscEquip.Manage_misc_equipment()
        misc_equip_manager.load_set(app_config.test_file_path + app_config.test_misc_equip_filename)
        gui = misc_equip_manager.launch_list('Armor',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
