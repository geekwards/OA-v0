import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Clothing

class test_Manage_Clothing(unittest.TestCase):
    def test_clothing_load_and_get(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        loaded = clothing_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_clothing_save_update(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        loaded = clothing_manager.get_current_set().clone()
        num_clothing = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshrtdesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        clothing_manager.save_one(clone)
        loaded2 = clothing_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'Test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_clothing)

    def test_clothing_save_new(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        loaded = clothing_manager.get_current_set().clone()
        num_clothing = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'Test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        clothing_manager.save_one(clone)
        loaded2 = clothing_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshrtdesc2')
        self.assertEqual(len(loaded2),num_clothing + 1)

    def test_clothing_save(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        copy2(app_config.test_file_path + app_config.test_clothing_filename,app_config.test_file_path + app_config.test_clothing_filename + '2')
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        loaded = clothing_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        clothing_manager.save_one(loaded.all_items[0])
        clothing_manager.save_one(loaded.all_items[1])
        clothing_manager.save_one(loaded.all_items[2])
        clothing_manager.save_all(app_config.test_file_path + app_config.test_clothing_filename + '2',app_config.test_file_path + app_config.test_backup_clothing_filename)
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename + '2')
        loaded2 = clothing_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_clothing_remove(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        num_clothing = len(clothing_manager.get_current_set())
        clothing_manager.remove_item(clothing_manager.get_current_set().all_items[1])
        self.assertEqual(len(clothing_manager.get_current_set()),num_clothing - 1)

    def test_clothing_launch_edit(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        gui = clothing_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_clothing_launch_list(self):
        clothing_manager = Manage_Clothing.Manage_clothing()
        clothing_manager.load_set(app_config.test_file_path + app_config.test_clothing_filename)
        gui = clothing_manager.launch_list('Clothing',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
