import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Focus_Form
import List_Object
import GUI_Select_Set_Controller

class GUI_focus_controller:
    def create_form(self,parent=None):
        global focus_form
        global focus_window

        focus_form,focus_window = GUI_Focus_Form.create_focus_form(parent)

    def load_lookups(self,langs):
        global languages

        languages = langs

    def load_data(self,loaded_focus,save_call,close_call,supress_gui=False):
        global current_focus
        global rollback_focus
        global save_callback
        global focus_form
        global focus_window
        global close_callback
    
        save_callback = save_call
        close_callback = close_call

        current_focus = loaded_focus
        rollback_focus = loaded_focus.clone()
        self.refresh_data()
        if supress_gui:
            return focus_form
        else:
            focus_window.mainloop()

    def refresh_data(self):
        global current_focus
        global save_callback
        global focus_form

        focus_form.clear()
        focus_form.add_item(current_focus,self.close_click,self.cancel_click,self.edit_click,self.save_click,self.edit_list)
        if current_focus.isempty():
            focus_form.set_edit()
        else:
            focus_form.set_view()

    def close_click(self):
        global current_focus
        global rollback_focus 
        global focus_form
        global focus_window
        global close_callback

        if not rollback_focus.equals(current_focus):
            #confirm save
            self.save_click()
        
        focus_window.destroy()
        focus_form = None
        close_callback()

    def edit_list(self,type):
        global languages
        global select_controller

        select_controller = GUI_Select_Set_Controller.GUI_select_set_controller()
        current_list = []

        include_score = False

        source = []

        if type == 'Languages':
            for list in languages.all_lists:
                source.append([e for e in list.all_items if e.name not in [a.name for index,a in enumerate(current_focus.languages_bonus)]])
            for lang in current_focus.languages_bonus:
                current_list.append(lang.name.strip() + ': ' + lang.short_description.strip())
            include_score = True

        select_controller.load_sets(type,source,current_list,self.save_list,include_score)

    def save_list(self,type,list):
        global focus_form

        lst = None

        if type=='Languages':
            lst = focus_form.f1.lstlangs

        if lst != None:
            lst.delete(0,'end')
            for item in list:
                lst.insert(0,item)

        select_controller.destroy_select_set()

    def edit_click(self):
        global focus_form

        focus_form.set_edit()

    def save_click(self):
        global save_callback
        global focus_form
        global current_focus
        global rollback_focus

        current_focus.name = focus_form.f1.ename.get()
        current_focus.short_description = focus_form.f1.eshortdescr.get()
        current_focus.description = focus_form.f1.txtdescription.get("1.0",'end-1c')
        current_focus.str_bonus = focus_form.f1.estr.get()
        current_focus.per_bonus = focus_form.f1.eper.get()
        current_focus.int_bonus = focus_form.f1.eint.get()
        current_focus.dex_bonus = focus_form.f1.edex.get()
        current_focus.cha_bonus = focus_form.f1.echa.get()
        current_focus.vit_bonus = focus_form.f1.evit.get()
        current_focus.mag_bonus = focus_form.f1.emag.get()
        current_focus.str_skill_bonus = focus_form.f1.estrskill.get()
        current_focus.per_skill_bonus = focus_form.f1.eperskill.get()
        current_focus.int_skill_bonus = focus_form.f1.eintskill.get()
        current_focus.dex_skill_bonus = focus_form.f1.edexskill.get()
        current_focus.cha_skill_bonus = focus_form.f1.echaskill.get()
        current_focus.vit_skill_bonus = focus_form.f1.evitskill.get()
        current_focus.mag_skill_bonus = focus_form.f1.emagskill.get()
        current_focus.will_bonus = focus_form.f1.ewill.get()
        current_focus.fortitude_bonus = focus_form.f1.efortitude.get()
        current_focus.reflex_bonus = focus_form.f1.ereflex.get()
        current_focus.languages_bonus = []
        for lang in focus_form.f1.lstlangs.get(0,'end'):
            lang_name,lang_score = lang.split(":",1)
            current_focus.languages_bonus.append(List_Object.List_object(lang_name,lang_score))

        rollback_focus = current_focus.clone()
        save_callback(current_focus)
        focus_form.set_view()

    def cancel_click(self):
        global current_focus
        global rollback_focus
        global focus_form

        if rollback_focus.equals(current_focus):
            #confirm rollback
            current_focus = rollback_focus
            self.refresh_data()

        focus_form.set_view()

    def get_current_focus(self):
        global current_focus

        return current_focus

    def get_focus_form(self):
        global focus_form

        return focus_form

    def __init__(self):
        self.create_form()