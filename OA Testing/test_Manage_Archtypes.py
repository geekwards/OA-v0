import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Archtypes

class test_Manage_Archtypes(unittest.TestCase):

    def test_load_archtypes(self):

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        loaded = Manage_Archtypes.get_loaded_set()

        self.assertTrue(len(loaded.get_all())>0)

    def test_save_archtype(self):

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        loaded = Manage_Archtypes.get_loaded_set()
        num_Arch = len(loaded.get_all())

        self.assertEqual(loaded[1].short_description,'TestShortDesc2')
        clone = loaded[1].clone()

        clone.short_description = 'MODIFIED TEST'
        Manage_Archtypes.save_archtype(1,clone)
        loaded2 = Manage_Archtypes.get_loaded_set()

        self.assertEqual(loaded2[1].name,'Test2')
        self.assertEqual(loaded2[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded.get_all()),num_Arch)

    def test_save_archtype_new(self):

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        loaded = Manage_Archtypes.get_loaded_set()
        num_Arch = len(loaded.get_all())

        self.assertEqual(loaded[1].short_description,'TestShortDesc2')
        clone = loaded[1].clone()

        clone.short_description = 'MODIFIED TEST'
        Manage_Archtypes.save_archtype(5,clone)
        loaded2 = Manage_Archtypes.get_loaded_set()

        self.assertEqual(loaded2[4].name,'Test2')
        self.assertEqual(loaded2[4].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded.get_all()),num_Arch + 1)

    def test_save_archtypes(self):
        copy2(app_config.test_file_path + app_config.test_filename,app_config.test_file_path + app_config.test_filename + '2')
        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename + '2')

        loaded = Manage_Archtypes.get_loaded_set()
        loaded[0].name = 'updated name 1'
        loaded[1].name = 'updated name 2'
        loaded[2].name = 'updated name 3'
        loaded[3].name = 'updated name 4'

        Manage_Archtypes.save_archtype(0,loaded[0])
        Manage_Archtypes.save_archtype(1,loaded[1])
        Manage_Archtypes.save_archtype(2,loaded[2])
        Manage_Archtypes.save_archtype(3,loaded[3])

        Manage_Archtypes.save_archtypes(app_config.test_file_path + app_config.test_filename + '2',app_config.test_file_path + app_config.test_backup_filename)

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename + '2')
        loaded2 = Manage_Archtypes.get_loaded_set()

        self.assertEqual(loaded2[0].name,'updated name 1')
        self.assertEqual(loaded2[1].name,'updated name 2')
        self.assertEqual(loaded2[2].name,'updated name 3')
        self.assertEqual(loaded2[3].name,'updated name 4')

    def test_remove_archtype(self):
        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        num_Arch = len(Manage_Archtypes.get_loaded_set().get_all())

        Manage_Archtypes.remove_archtype(1)

        self.assertEqual(len(Manage_Archtypes.get_loaded_set().get_all()),num_Arch - 1)

    def test_launch_edit(self):
        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        gui = Manage_Archtypes.launch_edit_archtype(None,1,True)

        self.assertNotEqual(gui,None)

    def test_launch_list(self):
        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        gui = Manage_Archtypes.launch_archtype_list(True)

        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
