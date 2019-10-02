import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Equipment_Controller
import test__gui_equipment_form
import List_Object
import Misc_List

class GUI_controller(GUI_Equipment_Controller.GUI_equipment_controller):
    def create_form(self,parent=None):
        self.equipment_form = test__gui_equipment_form.GUI_equipment_form()
        self.equipment_window = test__gui_equipment_form.GUI_equipment_window()
