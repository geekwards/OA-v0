import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Money
import GUI_Equipment_Controller
import GUI_List_Controller
import test__data

class test_Manage_Money(unittest.TestCase):
    def test_load_and_get(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_monies4)
 
    def test_load_file_DNE(self):
        money_manager = Manage_Money.Manage_money()
        try:
            money_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        money_manager = Manage_Money.Manage_money()
        loaded = money_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        money_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        money_manager.save_one(clone)
        loaded2 = money_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        money_manager = Manage_Money.Manage_money()
        copy2(app_config.test_file_path + app_config.test_money_filename,app_config.test_file_path + app_config.test_money_filename + '3')
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        money_manager.save_one(clone,app_config.test_file_path + app_config.test_money_filename + '3',app_config.test_file_path + app_config.test_backup_money_filename)
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        money_manager2 = Manage_Money.Manage_money()
        money_manager2.load_set(app_config.test_file_path + app_config.test_money_filename + '3')
        loaded2 = money_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        money_manager = Manage_Money.Manage_money()
        copy2(app_config.test_file_path + app_config.test_money_filename,app_config.test_file_path + app_config.test_money_filename + '3')
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        money_manager.save_one(clone,app_config.test_file_path + app_config.test_money_filename + '3',app_config.test_file_path + app_config.test_backup_money_filename)
        money_manager2 = Manage_Money.Manage_money()
        money_manager2.load_set(app_config.test_file_path + app_config.test_money_filename + '3')
        loaded2 = money_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        try:
            money_manager.save_one(test__data.test_archtype1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        try:
            money_manager.save_one(test__data.test_archtype1,app_config.test_file_path + app_config.test_money_filename + '4',app_config.test_file_path + app_config.test_backup_money_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  
 
    def test_big_save(self):
        money_manager = Manage_Money.Manage_money()
        copy2(app_config.test_file_path + app_config.test_money_filename,app_config.test_file_path + app_config.test_money_filename + '2')
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename + '2')
        loaded = money_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        money_manager.save_one(loaded.all_items[0])
        money_manager.save_one(loaded.all_items[1])
        money_manager.save_one(loaded.all_items[2])
        money_manager.save_one(loaded.all_items[3])
        money_manager.save_one(clone)
        money_manager.save_all(app_config.test_file_path + app_config.test_money_filename + '2',app_config.test_file_path + app_config.test_backup_money_filename)
        money_manager2 = Manage_Money.Manage_money()
        money_manager2.load_set(app_config.test_file_path + app_config.test_money_filename + '2')
        loaded2 = money_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_monies4)
        money_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_monies3)

    def test_remove_DNE(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        loaded = money_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_monies4)
        try:
            money_manager.remove_item(test__data.test_foods1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_edit('test1',None,True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_close_edit(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_edit('test1',None,True)
        gui = money_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_edit('DNE',None,True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_launch_list(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_list('Food',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        money_manager = Manage_Money.Manage_money()
        money_manager.load_set(app_config.test_file_path + app_config.test_money_filename)
        gui = money_manager.launch_list('NOTFOUND',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
