import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Money

class test_Manage_Money(unittest.TestCase):
    def test_money_load_and_get(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_money_save_update(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set().clone()
        num_money = len(loaded)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdescr2')
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        money_manager.save_one(clone)
        loaded2 = money_manager.get_current_set()
        self.assertEqual(loaded2.all_items[1].name,'test2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')
        self.assertEqual(len(loaded),num_money)

    def test_money_save_new(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set().clone()
        num_money = len(loaded)
        self.assertEqual(loaded.all_items[1].name,'test2')
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        money_manager.save_one(clone)
        loaded2 = money_manager.get_current_set()
        self.assertEqual(loaded2.all_items[3].name,'MODIFIED TEST')
        self.assertEqual(loaded2.all_items[3].short_description,'testshortdescr2')
        self.assertEqual(len(loaded2),num_money + 1)

    def test_money_save(self):
        money_manager = Manage_Money.Manage_money()
        copy2(app_config.test_file_path + app_config.test_money_filename,app_config.test_file_path + app_config.test_money_filename + '2')
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set().clone()
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        money_manager.save_one(loaded.all_items[0])
        money_manager.save_one(loaded.all_items[1])
        money_manager.save_one(loaded.all_items[2])
        money_manager.save_all(app_config.test_file_path + app_config.test_money_filename + '2',app_config.test_file_path + app_config.test_backup_money_filename)
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename + '2')
        loaded2 = money_manager.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')

    def test_money_remove(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        num_money = len(money_manager.get_current_set())
        money_manager.remove_item(money_manager.get_current_set().all_items[1])
        self.assertEqual(len(money_manager.get_current_set()),num_money - 1)

    def test_money_launch_edit(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_edit(None,'test1',True)
        self.assertNotEqual(gui,None)

    def test_money_launch_list(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_list('Money',True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
