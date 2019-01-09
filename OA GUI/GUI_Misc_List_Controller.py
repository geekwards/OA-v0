import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import Misc_List
import GUI_Misc_List_Form
import List_Object

class GUI_misc_list_controller:
    misc_list_form = None
    misc_list_window = None
    current_misc_list = None
    rollback_misc_list = None
    save_callback = None
    close_callback = None

    def create_form(self,parent=None):
        self.misc_list_form,self.misc_list_window = GUI_Misc_List_Form.create_misc_list_form(parent)

    def load_data(self,loaded_misc_list,save_call,close_call,supress_gui=False):
        self.save_callback = save_call
        self.close_callback = close_call

        self.current_misc_list = loaded_misc_list
        self.rollback_misc_list = loaded_misc_list.clone()
        self.misc_list_form.setup(self.current_misc_list.name,self.new_click,self.close_click,self.edit_click,self.save_click,self.cancel_click)
        self.refresh_data()
        if supress_gui:
            return self.misc_list_form
        else:
            self.misc_list_window.mainloop()

    def refresh_data(self):
        self.misc_list_form.clear()
        index=0
        if len(self.current_misc_list) > 0:
            for list_item in self.current_misc_list.all_items:
                self.misc_list_form.add_item(index,list_item)
                index += 1
    
            self.misc_list_form.set_view()
        else:
            self.misc_list_form.set_edit(True)

    def new_click(self):
        self.misc_list_form.add_item(len(self.misc_list_form.f1.winfo_children()),List_Object.List_object('',''))

    def close_click(self):
        if not self.rollback_misc_list.equals(self.current_misc_list):
            #confirm save
            self.save_click() 
        
        self.misc_list_window.destroy()
        self.misc_list_form = None
        self.close_callback()

    def edit_click(self):
        self.misc_list_form.set_edit()

    def save_click(self):
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

    def cancel_click(self):
        if not self.rollback_misc_list.equals(self.current_misc_list):
            #confirm rollback
            self.current_misc_list = self.rollback_misc_list
            self.refresh_data()

        self.misc_list_form.set_view()

    def get_current_misc_list(self):
        return self.current_misc_list

    def get_misc_list_form(self):
        return self.misc_list_form

    def __init__(self):
        self.create_form()