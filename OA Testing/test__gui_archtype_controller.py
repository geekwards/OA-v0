import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype_Controller
import test__gui_archtype_form
import List_Object
import Misc_List

class GUI_controller(GUI_Archtype_Controller.GUI_archtype_controller):
    def create_form(self,parent=None):
        self.archtype_form = test__gui_archtype_form.GUI_archtype_form()
        self.archtype_window = test__gui_archtype_form.GUI_archtype_window()

