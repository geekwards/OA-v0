import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Misc_Lists
import List_Object

class test_Manage_Misc_Lists(unittest.TestCase):

    def test_misc_lists_load_and_get(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misc_manager.get_current_set()

        self.assertTrue(len(loaded)>0)

    def test_misc_list_save_modify(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misc_manager.get_current_set()
        num_list = len(loaded)

        self.assertEqual(loaded.all_items[1].all_items[0].name,'Item2-1')
        clone = loaded.all_items[1].clone()

        clone.all_items[0] = List_Object.List_object('MODIFIED TEST','')
        misc_manager.save_misc_list(clone)
        loaded2 = misc_manager.get_current_set()

        self.assertEqual(loaded2.all_items[1].all_items[0].name,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_list)

    def test_misc_list_save_new(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misc_manager.get_current_set()
        num_list = len(loaded)

        self.assertEqual(loaded.all_items[1].name,'List2')
        clone = loaded.all_items[1].clone()

        clone.name = 'MODIFIED TEST'
        misc_manager.save_misc_list(clone)
        loaded2 = misc_manager.get_current_set()

        self.assertEqual(loaded2.all_items[5].name,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_list + 1)

    def test_misc_lists_save(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '2')
        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2')

        loaded = misc_manager.get_current_set()
        loaded.all_items[0].name = 'updated name 1'
        loaded.all_items[1].name = 'updated name 2'
        loaded.all_items[2].name = 'updated name 3'
        loaded.all_items[3].name = 'updated name 4'

        misc_manager.save_misc_list(loaded.all_items[0])
        misc_manager.save_misc_list(loaded.all_items[1])
        misc_manager.save_misc_list(loaded.all_items[2])
        misc_manager.save_misc_list(loaded.all_items[3])

        misc_manager.save_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2')
        loaded2 = misc_manager.get_current_set()

        self.assertEqual(loaded2.all_items[0].name,'updated name 1')
        self.assertEqual(loaded2.all_items[1].name,'updated name 2')
        self.assertEqual(loaded2.all_items[2].name,'updated name 3')
        self.assertEqual(loaded2.all_items[3].name,'updated name 4')

    def test_misc_list_remove(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        num_list = len(misc_manager.get_current_set())

        misc_manager.remove_misc_list(misc_manager.get_current_set().all_items[1])

        self.assertEqual(len(misc_manager.get_current_set()),num_list - 1)

    def test_misc_list_launch_edit(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misc_manager.launch_edit_misc_list(None,misc_manager.get_current_set().all_items[1].name,True)

        self.assertNotEqual(gui,None)

    def test_misc_lists_launch_list(self):
        misc_manager = Manage_Misc_Lists.Manage_misc_lists()

        misc_manager.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misc_manager.launch_misc_list_list(True)

        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
