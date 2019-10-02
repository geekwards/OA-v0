import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Race_Controller
import test__gui_race_form
import List_Object
import Misc_List

class GUI_controller(GUI_Race_Controller.GUI_race_controller):
    def get_langs(self):
        return self.languages
 
    def get_sizes(self):
        self.sizes.sort()
        return self.sizes

    def get_bodies(self):
        self.bodies.sort()
        return self.bodies

    def get_foc(self):
        return self.foci

    def get_fea(self):
        self.feats.sort()
        return self.feats

    def get_current_picklist(self):
        if type(self.current_list[0]) == List_Object.List_object:
            plist = []
            for item in self.current_list:
                plist.append(item.name.strip() + ': ' + item.short_description.strip())
        else:
            plist = self.current_list
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
        self.race_form = test__gui_race_form.GUI_race_form()
        self.race_window = test__gui_race_form.GUI_race_window()

    def edit_picklist(self,pickname):
        if pickname == 'Languages':
            self.source = ['testlang1.1: langscore1.1', 'testlang1.2: langscore1.2', 'testlang1.3: langscore1.3']
            self.current_list = self.current_race.languages_bonus
        elif pickname == 'Feats':
            self.source = ['feat1.1', 'feat1.2', 'feat1.3']
            self.current_list = self.current_race.feats
        elif pickname == 'Foci':
            self.source = ['foci1.1', 'foci1.2', 'foci1.3']
            self.current_list = self.current_race.foci
