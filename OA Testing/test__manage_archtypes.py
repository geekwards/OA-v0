import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Archtypes
import test__gui_archtype_controller
import test__gui_list_controller

class Manage_data(Manage_Archtypes.Manage_archtypes):
    def set_controller(self):
        self.edit_controller = test__gui_archtype_controller.GUI_controller()
        self.list_controller = test__gui_list_controller.GUI_controller()
    
    def get_edit_controller(self):
        return self.edit_controller

    def get_list_controller(self):
        return self.list_controller
