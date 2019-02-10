import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Containers
import GUI_Equipment_Controller
import GUI_List_Controller
import test__data

class test_Manage_Containers(unittest.TestCase):
    def test_load_and_get(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_containers4)
 
    def test_load_file_DNE(self):
        container_manager = Manage_Containers.Manage_containers()
        try:
            container_manager.load_set('no filename')
        except FileNotFoundError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')      

    def test_get_empty(self):
        container_manager = Manage_Containers.Manage_containers()
        loaded = container_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        container_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        container_manager.save_one(clone)
        loaded2 = container_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        container_manager = Manage_Containers.Manage_containers()
        copy2(app_config.test_file_path + app_config.test_container_filename,app_config.test_file_path + app_config.test_container_filename + '3')
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        container_manager.save_one(clone,app_config.test_file_path + app_config.test_container_filename + '3',app_config.test_file_path + app_config.test_backup_container_filename)
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        container_manager2 = Manage_Containers.Manage_containers()
        container_manager2.load_set(app_config.test_file_path + app_config.test_container_filename + '3')
        loaded2 = container_manager2.get_current_set()
        self.assertEqual(len(loaded2),4)
        self.assertEqual(loaded2.all_items[1].name,loaded.all_items[1].name)
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        self.assertEqual(loaded2.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new_withfull(self):
        container_manager = Manage_Containers.Manage_containers()
        copy2(app_config.test_file_path + app_config.test_container_filename,app_config.test_file_path + app_config.test_container_filename + '3')
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        container_manager.save_one(clone,app_config.test_file_path + app_config.test_container_filename + '3',app_config.test_file_path + app_config.test_backup_container_filename)
        container_manager2 = Manage_Containers.Manage_containers()
        container_manager2.load_set(app_config.test_file_path + app_config.test_container_filename + '3')
        loaded2 = container_manager2.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_wrongtype(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        try:
            container_manager.save_one(test__data.test_archtype1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_save_wrongtype_withfull(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        try:
            container_manager.save_one(test__data.test_archtype1,app_config.test_file_path + app_config.test_container_filename + '4',app_config.test_file_path + app_config.test_backup_container_filename)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  
 
    def test_big_save(self):
        container_manager = Manage_Containers.Manage_containers()
        copy2(app_config.test_file_path + app_config.test_container_filename,app_config.test_file_path + app_config.test_container_filename + '2')
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename + '2')
        loaded = container_manager.get_current_set().clone()
        self.assertEqual(len(loaded),4)
        clone = loaded.all_items[0].clone()
        clone.name = 'MODIFIED'
        loaded.all_items[0].short_description = 'updated name 1'
        loaded.all_items[1].short_description = 'updated name 2'
        loaded.all_items[2].short_description = 'updated name 3'
        loaded.all_items[3].short_description = 'updated name 4'
        container_manager.save_one(loaded.all_items[0])
        container_manager.save_one(loaded.all_items[1])
        container_manager.save_one(loaded.all_items[2])
        container_manager.save_one(loaded.all_items[3])
        container_manager.save_one(clone)
        container_manager.save_all(app_config.test_file_path + app_config.test_container_filename + '2',app_config.test_file_path + app_config.test_backup_container_filename)
        container_manager2 = Manage_Containers.Manage_containers()
        container_manager2.load_set(app_config.test_file_path + app_config.test_container_filename + '2')
        loaded2 = container_manager2.get_current_set()
        self.assertEqual(loaded2.all_items[0].short_description,'updated name 1')
        self.assertEqual(loaded2.all_items[1].short_description,'updated name 2')
        self.assertEqual(loaded2.all_items[2].short_description,'updated name 3')
        self.assertEqual(loaded2.all_items[3].short_description,'updated name 4')

    def test_remove(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_containers4)
        container_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_containers3)

    def test_remove_DNE(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        loaded = container_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_containers4)
        try:
            container_manager.remove_item(test__data.test_containers1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_launch_edit(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_edit(None,'test1',True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_close_edit(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_edit(None,'test1',True)
        gui = container_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_edit(None,'DNE',True)
        self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)

    def test_launch_list(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_list('Containers',True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_list_DNE(self):
        container_manager = Manage_Containers.Manage_containers()
        container_manager.load_set(app_config.test_file_path + app_config.test_container_filename)
        gui = container_manager.launch_list('NOTFOUND',True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
