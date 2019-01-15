import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Race_Form
import List_Object
import GUI_Select_Set_Controller

class GUI_race_controller:
    race_form
    race_window
    languages
    foci
    feats
    current_race
    rollback_race
    save_callback
    close_callback

    def create_form(self,parent=None):
        self.race_form = None
        self.race_window = None
        self.languages = None
        self.foci = None
        self.feats = None
        self.current_race = None
        self.rollback_race = None
        self.save_callback = None
        self.close_callback = None
        self.race_form,self.race_window = GUI_Race_Form.create_race_form(parent)

    def load_lookups(self,sizes,bodies,langs,foc,fea):
        self.foci = foc
        self.feats = fea
        self.languages = langs
        self.race_form.add_lists(sizes,bodies)

    def load_data(self,loaded_race,save_call,close_call,supress_gui=False):
        self.save_callback = save_call
        self.close_callback = close_call

        self.current_race = loaded_race
        self.rollback_race = loaded_race.clone()
        self.refresh_data()
        if supress_gui:
            return self.race_form
        else:
            self.race_window.mainloop()

    def refresh_data(self):
        self.race_form.clear()
        self.race_form.add_item(self.current_race,self.close_click,self.cancel_click,self.edit_click,self.save_click,self.edit_list)
        if self.current_race.isempty():
            self.race_form.set_edit()
        else:
            self.race_form.set_view()

    def close_click(self):
        if not self.rollback_race.equals(self.current_race):
            self.save_click()
        
        self.race_window.destroy()
        self.race_form = None
        self.close_callback()

    def edit_list(self,type):
        select_controller = GUI_Select_Set_Controller.GUI_select_set_controller()
        current_list = []
        include_score = False
        source = []
        if type == 'Languages':
            for list in self.languages.all_lists:
                source.append([e for e in list.all_items if e.name not in [a.name for index,a in enumerate(self.current_race.languages_bonus)]])
            for lang in self.current_race.languages_bonus:
                current_list.append(lang.name.strip() + ': ' + lang.short_description.strip())
            include_score = True
        elif type == 'Feats':
            for list in feats.all_lists:
                source.append([e for e in list.all_items if e.name not in self.current_race.feats])
            for feat in self.current_race.feats:
                current_list.append(feat)
        elif type == 'Foci':
            for list in foci.all_lists:
                source.append([e for e in list.all_items if e.name not in self.current_race.foci])
            for foc in self.current_race.foci:
                current_list.append(foc)

        select_controller.load_sets(type,source,current_list,self.save_list,include_score)

    def save_list(self,type,list):
        lst = None
        if type=='Languages':
            lst = self.race_form.f1.lstlangs
        elif type=='Feats':
            lst = self.race_form.f1.lstfeats
        elif type=='Foci':
            lst = self.race_form.f1.lstfoci

        if lst != None:
            lst.delete(0,'end')
            for item in list:
                lst.insert(0,item)

        select_controller.destroy_select_set()

    def edit_click(self):
        self.race_form.set_edit()

    def save_click(self):
        self.current_race.name = self.race_form.f1.ename.get()
        self.current_race.short_description = self.race_form.f1.eshortdescr.get()
        self.current_race.description = self.race_form.f1.txtdescription.get("1.0",'end-1c')
        self.current_race.size = self.race_form.f1.cbosize.get()
        self.current_race.body = self.race_form.f1.cbobody.get()
        self.current_race.str_bonus = self.race_form.f1.estr.get()
        self.current_race.per_bonus = self.race_form.f1.eper.get()
        self.current_race.int_bonus = self.race_form.f1.eint.get()
        self.current_race.dex_bonus = self.race_form.f1.edex.get()
        self.current_race.cha_bonus = self.race_form.f1.echa.get()
        self.current_race.vit_bonus = self.race_form.f1.evit.get()
        self.current_race.mag_bonus = self.race_form.f1.emag.get()
        self.current_race.will_bonus = self.race_form.f1.ewill.get()
        self.current_race.fortitude_bonus = self.ace_form.f1.efortitude.get()
        self.current_race.reflex_bonus = self.race_form.f1.ereflex.get()
        self.current_race.languages_bonus = []
        for lang in self.race_form.f1.lstlangs.get(0,'end'):
            lang_name,lang_score = lang.split(":",1)
            self.current_race.languages_bonus.append(List_Object.List_object(lang_name,lang_score))
        self.current_race.foci = self.race_form.f1.lstfoci.get(0,'end')
        self.current_race.feats = self.race_form.f1.lstfeats.get(0,'end')

        self.rollback_race = self.current_race.clone()
        self.save_callback(current_race)
        self.race_form.set_view()

    def cancel_click(self):
        if self.rollback_race.equals(self.current_race):
            #confirm rollback
            self.current_race = self.rollback_race
            self.refresh_data()

        self.race_form.set_view()

    def get_current_race(self):
        return self.current_race

    def get_race_form(self):
        return self.race_form

    def __init__(self):
        self.create_form()