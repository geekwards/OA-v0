import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__manage_archtypes
import GUI_Archtype_Controller
import test__gui_list_controller
import test__data

class test_Manage_Archtypes(unittest.TestCase):
    def test_load_and_get(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_archtypes4)

    def test_load_file_DNE(self):
        arch_manager = test__manage_archtypes.Manage_data()
        try:
            arch_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        arch_manager = test__manage_archtypes.Manage_data()
        loaded = arch_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        arch_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        arch_manager.save_one(clone)
        loaded2 = arch_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        arch_manager.save_one(clone,app_config.test_file_path + app_config.test_archive_filename + '3',app_config.test_file_path + app_config.test_backup_archive_filename)
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        arch_manager2 = test__manage_archtypes.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_archive_filename + '3')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        arch_manager.save_one(clone,app_config.test_file_path + app_config.test_archive_filename + '3',app_config.test_file_path + app_config.test_backup_archive_filename)
        arch_manager2 = test__manage_archtypes.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_archive_filename + '3')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        try:
            arch_manager.save_one(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        try:
            arch_manager.save_one(test__data.test_armor1,app_config.test_file_path + app_config.test_archive_filename + '4',app_config.test_file_path + app_config.test_backup_archive_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_big_save(self):
        arch_manager = test__manage_archtypes.Manage_data()
        copy2(app_config.test_file_path + app_config.test_archive_filename,app_config.test_file_path + app_config.test_archive_filename + '2')
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename + '2')
        loaded = arch_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        arch_manager.save_one(loaded.all_items[0])
        arch_manager.save_one(loaded.all_items[1])
        arch_manager.save_one(loaded.all_items[2])
        arch_manager.save_one(loaded.all_items[3])
        arch_manager.save_one(clone)
        arch_manager.save_all(app_config.test_file_path + app_config.test_archive_filename + '2',app_config.test_file_path + app_config.test_backup_archive_filename)
        arch_manager2 = test__manage_archtypes.Manage_data()
        arch_manager2.load_set(app_config.test_file_path + app_config.test_archive_filename + '2')
        loaded2 = arch_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_archtypes4)
        arch_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_archtypes3)

    def test_remove_DNE(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        loaded = arch_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_archtypes4)
        try:
            arch_manager.remove_item(test__data.test_armor1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        arch_manager.launch_edit('test1',None) 
        self.assertEqual(arch_manager.get_edit_controller().get_form().get_frame().ename.get(),'test1')

    def test_launch_list(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        self.assertEqual(type(arch_manager.get_list_controller()),test__gui_list_controller.GUI_controller)

    def test_launch_list_DNE(self):
        arch_manager = test__manage_archtypes.Manage_data()
        arch_manager.load_set(app_config.test_file_path + app_config.test_archive_filename)
        self.assertEqual(type(arch_manager.get_list_controller()),test__gui_list_controller.GUI_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
