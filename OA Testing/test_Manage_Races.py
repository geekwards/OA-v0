import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__manage_races
import GUI_Race_Controller
import GUI_List_Controller
import test__data

class test_Manage_Races(unittest.TestCase):
    def test_load_and_get(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_races4)

    def test_load_file_DNE(self):
        race_manager = test__manage_races.Manage_data()
        try:
            race_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        race_manager = test__manage_races.Manage_data()
        loaded = race_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        race_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        race_manager.save_one(clone)
        loaded2 = race_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        race_manager = test__manage_races.Manage_data()
        copy2(app_config.test_file_path + app_config.test_race_filename,app_config.test_file_path + app_config.test_race_filename + '3')
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        race_manager.save_one(clone,app_config.test_file_path + app_config.test_race_filename + '3',app_config.test_file_path + app_config.test_backup_foci_filename)
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        arch_manager2 = test__manage_races.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_race_filename + '3')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        race_manager = test__manage_races.Manage_data()
        copy2(app_config.test_file_path + app_config.test_race_filename,app_config.test_file_path + app_config.test_race_filename + '3')
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        race_manager.save_one(clone,app_config.test_file_path + app_config.test_race_filename + '3',app_config.test_file_path + app_config.test_backup_foci_filename)
        arch_manager2 = test__manage_races.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_race_filename + '3')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        try:
            race_manager.save_one(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        race_manager = test__manage_races.Manage_data()
        copy2(app_config.test_file_path + app_config.test_race_filename,app_config.test_file_path + app_config.test_race_filename + '4')
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        try:
            race_manager.save_one(test__data.test_armor1,app_config.test_file_path + app_config.test_race_filename + '4',app_config.test_file_path + app_config.test_backup_foci_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_big_save(self):
        race_manager = test__manage_races.Manage_data()
        copy2(app_config.test_file_path + app_config.test_race_filename,app_config.test_file_path + app_config.test_race_filename + '2')
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename + '2')
        loaded = race_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        race_manager.save_one(loaded.all_items[0])
        race_manager.save_one(loaded.all_items[1])
        race_manager.save_one(loaded.all_items[2])
        race_manager.save_one(loaded.all_items[3])
        race_manager.save_one(clone)
        race_manager.save_all(app_config.test_file_path + app_config.test_race_filename + '2',app_config.test_file_path + app_config.test_backup_foci_filename)
        arch_manager2 = test__manage_races.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_race_filename + '2')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_races4)
        race_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_races3)

    def test_remove_DNE(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        loaded = race_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_races4)
        try:
            race_manager.remove_item(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_edit(1,None,True)
        self.assertEqual(type(gui),GUI_Race_Controller.GUI_race_controller)

    def test_close_edit(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_edit('test1',None,True)
        gui = race_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_edit('DNE',None,True)
        self.assertEqual(type(gui),GUI_Race_Controller.GUI_race_controller)

    def test_launch_list(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_list('Foci',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        race_manager = test__manage_races.Manage_data()
        race_manager.load_set(app_config.test_file_path + app_config.test_race_filename)
        gui = race_manager.launch_list('NOTFOUND',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_lookup_data(self):
        race_manager = test__manage_races.Manage_data()
        self.assertEqual(race_manager.get_language_data(),['Common', 'Elvish', 'Dwarvish'])
        self.assertEqual(race_manager.get_sizes_data(),['Small', 'Medium', 'Large'])
        self.assertEqual(race_manager.get_bodies_data(),['Slim', 'Average', 'Stout'])
        self.assertEqual(race_manager.get_foci_data(),['Elf', 'ambition'])
        self.assertEqual(race_manager.get_feats_data(),['General Feats', 'Supernatural Feats', 'Non-Human Feats'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
