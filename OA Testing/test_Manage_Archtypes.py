import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Archtypes

class test_Manage_Archtypes(unittest.TestCase):

    def test_archtypes_load_and_get(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()

        self.assertTrue(len(loaded)>0)

    def test_archtype_save_update(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        num_Arch = len(loaded)

        self.assertEqual(loaded.all_archtypes[1].short_description,'TestShortDesc2')
        clone = loaded.all_archtypes[1].clone()

        clone.short_description = 'MODIFIED TEST'
        arch_manager.save_archtype(clone)
        loaded2 = arch_manager.get_current_set()

        self.assertEqual(loaded2.all_archtypes[1].name,'Test2')
        self.assertEqual(loaded2.all_archtypes[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_Arch)

    def test_archtype_save_new(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        num_Arch = len(loaded)

        self.assertEqual(loaded.all_archtypes[1].name,'Test2')
        clone = loaded.all_archtypes[1].clone()

        clone.name = 'MODIFIED TEST'
        arch_manager.save_archtype(clone)
        loaded2 = arch_manager.get_current_set()

        self.assertEqual(loaded2.all_archtypes[4].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_archtypes[4].short_description,'TestShortDesc2')
        self.assertEqual(len(loaded),num_Arch + 1)

    def test_archtypes_save(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        copy2(app_config.test_file_path + app_config.test_archive_filename,app_config.test_file_path + app_config.test_archive_filename + '2')
        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename + '2')

        loaded = arch_manager.get_current_set().clone()
        loaded.all_archtypes[0].short_description = 'updated name 1'
        loaded.all_archtypes[1].short_description = 'updated name 2'
        loaded.all_archtypes[2].short_description = 'updated name 3'
        loaded.all_archtypes[3].short_description = 'updated name 4'

        arch_manager.save_archtype(loaded.all_archtypes[0])
        arch_manager.save_archtype(loaded.all_archtypes[1])
        arch_manager.save_archtype(loaded.all_archtypes[2])
        arch_manager.save_archtype(loaded.all_archtypes[3])

        arch_manager.save_archtypes(app_config.test_file_path + app_config.test_archive_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename + '2')
        loaded2 = arch_manager.get_current_set()

        self.assertEqual(loaded2.all_archtypes[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_archtypes[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_archtypes[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_archtypes[3].short_description,'updated name 4')

    def test_archtype_remove(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        num_Arch = len(arch_manager.get_current_set())

        arch_manager.remove_archtype(arch_manager.get_current_set().all_archtypes[1])

        self.assertEqual(len(arch_manager.get_current_set()),num_Arch - 1)

    def test_archtype_launch_edit(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        gui = arch_manager.launch_edit_archtype(None,1,True)

        self.assertNotEqual(gui,None)

    def test_archtypes_launch_list(self):
        arch_manager = Manage_Archtypes.Manage_archtypes()

        arch_manager.load_archtypes(app_config.test_file_path + app_config.test_archive_filename)
        gui = arch_manager.launch_archtype_list(True)

        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
