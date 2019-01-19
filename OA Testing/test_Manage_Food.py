import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Food

class test_Manage_Food(unittest.TestCase):
    def test_food_load_and_get(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_food_save_update(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshrdesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        food_manager.save_one(clone)
        loaded2 = food_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_Armor)

    def test_food_save_new(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set().clone()
        num_Armor = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        food_manager.save_one(clone)
        loaded2 = food_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshrdesc2')
        self.assertEqual(len(loaded2),num_Armor + 1)

    def test_food_save(self):
        food_manager = Manage_Food.Manage_food()
        copy2(app_config.test_file_path + app_config.test_food_filename,app_config.test_file_path + app_config.test_food_filename + '2')
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        food_manager.save_one(loaded.all_items[0])
        food_manager.save_one(loaded.all_items[1])
        food_manager.save_one(loaded.all_items[2])
        food_manager.save_all(app_config.test_file_path + app_config.test_food_filename + '2',app_config.test_file_path + app_config.test_backup_food_filename)
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename + '2')
        loaded2 = food_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_food_remove(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        num_Armor = len(food_manager.get_current_set())
        food_manager.remove_item(food_manager.get_current_set().all_items[1])
        self.assertEqual(len(food_manager.get_current_set()),num_Armor - 1)

    def test_food_launch_edit(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_food_launch_list(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_list('Armor',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
