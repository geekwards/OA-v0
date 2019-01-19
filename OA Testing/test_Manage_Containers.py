import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Containers

class test_Manage_Containers(unittest.TestCase):
    def test_container_load_and_get(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_container_save_update(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        num_container = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshrtdesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        container_manager.save_one(clone)
        loaded2 = container_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_container)

    def test_container_save_new(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set().clone()
        num_container = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        container_manager.save_one(clone)
        loaded2 = container_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshrtdesc2')
        self.assertEqual(len(loaded2),num_container + 1)

    def test_container_save(self):
        container_manager = Manage_Containers.Manage_containers()
        copy2(app_config.test_file_path + app_config.test_container_filename,app_config.test_file_path + app_config.test_container_filename + '2')
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        container_manager.save_one(loaded.all_items[0])
        container_manager.save_one(loaded.all_items[1])
        container_manager.save_one(loaded.all_items[2])
        container_manager.save_all(app_config.test_file_path + app_config.test_container_filename + '2',app_config.test_file_path + app_config.test_backup_container_filename)
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename + '2')
        loaded2 = container_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_container_remove(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        num_container = len(container_manager.get_current_set())
        container_manager.remove_item(container_manager.get_current_set().all_items[1])
        self.assertEqual(len(container_manager.get_current_set()),num_container - 1)

    def test_container_launch_edit(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_container_launch_list(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_list('Containers',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
