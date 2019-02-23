import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Food
import GUI_Equipment_Controller
import GUI_List_Controller
import test__data

class test_Manage_Food(unittest.TestCase):
    def test_load_and_get(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_foods4)
 
    def test_load_file_DNE(self):
        food_manager = Manage_Food.Manage_food()
        try:
            food_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        food_manager = Manage_Food.Manage_food()
        loaded = food_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        food_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        food_manager.save_one(clone)
        loaded2 = food_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        food_manager = Manage_Food.Manage_food()
        copy2(app_config.test_file_path + app_config.test_food_filename,app_config.test_file_path + app_config.test_food_filename + '3')
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        food_manager.save_one(clone,app_config.test_file_path + app_config.test_food_filename + '3',app_config.test_file_path + app_config.test_backup_food_filename)
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        food_manager2 = Manage_Food.Manage_food()
        food_manager2.load_set(app_config.test_file_path + app_config.test_food_filename + '3')
        loaded2 = food_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        food_manager = Manage_Food.Manage_food()
        copy2(app_config.test_file_path + app_config.test_food_filename,app_config.test_file_path + app_config.test_food_filename + '3')
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        food_manager.save_one(clone,app_config.test_file_path + app_config.test_food_filename + '3',app_config.test_file_path + app_config.test_backup_food_filename)
        food_manager2 = Manage_Food.Manage_food()
        food_manager2.load_set(app_config.test_file_path + app_config.test_food_filename + '3')
        loaded2 = food_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        try:
            food_manager.save_one(test__data.test_archtype1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        try:
            food_manager.save_one(test__data.test_archtype1,app_config.test_file_path + app_config.test_food_filename + '4',app_config.test_file_path + app_config.test_backup_food_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  
 
    def test_big_save(self):
        food_manager = Manage_Food.Manage_food()
        copy2(app_config.test_file_path + app_config.test_food_filename,app_config.test_file_path + app_config.test_food_filename + '2')
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename + '2')
        loaded = food_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        food_manager.save_one(loaded.all_items[0])
        food_manager.save_one(loaded.all_items[1])
        food_manager.save_one(loaded.all_items[2])
        food_manager.save_one(loaded.all_items[3])
        food_manager.save_one(clone)
        food_manager.save_all(app_config.test_file_path + app_config.test_food_filename + '2',app_config.test_file_path + app_config.test_backup_food_filename)
        food_manager2 = Manage_Food.Manage_food()
        food_manager2.load_set(app_config.test_file_path + app_config.test_food_filename + '2')
        loaded2 = food_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_foods4)
        food_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_foods3)

    def test_remove_DNE(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        loaded = food_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_foods4)
        try:
            food_manager.remove_item(test__data.test_foods1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_edit('test1',None,True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_close_edit(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_edit('test1',None,True)
        gui = food_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_edit('DNE',None,True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_launch_list(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_list('Food',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        food_manager = Manage_Food.Manage_food()
        food_manager.load_set(app_config.test_file_path + app_config.test_food_filename)
        gui = food_manager.launch_list('NOTFOUND',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
