import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Manage_Data
import test__data

class test_Manage_Base(unittest.TestCase):
    def test_base_get(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        loaded = base_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_base_save_update(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        loaded = base_manager.get_current_set()
        num_Base = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'test short descr2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        base_manager.save_one(clone)
        loaded2 = base_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_Base)

    def test_base_save_new(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        loaded = base_manager.get_current_set()
        num_Base = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        base_manager.save_one(clone)
        loaded2 = base_manager.get_current_set()
        self.assertEqual(loaded2.all_items[4].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[4].short_description,'test short descr2')
        self.assertEqual(len(loaded),num_Base + 1)

    def test_base_remove(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        num_Base = len(base_manager.get_current_set())
        base_manager.remove_item(base_manager.get_current_set().all_items[1])
        self.assertEqual(len(base_manager.get_current_set()),num_Base - 1)

    def test_base_launch_list(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        gui = base_manager.launch_list('Base Test',True)
        self.assertNotEqual(gui,None)

    def test_base_close_edit(self):
        base_manager = Base_Manage_Data.Manage_data()
        base_manager.set_set(test__data.test_races.clone())
        gui = base_manager.launch_list('Base Test',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
