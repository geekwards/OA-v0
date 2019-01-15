import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Base_Form
import List_Object
import GUI_Select_Set_Controller

class Base_controller:
    def create_form(self,parent=None):
        raise NotImplementedError("Please Implement this method")

    def set_form(self,dataform):
        self.data_form = dataform

    def set_data(self,loaded_data):
        self.current_data = loaded_data.clone()
        self.rollback_data = loaded_data.clone()

    def setup_form(self,loaded_data,name,lookups,save_call,edit_call,close_call,cancel_call):
        self.save_callback = save_call
        self.edit_callback = edit_call
        self.close_callback = close_call
        self.cancel_callback = cancel_call
        self.current_data = loaded_data.clone()
        self.rollback_data = loaded_data.clone()
        self.lookup_data = lookups
        self.data_form.setup_form(name,lookups,self.launch_picker)

    def load_form(self):
        self.data_form.clear_form()
        self.data_form.add_item(self.current_data,self.close_click,self.cancel_click,self.edit_click,self.save_click)
        if self.current_data.isempty():
            self.data_form.set_edit()
        else:
            self.data_form.set_view()

    def launch_form(self):
        self.data_window.mainloop()

    def close_click(self):
        if not self.rollback_data == self.current_data:
            self.save_click()
        
        self.data_window.destroy()
        self.data_form = None
        self.close_callback()

    def edit_click(self):
        self.data_form.set_edit()

    def save_click(self):
        self.save_callback(self.current_data)

    def cancel_click(self):
        if self.rollback_data == self.current_data:
            self.current_data = self.rollback_data
            self.load_form()

        self.data_form.set_view()

    def launch_picker(self,type):
        raise NotImplementedError("Please Implement this method")

    def save_picker(self,type,list):
        raise NotImplementedError("Please Implement this method")
        
    def get_current_data(self):
        return self.current_data

    def get_data_form(self):
        return self.data_form

    def __init__(self):
        self.create_form()