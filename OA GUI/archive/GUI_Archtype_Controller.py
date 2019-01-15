import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Base_Controller
import GUI_Archtype_Form

class GUI_archtype_controller(GUI_Base_Controller.Base_controller):
    def create_form(self,parent=None):
        self.data_form = GUI_Archtype_Form.GUI_archtype_form(parent)
        super().set_form(self.data_form)

    def save_click(self):
        current_archtype = super().get_current_data()
        current_archtype.name = self.data_form.f1.ename.get()
        current_archtype.short_description = self.data_form.f1.eshortdescription.get()
        current_archtype.description = self.data_form.f1.txtdescription.get("1.0",'end-1c')
        current_archtype.proficiency = self.data_form.f1.eproficiency.get()
        current_archtype.str_bonus = self.data_form.f1.estr.get()
        current_archtype.per_bonus = self.data_form.f1.eper.get()
        current_archtype.int_bonus = self.data_form.f1.eint.get()
        current_archtype.dex_bonus = self.data_form.f1.edex.get()
        current_archtype.cha_bonus = self.data_form.f1.echa.get()
        current_archtype.vit_bonus = self.data_form.f1.evit.get()
        current_archtype.mag_bonus = self.data_form.f1.emag.get()
        current_archtype.stamina_bonus = self.data_form.f1.estamina.get()
        current_archtype.attack_bonus = self.data_form.f1.eattack.get()
        current_archtype.reflex_bonus = self.data_form.f1.ereflex.get()
        current_archtype.feats = self.data_form.f1.efeats.get()
        current_archtype.movement = self.data_form.f1.emvmt.get()
        current_archtype.skill_points = self.data_form.f1.eskillpts.get()
        current_archtype.level_health = self.data_form.f1.elvlhealth.get()

        super().set_data(current_archtype.clone())
        super().save_click()
        super().load_form
