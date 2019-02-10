import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Armor
import GUI_Equipment_Controller
import GUI_List_Controller
import test__data

class test_Manage_Armor(unittest.TestCase):
    def test_load_and_get(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_armors4)

    def test_load_file_DNE(self):
        armor_manager = Manage_Armor.Manage_armor()
        try:
            armor_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        armor_manager = Manage_Armor.Manage_armor()
        loaded = armor_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        armor_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        armor_manager.save_one(clone)
        loaded2 = armor_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        armor_manager = Manage_Armor.Manage_armor()
        copy2(app_config.test_file_path + app_config.test_armor_filename,app_config.test_file_path + app_config.test_armor_filename + '3')
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        armor_manager.save_one(clone,app_config.test_file_path + app_config.test_armor_filename + '3',app_config.test_file_path + app_config.test_backup_armor_filename)
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        armor_manager2 = Manage_Armor.Manage_armor()
        armor_manager2.load_set(app_config.test_file_path + app_config.test_armor_filename + '3')
        loaded2 = armor_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        armor_manager = Manage_Armor.Manage_armor()
        copy2(app_config.test_file_path + app_config.test_armor_filename,app_config.test_file_path + app_config.test_armor_filename + '3')
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        armor_manager.save_one(clone,app_config.test_file_path + app_config.test_armor_filename + '3',app_config.test_file_path + app_config.test_backup_armor_filename)
        armor_manager2 = Manage_Armor.Manage_armor()
        armor_manager2.load_set(app_config.test_file_path + app_config.test_armor_filename + '3')
        loaded2 = armor_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        try:
            armor_manager.save_one(test__data.test_archtype1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        try:
            armor_manager.save_one(test__data.test_archtype1,app_config.test_file_path + app_config.test_armor_filename + '4',app_config.test_file_path + app_config.test_backup_armor_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  
 
    def test_big_save(self):
        armor_manager = Manage_Armor.Manage_armor()
        copy2(app_config.test_file_path + app_config.test_armor_filename,app_config.test_file_path + app_config.test_armor_filename + '2')
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename + '2')
        loaded = armor_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        armor_manager.save_one(loaded.all_items[0])
        armor_manager.save_one(loaded.all_items[1])
        armor_manager.save_one(loaded.all_items[2])
        armor_manager.save_one(loaded.all_items[3])
        armor_manager.save_one(clone)
        armor_manager.save_all(app_config.test_file_path + app_config.test_armor_filename + '2',app_config.test_file_path + app_config.test_backup_armor_filename)
        armor_manager2 = Manage_Armor.Manage_armor()
        armor_manager2.load_set(app_config.test_file_path + app_config.test_armor_filename + '2')
        loaded2 = armor_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_armors4)
        armor_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_armors3)

    def test_remove_DNE(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        loaded = armor_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_armors4)
        try:
            armor_manager.remove_item(test__data.test_archtype1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_edit(None,'test1',True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_close_edit(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_edit(None,'test1',True)
        gui = armor_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_edit(None,'DNE',True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_launch_list(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_list('Armor',True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        armor_manager = Manage_Armor.Manage_armor()
        armor_manager.load_set(app_config.test_file_path + app_config.test_armor_filename)
        gui = armor_manager.launch_list('NOTFOUND',True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
