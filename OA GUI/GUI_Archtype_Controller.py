import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Archtype_Form

class GUI_archtype_controller:
    def create_form(self,parent=None):
        self.archtype_form,self.archtype_window = GUI_Archtype_Form.create_form(parent)

    def load_data(self,loaded_archtype,save_call,close_call):
        self.save_callback = save_call
        self.close_callback = close_call

        self.current_archtype = loaded_archtype
        self.rollback_archtype = loaded_archtype.clone()
        self.archtype_form.clear_frame()
        self.archtype_form.add_item(self.current_archtype,self.save_call,self.edit_call,self.close_call,self.cancel_call)
        if self.current_archtype.isempty():
            self.archtype_form.set_edit()
        else:
            self.archtype_form.set_view()

    def launch_form(self):
        self.archtype_window.mainloop()

    def new_call(self):
        raise NotImplementedError

    def edit_call(self):
        self.archtype_form.set_edit()

    def save_call(self):
        self.current_archtype.name = self.archtype_form.f1.ename.get()
        self.current_archtype.short_description = self.archtype_form.f1.eshortdescription.get()
        self.current_archtype.description = self.archtype_form.f1.txtdescription.get("1.0",'end-1c')
        self.current_archtype.proficiency = self.archtype_form.f1.eproficiency.get()
        self.current_archtype.str_bonus = self.archtype_form.f1.estr.get()
        self.current_archtype.per_bonus = self.archtype_form.f1.eper.get()
        self.current_archtype.int_bonus = self.archtype_form.f1.eint.get()
        self.current_archtype.dex_bonus = self.archtype_form.f1.edex.get()
        self.current_archtype.cha_bonus = self.archtype_form.f1.echa.get()
        self.current_archtype.vit_bonus = self.archtype_form.f1.evit.get()
        self.current_archtype.mag_bonus = self.archtype_form.f1.emag.get()
        self.current_archtype.stamina_bonus = self.archtype_form.f1.estamina.get()
        self.current_archtype.attack_bonus = self.archtype_form.f1.eattack.get()
        self.current_archtype.reflex_bonus = self.archtype_form.f1.ereflex.get()
        self.current_archtype.feats = self.archtype_form.f1.efeats.get()
        self.current_archtype.movement = self.archtype_form.f1.emvmt.get()
        self.current_archtype.skill_points = self.archtype_form.f1.eskillpts.get()
        self.current_archtype.level_health = self.archtype_form.f1.elvlhealth.get()

        self.rollback_archtype = self.current_archtype.clone()
        self.save_callback(self.current_archtype)
        self.archtype_form.set_view()

    def close_call(self):
        if not self.rollback_archtype == self.current_archtype:
            #confirm save
            self.save_call()
        
        self.archtype_window.destroy()
        self.archtype_form = None
        self.close_callback()

    def cancel_call(self):
        if self.rollback_archtype == self.current_archtype:
            #confirm rollback
            self.current_archtype = self.rollback_archtype
            self.load_data(self.current_archtype,self.save_callback,self.close_callback)

        self.archtype_form.set_view()

    def get_current_set(self):
        return self.current_archtype

    def get_form(self):
        return self.archtype_form

    def __init__(self):
        self.create_form()