import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Weapons

class test_Manage_Weapons(unittest.TestCase):
    def test_weapons_load_and_get(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        loaded = weapons_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_weapons_save_update(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        loaded = weapons_manager.get_current_set().clone()
        num_weap = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdescr2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        weapons_manager.save_one(clone)
        loaded2 = weapons_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_weap)

    def test_weapons_save_new(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        loaded = weapons_manager.get_current_set().clone()
        num_weap = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        weapons_manager.save_one(clone)
        loaded2 = weapons_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshortdescr2')
        self.assertEqual(len(loaded2),num_weap + 1)

    def test_weapons_save(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        copy2(app_config.test_file_path + app_config.test_weapons_filename,app_config.test_file_path + app_config.test_weapons_filename + '2')
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        loaded = weapons_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        weapons_manager.save_one(loaded.all_items[0])
        weapons_manager.save_one(loaded.all_items[1])
        weapons_manager.save_one(loaded.all_items[2])
        weapons_manager.save_all(app_config.test_file_path + app_config.test_weapons_filename + '2',app_config.test_file_path + app_config.test_backup_weapons_filename)
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename + '2')
        loaded2 = weapons_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_weapons_remove(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        num_weap = len(weapons_manager.get_current_set())
        weapons_manager.remove_item(weapons_manager.get_current_set().all_items[1])
        self.assertEqual(len(weapons_manager.get_current_set()),num_weap - 1)

    def test_weapons_launch_edit(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        gui = weapons_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_weapons_launch_list(self):
        weapons_manager = Manage_Weapons.Manage_weapons()
        weapons_manager.load_set(app_config.test_file_path + app_config.test_weapons_filename)
        gui = weapons_manager.launch_list('Money',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
