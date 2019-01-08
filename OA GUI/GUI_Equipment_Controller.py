import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Equipment_Form

class GUI_equipment_controller:
    equipment_form
    equipment_window
    current_equipment
    rollback_equipment
    save_callback
    close_callback
    equipment_type

    def create_form(self,parent=None):
        self.equipment_form = None
        self.equipment_window = None
        self.current_equipment
        self.rollback_equipment
        self.save_callback
        self.close_callback
        self.equipment_type
        self.equipment_form,self.equipment_window = GUI_Equipment_Form.create_equipment_form(parent)

    def load_data(self,equip_type,loaded_equipment,save_call,close_call,supress_gui=False):
        self.save_callback = save_call
        self.close_callback = close_call
        self.current_equipment = loaded_equipment
        self.rollback_equipment = loaded_equipment.clone()
        self.equipment_type = equip_type
        self.refresh_data()
        if supress_gui:
            return self.equipment_form
        else:
            self.equipment_window.mainloop()

    def refresh_data(self):
        self.equipment_form.configure_form(self.equipment_type)
        self.equipment_form.clear()
        self.equipment_form.add_item(self.equipment_type,self.current_equipment,self.close_click,self.cancel_click,self.edit_click,self.save_click)
        if self.current_equipment.isempty():
            self.equipment_form.set_edit()
        else:
            self.equipment_form.set_view()

    def close_click(self):
        if not self.rollback_equipment.equals(self.current_equipment):
            #confirm save
            self.save_click()
        
        self.equipment_window.destroy()
        self.equipment_form = None
        close_callback()

    def edit_click(self):
        self.equipment_form.set_edit()

    def save_click(self):
        self.current_equipment.name = self.equipment_form.f1.ename.get()
        self.current_equipment.short_description = self.equipment_form.f1.eshortdescription.get()
        self.current_equipment.description = self.equipment_form.f1.txtdescription.get("1.0",'end-1c')
        self.current_equipment.cost = self.equipment_form.f1.ecost.get()
        self.current_equipment.weight = self.equipment_form.f1.eweight.get()

        self.rollback_equipment = self.current_equipment.clone()
        self.save_callback(current_equipment)
        self.equipment_form.set_view()

    def cancel_click(self):
        if self.rollback_equipment.equals(self.current_equipment):
            #confirm rollback
            self.current_equipment = self.rollback_equipment
            self.refresh_data()

        self.equipment_form.set_view()

    def get_current_equipment(self):
        return self.current_equipment

    def get_equipment_form(self):
]       return self.equipment_form

    def __init__(self):
        self.create_form()