import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config

import GUI_Archtype_Form

class GUI_archtype_controller:
    def create_form(self,parent=None):
        global archtype_form
        global archtype_window

        archtype_form,archtype_window = GUI_Archtype_Form.create_archtype_form(parent)

    def load_data(self,loaded_archtype,save_call,supress_gui=False):
        global current_archtype
        global rollback_archtype
        global save_callback
        global archtype_form
        global archtype_window
    
        save_callback = save_call

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

        if not rollback_archtype.equals(current_archtype):
            #confirm save
            self.save_click()
        
        archtype_window.destroy()
        archtype_form = None

    def edit_click(self):
        global archtype_form

        archtype_form.set_edit()

    def save_click(self):
        global save_callback
        global archtype_form

        save_callback()
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