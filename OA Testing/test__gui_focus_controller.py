import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Focus_Controller
import test__gui_focus_form
import List_Object
import Misc_List

class GUI_controller(GUI_Focus_Controller.GUI_focus_controller):
    def get_langs(self):
        return self.pick_list
 
    def get_current_picklist(self):
        if type(self.current_list[0]) == List_Object.List_object:
            plist = []
            for item in self.current_list:
                plist.append(item.name.strip() + ': ' + item.short_description.strip())
        else:
            plist = self.current_list[0]
        return sorted(plist)

    def get_source_picklist(self):
        return self.source    
 
    def get_form_langs(self):
        return_langs = []
        for lang in self.focus_form.f1.lstlangs.get(0,'end'):
            lang_name,lang_score = lang.split(":",1)
            return_langs.append(List_Object.List_object(lang_name,lang_score))
        return return_langs

    def get_saved_picklist(self):
        return self.saved_picklist

    def save_picklist(self,listtype,picklist):
        self.saved_picklist = picklist

    def create_form(self,parent=None):
        self.focus_form = test__gui_focus_form.GUI_focus_form()
        self.focus_window = test__gui_focus_form.GUI_focus_window()

    def edit_picklist(self,pickname):
        picklist = self.pick_list
        self.source = [e.name.strip() + ': ' + e.short_description.strip() for e in picklist.all_items if e.name not in [a.name for index,a in enumerate(self.current_focus.languages_bonus)]]
        self.current_list = self.current_focus.languages_bonus
