import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Picklist_Controller
import List_Object
import Misc_List

class GUI_controller(GUI_Picklist_Controller.GUI_picklist_controller):
    def save_call(self):
        self.sel_list.remove(self.sel_list[0])
        super().save_call()