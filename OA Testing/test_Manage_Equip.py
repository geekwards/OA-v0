import unittest
from shutil import copy2
import copy

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__manage_equipment
import GUI_Equipment_Controller
import Base_Manage_Data
import test__gui_list_controller
import test__data
 
class test_Manage_Equip(unittest.TestCase):
    def test_equip_load_get(self):
        equip_manager = test__manage_equipment.Manage_data()
        equip_manager.load_set()
        loaded = equip_manager.get_current_set()
        self.assertEqual(len(loaded),7)
        self.assertEqual(sorted(loaded),sorted(test__data.test_equip_types))

    def test_launch_list(self):
        equip_manager = test__manage_equipment.Manage_data()
        equip_manager.load_set()
        self.assertEqual(type(equip_manager.get_list_controller()),test__gui_list_controller.GUI_controller)
 
if __name__ == '__main__':
    unittest.main(verbosity=2)
