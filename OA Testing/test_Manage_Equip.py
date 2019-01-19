import unittest
from shutil import copy2
import copy

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Equipment
import test__data

class test_Manage_Equip(unittest.TestCase):
    def test_equip_get(self):
        equip_manager = Manage_Equipment.Manage_equipment()
        equip_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        loaded = equip_manager.get_current_set()
        self.assertTrue(len(loaded)>0)

    def test_equip_launch_list(self):
        equip_manager = Manage_Equipment.Manage_equipment()
        equip_manager.load_set(app_config.test_file_path + app_config.test_misc_list_filename)
        gui = equip_manager.launch_list(True)
        self.assertNotEqual(gui,None)

if __name__ == '__main__':
    unittest.main(verbosity=2)
