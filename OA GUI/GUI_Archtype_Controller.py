import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Archtype_Form

class GUI_archtype_controller:
    def create_form(self,parent=None):
        global archtype_form
        global archtype_window

        archtype_form,archtype_window = GUI_Archtype_Form.create_archtype_form(parent)

    def load_data(self,loaded_archtype,save_call,close_call,supress_gui=False):
        global current_archtype
        global rollback_archtype
        global save_callback
        global archtype_form
        global archtype_window
        global close_callback
    
        save_callback = save_call
        close_callback = close_call

        current_archtype = loaded_archtype
        rollback_archtype = loaded_archtype.clone()
        self.refresh_data()
        if supress_gui:
            return archtype_form
        else:
            archtype_window.mainloop()

    def refresh_data(self):
        global current_archtype
        global save_callback
        global archtype_form

        archtype_form.clear()
        archtype_form.add_item(current_archtype,self.close_click,self.cancel_click,self.edit_click,self.save_click)
        if current_archtype.isempty():
            archtype_form.set_edit()
        else:
            archtype_form.set_view()

    def close_click(self):
        global current_archtype
        global rollback_archtype
        global archtype_form
        global archtype_window
        global close_callback

        if not rollback_archtype.equals(current_archtype):
            #confirm save
            self.save_click()
        
        archtype_window.destroy()
        archtype_form = None
        close_callback()

    def edit_click(self):
        global archtype_form

        archtype_form.set_edit()

    def save_click(self):
        global save_callback
        global archtype_form
        global current_archtype
        global rollback_archtype

        current_archtype.name = archtype_form.f1.ename.get()
        current_archtype.short_description = archtype_form.f1.eshortdescription.get()
        current_archtype.description = archtype_form.f1.txtdescription.get("1.0",'end-1c')
        current_archtype.proficiency = archtype_form.f1.eproficiency.get()
        current_archtype.str_bonus = archtype_form.f1.estr.get()
        current_archtype.per_bonus = archtype_form.f1.eper.get()
        current_archtype.int_bonus = archtype_form.f1.eint.get()
        current_archtype.dex_bonus = archtype_form.f1.edex.get()
        current_archtype.cha_bonus = archtype_form.f1.echa.get()
        current_archtype.vit_bonus = archtype_form.f1.evit.get()
        current_archtype.mag_bonus = archtype_form.f1.emag.get()
        current_archtype.stamina_bonus = archtype_form.f1.estamina.get()
        current_archtype.attack_bonus = archtype_form.f1.eattack.get()
        current_archtype.reflex_bonus = archtype_form.f1.ereflex.get()
        current_archtype.feats = archtype_form.f1.efeats.get()
        current_archtype.movement = archtype_form.f1.emvmt.get()
        current_archtype.skill_points = archtype_form.f1.eskillpts.get()
        current_archtype.level_health = archtype_form.f1.elvlhealth.get()

        rollback_archtype = current_archtype.clone()
        save_callback(current_archtype)
        archtype_form.set_view()

    def cancel_click(self):
        global current_archtype
        global rollback_archtype
        global archtype_form

        if rollback_archtype.equals(current_archtype):
            #confirm rollback
            current_archtype = rollback_archtype
            self.refresh_data()

        archtype_form.set_view()

    def get_current_archtype(self):
        global current_archtype

        return current_archtype

    def get_archtype_form(self):
        global archtype_form

        return archtype_form

    def __init__(self):
        self.create_form()