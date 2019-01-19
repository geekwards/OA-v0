import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Foci

class test_Manage_Foci(unittest.TestCase):
    def test_foci_load_and_get(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_foci_save_update(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        num_foci = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'TestShrtDesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        foci_manager.save_one(clone)
        loaded2 = foci_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'Test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_foci)

    def test_foci_save_new(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        num_foci = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'Test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        foci_manager.save_one(clone)
        loaded2 = foci_manager.get_current_set()
        self.assertEqual(loaded2.all_items[4].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[4].short_description,'TestShrtDesc2')
        self.assertEqual(len(loaded2),num_foci + 1)

    def test_foci_save(self):
        foci_manager = Manage_Foci.Manage_foci()
        copy2(app_config.test_file_path + app_config.test_foci_filename,app_config.test_file_path + app_config.test_foci_filename + '2')
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename + '2')
        loaded = foci_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        foci_manager.save_one(loaded.all_items[0])
        foci_manager.save_one(loaded.all_items[1])
        foci_manager.save_one(loaded.all_items[2])
        foci_manager.save_one(loaded.all_items[3])
        foci_manager.save_all(app_config.test_file_path + app_config.test_foci_filename + '2',app_config.test_file_path + app_config.test_backup_foci_filename)
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename + '2')
        loaded2 = foci_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_foci_remove(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        num_foci = len(foci_manager.get_current_set())
        foci_manager.remove_item(foci_manager.get_current_set().all_items[1])
        self.assertEqual(len(foci_manager.get_current_set()),num_foci - 1)

    def test_foci_launch_edit(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        gui = foci_manager.launch_edit(None,1,True)
        self.assertNotEqual(gui,None)

    def test_foci_launch_list(self):
        foci_manager = Manage_Foci.Manage_foci()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        gui = foci_manager.launch_list('Foci',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
