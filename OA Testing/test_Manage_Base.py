import unittest
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), '..') + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__base_manage_data
import GUI_List_Controller
import test__data

class test_Manage_Base(unittest.TestCase):
    def test_load_(self):
        base_manager = test__base_manage_data.Manage_data()
        try:
            base_manager.load_set('filename')
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised') 

    def test_get(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        self.assertEqual(loaded,test__data.test_armors4)

    def test_get_empty(self):
        base_manager = test__base_manage_data.Manage_data()
        loaded = base_manager.get_current_set()
        self.assertEqual(loaded,None)

    def test_save_update(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        self.assertEqual(loaded.all_items[1].short_description,'testshortdesc2')
        base_manager.save_one(clone)
        self.assertEqual(loaded.all_items[1].short_description,'MODIFIED TEST')

    def test_save_new(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        base_manager.save_one(clone)
        loaded2 = base_manager.get_current_set()
        self.assertEqual(len(loaded2),5)
        self.assertEqual(loaded.all_items[4].name,'MODIFIED TEST')

    def test_save_update_withfull(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        clone = loaded.all_items[1].clone()
        clone.short_description = 'MODIFIED TEST'
        try:
            base_manager.save_one(clone,'filename','filename')
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')         

    def test_save_new_withfull(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        clone = loaded.all_items[1].clone()
        clone.name = 'MODIFIED TEST'
        try:
            base_manager.save_one(clone,'filename','filename')
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')         
 
    def test_big_save(self):
        base_manager = test__base_manage_data.Manage_data()
        try:
            base_manager.save_all('filename','filename')
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')         

    def test_remove(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        loaded = base_manager.get_current_set()
        self.assertEqual(len(loaded),4)
        self.assertEqual(loaded,test__data.test_armors4)
        base_manager.remove_item(loaded.all_items[0])
        self.assertEqual(len(loaded),3)
        self.assertEqual(loaded,test__data.test_armors3)

    def test_launch_edit(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        try:
            gui = base_manager.launch_edit('test1',None,True)
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')  

    def test_close_edit(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        gui = base_manager.launch_list('TEST',None,True)
        gui = base_manager.close_edit_item(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_launch_edit_DNE(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        try:
            gui = base_manager.launch_edit('test1',None,True)
        except NotImplementedError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised') 
    
    def test_launch_list(self):
        base_manager = test__base_manage_data.Manage_data()
        base_manager.load_set2(test__data.test_armors4.clone())
        gui = base_manager.launch_list('TEST',None,True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

if __name__ == '__main__':
    unittest.main(verbosity=2)
