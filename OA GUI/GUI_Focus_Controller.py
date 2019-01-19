import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Focus_Form
import List_Object
import GUI_Select_Set_Controller

class GUI_focus_controller:
    def create_form(self,parent=None):
        self.focus_form,self.focus_window = GUI_Focus_Form.create_form(parent)

    def load_data(self,loaded_focus,save_call,close_call):
        self.save_callback = save_call
        self.close_callback = close_call
        self.current_focus = loaded_focus
        self.rollback_focus = loaded_focus.clone()
        self.focus_form.clear_frame()
        self.focus_form.add_item(self.current_focus,self.edit_call,self.save_call,self.close_call,self.cancel_call,self.edit_picklist)
        if self.current_focus.isempty():
            self.focus_form.set_edit()
        else:
            self.focus_form.set_view()

    def launch_form(self):
        self.focus_window.mainloop()

    def new_call(self):
        raise NotImplementedError

    def edit_call(self):
        self.focus_form.set_edit()

    def save_call(self):
        self.current_focus.name = self.focus_form.f1.ename.get()
        self.current_focus.short_description = self.focus_form.f1.eshortdescr.get()
        self.current_focus.description = self.focus_form.f1.txtdescription.get("1.0",'end-1c')
        self.current_focus.str_bonus = self.focus_form.f1.estr.get()
        self.current_focus.per_bonus = self.focus_form.f1.eper.get()
        self.current_focus.int_bonus = self.focus_form.f1.eint.get()
        self.current_focus.dex_bonus = self.focus_form.f1.edex.get()
        self.current_focus.cha_bonus = self.focus_form.f1.echa.get()
        self.current_focus.vit_bonus = self.focus_form.f1.evit.get()
        self.current_focus.mag_bonus = self.focus_form.f1.emag.get()
        self.current_focus.str_skill_bonus = self.focus_form.f1.estrskill.get()
        self.current_focus.per_skill_bonus = self.focus_form.f1.eperskill.get()
        self.current_focus.int_skill_bonus = self.focus_form.f1.eintskill.get()
        self.current_focus.dex_skill_bonus = self.focus_form.f1.edexskill.get()
        self.current_focus.cha_skill_bonus = self.focus_form.f1.echaskill.get()
        self.current_focus.vit_skill_bonus = self.focus_form.f1.evitskill.get()
        self.current_focus.mag_skill_bonus = self.focus_form.f1.emagskill.get()
        self.current_focus.will_bonus = self.focus_form.f1.ewill.get()
        self.current_focus.fortitude_bonus = self.focus_form.f1.efortitude.get()
        self.current_focus.reflex_bonus = self.focus_form.f1.ereflex.get()
        self.current_focus.languages_bonus = []
        for lang in self.focus_form.f1.lstlangs.get(0,'end'):
            lang_name,lang_score = lang.split(":",1)
            self.current_focus.languages_bonus.append(List_Object.List_object(lang_name,lang_score))

        self.rollback_focus = self.current_focus.clone()
        self.save_callback(self.current_focus)
        self.focus_form.set_view()

    def close_call(self):
        if not self.rollback_focus == self.current_focus:
            #confirm save
            self.save_call()
        
        self.focus_window.destroy()
        self.focus_form = None
        self.close_callback()

    def cancel_call(self):
        if self.rollback_focus == self.current_focus:
            #confirm rollback
            self.current_focus = self.rollback_focus
            self.load_data(self.current_focus,self.save_call,self.close_call)

        self.focus_form.set_view()

    def get_current_set(self):
        return self.current_focus

    def get_form(self):
        return self.focus_form

    def load_picklists(self,langs):
        self.languages = langs

    def edit_picklist(self,type):
        select_controller = GUI_Select_Set_Controller.GUI_select_set_controller()
        self.current_list = []
        include_score = False
        source = []
        if type == 'Languages':
            for list in self.languages.all_lists:
                source.append([e for e in list.all_items if e.name not in [a.name for index,a in enumerate(current_focus.languages_bonus)]])
            for lang in self.current_focus.languages_bonus:
                self.current_list.append(lang.name.strip() + ': ' + lang.short_description.strip())
            include_score = True

        select_controller.load_sets(type,source,self.current_list,self.save_list,include_score)

    def save_picklist(self,type,list):
        lst = None
        if type=='Languages':
            lst = self.focus_form.f1.lstlangs

        if lst != None:
            lst.delete(0,'end')
            for item in list:
                lst.insert(0,item)

        self.select_controller.destroy_select_set()

    def __init__(self):
        self.create_form()