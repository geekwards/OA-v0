import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Misc_Lists

class test_Manage_Misc_Lists(unittest.TestCase):

    def test_load_misc_lists(self):

        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = Manage_Misc_Lists.get_loaded_set()

        self.assertTrue(len(loaded.get_all())>0)

    def test_save_misc_lists(self):

        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = Manage_Misc_Lists.get_loaded_set()
        num_list = len(loaded.get_all())

        self.assertEqual(loaded[1].name,'Test2')
        clone = loaded[1].clone()

        clone.name = 'MODIFIED TEST'
        Manage_Misc_Lists.save_misc_lists(1,clone)
        loaded2 = Manage_Misc_Lists.get_loaded_set()

        self.assertEqual(loaded2[1].name,'MODIFIED TEST')
        self.assertEqual(len(loaded.get_all()),num_list)

    def test_save_misc_lists_new(self):

        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = Manage_Misc_Lists.get_loaded_set()
        num_list = len(loaded.get_all())

        self.assertEqual(loaded[1].name,'Test2')
        clone = loaded[1].clone()

        clone.name = 'MODIFIED TEST'
        Manage_Misc_Lists.save_num_list(5,clone)
        loaded2 = Manage_Misc_Lists.get_loaded_set()

        self.assertEqual(loaded2[4].name,'Test2')
        self.assertEqual(len(loaded.get_all()),num_list + 1)

    def test_save_misc_lists(self):
        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '2')
        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2')

        loaded = Manage_Misc_Lists.get_loaded_set()
        loaded[0].name = 'updated name 1'
        loaded[1].name = 'updated name 2'
        loaded[2].name = 'updated name 3'
        loaded[3].name = 'updated name 4'

        Manage_Misc_Lists.save_misc_list(0,loaded[0])
        Manage_Misc_Lists.save_misc_list(1,loaded[1])
        Manage_Misc_Lists.save_misc_list(2,loaded[2])
        Manage_Misc_Lists.save_misc_list(3,loaded[3])

        Manage_Misc_Lists.save_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)

        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename + '2')
        loaded2 = Manage_Misc_Lists.get_loaded_set()

        self.assertEqual(loaded2[0].name,'updated name 1')
        self.assertEqual(loaded2[1].name,'updated name 2')
        self.assertEqual(loaded2[2].name,'updated name 3')
        self.assertEqual(loaded2[3].name,'updated name 4')

    def test_remove_misc_list(self):
        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        num_list = len(Manage_Misc_Lists.get_loaded_set().get_all())

        Manage_Misc_Lists.remove_misc_list(1)

        self.assertEqual(len(Manage_Misc_Lists.get_loaded_set().get_all()),num_list - 1)

    def test_launch_edit(self):
        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = Manage_Misc_Lists.launch_edit_misc_list(None,1,True)

        self.assertNotEqual(gui,None)

    def test_launch_list(self):
        Manage_Misc_Lists.load_misc_lists(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = Manage_Misc_Lists.launch_misc_list_list(True)

        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
