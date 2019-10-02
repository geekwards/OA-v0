import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_List_Controller
import test__gui_list_form
import List_Object
import Misc_List

class GUI_controller(GUI_List_Controller.GUI_list_controller):
    def create_form(self,parent=None):
        self.list_form = test__gui_list_form.GUI_list_form()
        self.list_window = test__gui_list_form.GUI_list_window()
