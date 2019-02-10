import unittest
from shutil import copy2
import copy

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Equipment
import GUI_List_Controller
import GUI_Equipment_Controller
import test__data
 
class test_Manage_Equip(unittest.TestCase):
    def test_equip_load_get(self):
        equip_manager = Manage_Equipment.Manage_equipment()
        equip_manager.load_set(app_config.test_file_path + app_config.test_equipmenttype_filename)
        loaded = equip_manager.get_current_set()
        self.assertEqual(len(loaded),7)
        self.assertEqual(sorted(loaded),sorted(test__data.test_equip_types))

    def test_equip_launch_list(self):
        equip_manager = Manage_Equipment.Manage_equipment()
        equip_manager.load_set(app_config.test_file_path + app_config.test_equipmenttype_filename)
        gui = equip_manager.launch_list(True)
        self.assertEqual(type(gui),GUI_List_Controller.GUI_list_controller)

    def test_equip_launch_edit(self):
        equip_manager = Manage_Equipment.Manage_equipment()
        equip_manager.load_set(app_config.test_file_path + app_config.test_equipmenttype_filename)
        for equip_type in equip_manager.get_current_set():
            name = equip_type.name
            gui = equip_manager.launch_edit(None,name,True)
            self.assertEqual(type(gui),GUI_Equipment_Controller.GUI_equipment_controller)
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
