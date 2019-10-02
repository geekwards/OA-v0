import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List_Controller
import test__gui_misc_list_form
import List_Object
import Misc_List

class GUI_controller(GUI_Misc_List_Controller.GUI_misc_list_controller):
    def create_form(self,parent=None):
        self.misc_list_form = test__gui_misc_list_form.GUI_misc_list_form()
        self.misc_list_window = test__gui_misc_list_form.GUI_misc_list_window()
