import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import Misc_List
import GUI_Misc_List_Form
import List_Object

class GUI_misc_list_controller:
    def create_form(self,parent=None):
        self.misc_list_form,self.misc_list_window = GUI_Misc_List_Form.create_form(parent)

    def load_data(self,loaded_misc_list,save_call,close_call,supress_gui=False):
        self.save_callback = save_call
        self.close_callback = close_call
        self.current_misc_list = loaded_misc_list
        self.rollback_misc_list = loaded_misc_list.clone()
        self.misc_list_form.setup_form(self.current_misc_list.name,self.new_call,self.edit_call,self.save_call,self.close_call,self.cancel_call)
        self.misc_list_form.clear_frame()
        index=0
        if len(self.current_misc_list) > 0:
            for list_item in self.current_misc_list.all_items:
                self.misc_list_form.add_item(index,list_item)
                index += 1
    
            self.misc_list_form.set_view()
        else:
            self.misc_list_form.set_edit(True)

    def launch_form(self):
        self.misc_list_window.mainloop()

    def new_call(self):
        self.misc_list_form.add_item(len(self.misc_list_form.f1.winfo_children()),List_Object.List_object('',''))

    def edit_call(self):
        self.misc_list_form.set_edit()

    def save_call(self):
        new_misc_list = []
        index = 0
        for item in self.misc_list_form.f1.winfo_children():
            if index%2 == 0:
                item_name = item.get()
            else:
                item_desc = item.get("1.0",'end-1c')
                new_misc_list.append(List_Object.List_object(item_name,item_desc))

            index += 1

        if len(self.current_misc_list.name) > 0:
            list_name = self.current_misc_list.name
        else:
            list_name = self.misc_list_form.etitle.get()

        self.current_misc_list = Misc_List.Misc_list(list_name,new_misc_list)
        self.rollback_misc_list = self.current_misc_list.clone()
        self.save_callback(self.current_misc_list)
        self.misc_list_form.set_view()

    def close_call(self):
        if not self.rollback_misc_list == self.current_misc_list:
            #confirm save
            self.save_click() 
        
        self.misc_list_window.destroy()
        self.misc_list_form = None
        self.close_callback()

    def cancel_call(self):
        if not self.rollback_misc_list == self.current_misc_list:
            #confirm rollback
            self.current_misc_list = self.rollback_misc_list
            self.refresh_data()

        self.misc_list_form.set_view()

    def get_current_set(self):
        return self.current_misc_list

    def get_form(self):
        return self.misc_list_form

    def __init__(self):
        self.create_form()