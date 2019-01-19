import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Armor

class test_Manage_Armor(unittest.TestCase):
    def test_armor_load_and_get(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_armor_save_update(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshrtdesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        armor_manager.save_one(clone)
        loaded2 = armor_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_Armor)

    def test_armor_save_new(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        armor_manager.save_one(clone)
        loaded2 = armor_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshrtdesc2')
        self.assertEqual(len(loaded2),num_Armor + 1)

    def test_armor_save(self):
        armor_manager = Manage_Armor.Manage_armor()
        copy2(app_config.test_file_path + app_config.test_armor_filename,app_config.test_file_path + app_config.test_armor_filename + '2')
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        armor_manager.save_one(loaded.all_items[0])
        armor_manager.save_one(loaded.all_items[1])
        armor_manager.save_one(loaded.all_items[2])
        armor_manager.save_all(app_config.test_file_path + app_config.test_armor_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename + '2')
        loaded2 = armor_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_armor_remove(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        num_Armor = len(armor_manager.get_current_set())
        armor_manager.remove_item(armor_manager.get_current_set().all_items[1])
        self.assertEqual(len(armor_manager.get_current_set()),num_Armor - 1)

    def test_armor_launch_edit(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_armor_launch_list(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_list('Armor',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
