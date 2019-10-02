import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__manage_foci
import GUI_Focus_Controller
import GUI_List_Controller
import test__data

class test_Manage_Foci(unittest.TestCase):
    def test_load_and_get(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded.all_items[0].languages_bonus[0].name,test__data.test_foci4.all_items[0].languages_bonus[0].name)
        self.assertEqual(loaded,test__data.test_foci4)

    def test_load_file_DNE(self):
        foci_manager = test__manage_foci.Manage_data()
        try:
            foci_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        foci_manager = test__manage_foci.Manage_data()
        loaded = foci_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        foci_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        foci_manager.save_one(clone)
        loaded2 = foci_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        foci_manager = test__manage_foci.Manage_data()
        copy2(app_config.test_file_path + app_config.test_foci_filename,app_config.test_file_path + app_config.test_foci_filename + '3')
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        foci_manager.save_one(clone,app_config.test_file_path + app_config.test_foci_filename + '3',app_config.test_file_path + app_config.test_backup_foci_filename)
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        foci_manager2 = test__manage_foci.Manage_data()
        foci_manager2.load_set(app_config.test_file_path + app_config.test_foci_filename + '3')
        loaded2 = foci_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        foci_manager = test__manage_foci.Manage_data()
        copy2(app_config.test_file_path + app_config.test_foci_filename,app_config.test_file_path + app_config.test_foci_filename + '3')
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        foci_manager.save_one(clone,app_config.test_file_path + app_config.test_foci_filename + '3',app_config.test_file_path + app_config.test_backup_foci_filename)
        foci_manager2 = test__manage_foci.Manage_data()
        foci_manager2.load_set(app_config.test_file_path + app_config.test_foci_filename + '3')
        loaded2 = foci_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        try:
            foci_manager.save_one(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        foci_manager = test__manage_foci.Manage_data()
        copy2(app_config.test_file_path + app_config.test_foci_filename,app_config.test_file_path + app_config.test_foci_filename + '4')
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        try:
            foci_manager.save_one(test__data.test_armor1,app_config.test_file_path + app_config.test_foci_filename + '4',app_config.test_file_path + app_config.test_backup_foci_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_big_save(self):
        foci_manager = test__manage_foci.Manage_data()
        copy2(app_config.test_file_path + app_config.test_foci_filename,app_config.test_file_path + app_config.test_foci_filename + '2')
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename + '2')
        loaded = foci_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        foci_manager.save_one(loaded.all_items[0])
        foci_manager.save_one(loaded.all_items[1])
        foci_manager.save_one(loaded.all_items[2])
        foci_manager.save_one(loaded.all_items[3])
        foci_manager.save_one(clone)
        foci_manager.save_all(app_config.test_file_path + app_config.test_foci_filename + '2',app_config.test_file_path + app_config.test_backup_foci_filename)
        foci_manager2 = test__manage_foci.Manage_data()
        foci_manager2.load_set(app_config.test_file_path + app_config.test_foci_filename + '2')
        loaded2 = foci_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_foci4)
        foci_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_foci3)

    def test_remove_DNE(self):
        foci_manager = test__manage_foci.Manage_data()
        foci_manager.load_set(app_config.test_file_path + app_config.test_foci_filename)
        loaded = foci_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_foci4)
        try:
            foci_manager.remove_item(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  
 
    def test_lookup_data(self):
        foci_manager = test__manage_foci.Manage_data()
        self.assertEqual(foci_manager.get_language_data(),['Common', 'Elvish', 'Dwarvish'])

if __name__ == '__main__':
    unittest.main(verbosity=2)
