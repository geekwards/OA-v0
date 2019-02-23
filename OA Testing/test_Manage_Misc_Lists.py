import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Misc_Lists
import List_Object
import GUI_Misc_List_Controller
import GUI_List_Controller
import test__data

class test_Manage_Misc_Lists(unittest.TestCase):
    def test_load_and_get(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_misclists4)

    def test_load_file_DNE(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        try:
            misclist_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        loaded = misclist_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.all_items[0].short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].all_items[0].short_description,'testshortdesc2.1')
        misclist_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].all_items[0].short_description,'MODIFIED TEST')

    def test_save_new(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        misclist_manager.save_one(clone)
        loaded2 = misclist_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '3')
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.all_items[0].short_description = 'MODIFIED TEST'
        misclist_manager.save_one(clone,app_config.test_file_path + app_config.test_misc_list_filename + '3',app_config.test_file_path + app_config.test_backup_misc_list_filename)
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        misclist_manager2 = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager2.load_set(app_config.test_file_path + app_config.test_misc_list_filename + '3')
        loaded2 = misclist_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].all_items[0].short_description,'testshortdesc2.1')
        self.assertEqual(loaded2.all_items[1].all_items[0].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '3')
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        misclist_manager.save_one(clone,app_config.test_file_path + app_config.test_misc_list_filename + '3',app_config.test_file_path + app_config.test_backup_misc_list_filename)
        misclist_manager2 = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager2.load_set(app_config.test_file_path + app_config.test_misc_list_filename + '3')
        loaded2 = misclist_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        try:
            misclist_manager.save_one(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '4')
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        try:
            misclist_manager.save_one(test__data.test_armor1,app_config.test_file_path + app_config.test_misc_list_filename + '4',app_config.test_file_path + app_config.test_backup_misc_list_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_big_save(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        copy2(app_config.test_file_path + app_config.test_misc_list_filename,app_config.test_file_path + app_config.test_misc_list_filename + '2')
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename + '2')
        loaded = misclist_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].all_items[0].short_description = 'updated name 2'
        loaded.all_items[2].all_items[0].short_description = 'updated name 3'
        loaded.all_items[3].all_items[0].short_description = 'updated name 4'
        misclist_manager.save_one(loaded.all_items[0])
        misclist_manager.save_one(loaded.all_items[1])
        misclist_manager.save_one(loaded.all_items[2])
        misclist_manager.save_one(loaded.all_items[3])
        misclist_manager.save_one(clone)
        misclist_manager.save_all(app_config.test_file_path + app_config.test_misc_list_filename + '2',app_config.test_file_path + app_config.test_backup_misc_list_filename)
        misclist_manager2 = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager2.load_set(app_config.test_file_path + app_config.test_misc_list_filename + '2')
        loaded2 = misclist_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].all_items[0].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].all_items[0].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].all_items[0].short_description,'updated name 4')

    def test_remove(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_misclists4)
        misclist_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_misclists3)

    def test_remove_DNE(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = misclist_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_misclists4)
        try:
            misclist_manager.remove_item(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misclist_manager.launch_edit('test1',None,True)
        self.assertEqual(type(gui),GUI_Misc_List_Controller.GUI_misc_list_controller)

    def test_close_edit(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misclist_manager.launch_edit('test1',None,True)
        gui = misclist_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misclist_manager.launch_edit('DNE',None,True)
        self.assertEqual(type(gui),GUI_Misc_List_Controller.GUI_misc_list_controller)

    def test_launch_list(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misclist_manager.launch_list('Archtypes',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        misclist_manager = Manage_Misc_Lists.Manage_misc_lists()
        misclist_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = misclist_manager.launch_list('NOTFOUND',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
