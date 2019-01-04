import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Race_Form
import List_Object
import GUI_Select_Set_Controller

class GUI_race_controller:
    def create_form(self,parent=None):
        global race_form
        global race_window

        race_form,race_window = GUI_Race_Form.create_race_form(parent)

    def load_lookups(self,sizes,bodies,langs,foc,fea):
        global languages
        global foci
        global feats

        foci = foc
        feats = fea
        languages = langs
        race_form.add_lists(sizes,bodies)

    def load_data(self,loaded_race,save_call,close_call,supress_gui=False):
        global current_race
        global rollback_race
        global save_callback
        global race_form
        global race_window
        global close_callback
    
        save_callback = save_call
        close_callback = close_call

        current_race = loaded_race
        rollback_race = loaded_race.clone()
        self.refresh_data()
        if supress_gui:
            return race_form
        else:
            race_window.mainloop()

    def refresh_data(self):
        global current_race
        global save_callback
        global race_form

        race_form.clear()
        race_form.add_item(current_race,self.close_click,self.cancel_click,self.edit_click,self.save_click,self.edit_list)
        if current_race.isempty():
            race_form.set_edit()
        else:
            race_form.set_view()

    def close_click(self):
        global current_race
        global rollback_race 
        global race_form
        global race_window
        global close_callback

        if not rollback_race.equals(current_race):
            #confirm save
            self.save_click()
        
        race_window.destroy()
        race_form = None
        close_callback()

    def edit_list(self,type):
        global feats
        global foci
        global languages
        global select_controller

        select_controller = GUI_Select_Set_Controller.GUI_select_set_controller()
        current_list = []

        include_score = False

        source = []

        if type == 'Languages':
            for list in languages.all_lists:
                source.append([e for e in list.all_items if e.name not in [a.name for index,a in enumerate(current_race.languages_bonus)]])
            for lang in current_race.languages_bonus:
                current_list.append(lang.name.strip() + ': ' + lang.short_description.strip())
            include_score = True
        elif type == 'Feats':
            for list in feats.all_lists:
                source.append([e for e in list.all_items if e.name not in current_race.feats])
            for feat in current_race.feats:
                current_list.append(feat)
        elif type == 'Foci':
            for list in foci.all_lists:
                source.append([e for e in list.all_items if e.name not in current_race.foci])
            for foc in current_race.foci:
                current_list.append(foc)

        select_controller.load_sets(type,source,current_list,self.save_list,include_score)

    def save_list(self,type,list):
        global race_form

        lst = None

        if type=='Languages':
            lst = race_form.f1.lstlangs
        elif type=='Feats':
            lst = race_form.f1.lstfeats
        elif type=='Foci':
            lst = race_form.f1.lstfoci

        if lst != None:
            lst.delete(0,'end')
            for item in list:
                lst.insert(0,item)

        select_controller.destroy_select_set()

    def edit_click(self):
        global race_form

        race_form.set_edit()

    def save_click(self):
        global save_callback
        global race_form
        global current_race
        global rollback_race

        current_race.name = race_form.f1.ename.get()
        current_race.short_description = race_form.f1.eshortdescr.get()
        current_race.description = race_form.f1.txtdescription.get("1.0",'end-1c')
        current_race.size = race_form.f1.cbosize.get()
        current_race.body = race_form.f1.cbobody.get()
        current_race.str_bonus = race_form.f1.estr.get()
        current_race.per_bonus = race_form.f1.eper.get()
        current_race.int_bonus = race_form.f1.eint.get()
        current_race.dex_bonus = race_form.f1.edex.get()
        current_race.cha_bonus = race_form.f1.echa.get()
        current_race.vit_bonus = race_form.f1.evit.get()
        current_race.mag_bonus = race_form.f1.emag.get()
        current_race.will_bonus = race_form.f1.ewill.get()
        current_race.fortitude_bonus = race_form.f1.efortitude.get()
        current_race.reflex_bonus = race_form.f1.ereflex.get()
        current_race.languages_bonus = []
        for lang in race_form.f1.lstlangs.get(0,'end'):
            lang_name,lang_score = lang.split(":",1)
            current_race.languages_bonus.append(List_Object.List_object(lang_name,lang_score))
        current_race.foci = race_form.f1.lstfoci.get(0,'end')
        current_race.feats = race_form.f1.lstfeats.get(0,'end')

        rollback_race = current_race.clone()
        save_callback(current_race)
        race_form.set_view()

    def cancel_click(self):
        global current_race
        global rollback_race
        global race_form

        if rollback_race.equals(current_race):
            #confirm rollback
            current_race = rollback_race
            self.refresh_data()

        race_form.set_view()

    def get_current_race(self):
        global current_race

        return current_race

    def get_race_form(self):
        global race_form

        return race_form

    def __init__(self):
        self.create_form()