import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Races

class test_Manage_Races(unittest.TestCase):

    def test_races_load_and_get(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_race_save_update(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        num_race = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'TestShortDesc2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        race_manager.save_one(clone)
        loaded2 = race_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'Test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_race)

    def test_race_save_new(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        num_race = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'Test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        race_manager.save_one(clone)
        loaded2 = race_manager.get_current_set()
        self.assertEqual(loaded2.all_items[4].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[4].short_description,'TestShortDesc2')
        self.assertEqual(len(loaded2),num_race + 1)

    def test_races_save(self):
        race_manager = Manage_Races.Manage_races()
        copy2(app_config.test_file_path + app_config.test_race_filename,app_config.test_file_path + app_config.test_race_filename + '2')
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename + '2')
        loaded = race_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        race_manager.save_one(loaded.all_items[0])
        race_manager.save_one(loaded.all_items[1])
        race_manager.save_one(loaded.all_items[2])
        race_manager.save_one(loaded.all_items[3])
        race_manager.save_all(app_config.test_file_path + app_config.test_race_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename + '2')
        loaded2 = race_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_race_remove(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        num_race = len(race_manager.get_current_set())
        race_manager.remove_item(race_manager.get_current_set().all_items[1])
        self.assertEqual(len(race_manager.get_current_set()),num_race - 1)

    def test_race_launch_edit(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_edit(None,1,True)
        self.assertNotEqual(gui,None)

    def test_races_launch_list(self):
        race_manager = Manage_Races.Manage_races()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_list('Races',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
