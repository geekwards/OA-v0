import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Focus_Form
import List_Object
import GUI_Picklist_Controller

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
        self.focus_window.mainloop()

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
            self.current_focus.languages_bonus.sort()
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

    def load_picklists(self,picklist):
        self.pick_list = picklist

    def edit_picklist(self,listtype):
        self.select_controller = GUI_Picklist_Controller.GUI_picklist_controller()
        self.current_list = []
        self.source = []
        include_score = False
        if listtype == 'Languages':
            picklist = self.pick_list
            self.source = [e.name.strip() + ': ' + e.short_description.strip() for e in picklist.all_items if e.name not in [a.name for index,a in enumerate(self.current_focus.languages_bonus)]]
            self.current_list = self.current_focus.languages_bonus
            include_score = True
        self.select_controller.load_data(listtype,self.source,self.current_list,self.save_picklist,include_score)
 
    def save_picklist(self,listtype,picklist):
        lst = None
        if listtype=='Languages':
            lst = self.focus_form.f1.lstlangs
        if lst != None:
            lst.delete(0,'end')
            for item in picklist.all_items:
                lst.insert('end',item)
        self.select_controller.destroy_picklist()

    def __init__(self,parent):
        self.create_form(parent)
        self.current_focus = None
        self.current_list = []
        self.source = []
        self.pick_list = []
        self.select_controller = None
