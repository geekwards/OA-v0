import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Focus_Controller
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
        super().save_picklist(listtype,picklist)