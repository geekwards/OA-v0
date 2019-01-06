import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Equipment_Form

class GUI_equipment_controller:
    def create_form(self,parent=None):
        global equipment_form
        global equipment_window

        equipment_form,equipment_window = GUI_Equipment_Form.create_equipment_form(parent)

    def load_data(self,equip_type,loaded_equipment,save_call,close_call,supress_gui=False):
        global current_equipment
        global rollback_equipment
        global save_callback
        global equipment_form
        global equipment_window
        global close_callback
        global equipment_type
    
        save_callback = save_call
        close_callback = close_call
        current_equipment = loaded_equipment
        rollback_equipment = loaded_equipment.clone()
        equipment_type = equip_type
        self.refresh_data()
        if supress_gui:
            return equipment_form
        else:
            equipment_window.mainloop()

    def refresh_data(self):
        global current_equipment
        global equipment_form
        global equipment_type

        equipment_form.clear()
        equipment_form.configure_form(equipment_type)
        equipment_form.add_item(equipment_type,current_equipment,self.close_click,self.cancel_click,self.edit_click,self.save_click)
        if current_equipment.isempty():
            equipment_form.set_edit()
        else:
            equipment_form.set_view()

    def close_click(self):
        global current_equipment
        global rollback_equipment
        global equipment_form
        global equipment_window
        global close_callback

        if not rollback_equipment.equals(current_equipment):
            #confirm save
            self.save_click()
        
        equipment_window.destroy()
        equipment_form = None
        close_callback()

    def edit_click(self):
        global equipment_form

        equipment_form.set_edit()

    def save_click(self):
        global save_callback
        global equipment_form
        global current_equipment
        global rollback_equipment

        current_equipment.name = equipment_form.f1.ename.get()
        current_equipment.short_description = equipment_form.f1.eshortdescription.get()
        current_equipment.description = equipment_form.f1.txtdescription.get("1.0",'end-1c')
        current_equipment.cost = equipment_form.f1.ecost.get()
        current_equipment.weight = equipment_form.f1.eweight.get()

        rollback_equipment = current_equipment.clone()
        save_callback(current_equipment)
        equipment_form.set_view()

    def cancel_click(self):
        global current_equipment
        global rollback_equipment
        global equipment_form

        if rollback_equipment.equals(current_equipment):
            #confirm rollback
            current_equipment = rollback_equipment
            self.refresh_data()

        equipment_form.set_view()

    def get_current_equipment(self):
        global current_equipment

        return current_equipment

    def get_equipment_form(self):
        global equipment_form

        return equipment_form

    def __init__(self):
        self.create_form()