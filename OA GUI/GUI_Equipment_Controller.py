import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Equipment_Form

class GUI_equipment_controller:
    def create_form(self,parent=None):
        self.equipment_form,self.equipment_window = GUI_Equipment_Form.create_form(parent)

    def load_data(self,equip_type,loaded_equipment,save_call,close_call):
        self.save_callback = save_call
        self.close_callback = close_call
        self.current_equipment = loaded_equipment
        self.rollback_equipment = loaded_equipment.clone()
        self.equipment_type = equip_type
        self.equipment_form.clear_frame()
        self.equipment_form.add_item(self.equipment_type,self.current_equipment,self.edit_call,self.save_call,self.close_call,self.cancel_call)
        if self.current_equipment.isempty():
            self.equipment_form.set_edit()
        else:
            self.equipment_form.set_view()

    def launch_form(self):
        self.equipment_window.mainloop()

    def new_call(self):
        raise NotImplementedError

    def edit_call(self):
        self.equipment_form.set_edit()

    def save_call(self):
        self.current_equipment.name = self.equipment_form.f1.ename.get()
        self.current_equipment.short_description = self.equipment_form.f1.eshortdescription.get()
        self.current_equipment.description = self.equipment_form.f1.txtdescription.get("1.0",'end-1c')
        self.current_equipment.cost = self.equipment_form.f1.ecost.get()
        self.current_equipment.weight = self.equipment_form.f1.eweight.get()

        self.rollback_equipment = self.current_equipment.clone()
        self.save_callback(self.current_equipment)
        self.equipment_form.set_view()

    def close_call(self):
        if not self.rollback_equipment == self.current_equipment:
            #confirm save
            self.save_click()
        
        self.equipment_window.destroy()
        self.equipment_form = None
        self.close_callback()

    def cancel_call(self):
        if self.rollback_equipment == self.current_equipment:
            #confirm rollback
            self.current_equipment = self.rollback_equipment
            self.load_data(self.equipment_type,self.current_equipment,self.save_call,self.close_call)

        self.equipment_form.set_view()

    def get_current_set(self):
        return self.current_equipment

    def get_form(self):
        return self.equipment_form

    def __init__(self):
        self.create_form()