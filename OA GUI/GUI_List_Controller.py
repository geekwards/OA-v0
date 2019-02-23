
import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')
import app_config

import List_Object
import GUI_List_Form

class GUI_list_controller:
    def create_form(self,parent=None):
        self.list_form, self.list_window = GUI_List_Form.create_list_form(parent)
        
    def load_data(self,title,loaded_list,edit_call,remove_call,close_call,set_edit=True):
        self.current_list = loaded_list
        self.edit_callback = edit_call
        self.remove_callback = remove_call
        self.close_callback = close_call
        self.list_form.setup_form(title,self.new_call,self.edit_call,self.remove_call,self.close_call,set_edit)
        self.list_form.clear_frame()
        index=0
        for item in self.current_list:
            self.list_form.add_item(index,item.list_text,set_edit)
            index += 1
        self.list_window.mainloop()

    def new_call(self):
        self.edit_call(None)

    def edit_call(self,idx=None):
        if idx==None:
            name = ''
        else:
            name = self.current_list[idx].name

        self.edit_callback(name,self.list_window)

    def save_call(self):
        raise NotImplementedError

    def close_call(self):
        if self.close_callback != None:
            self.close_callback()
        self.list_window.destroy()
        self.list_form = None

    def cancel_call(self):
        raise NotImplementedError

    def get_current_set(self):
        return self.current_list

    def get_form(self):
        return self.list_form

    def get_window(self):
        return self.list_window

    def remove_call(self,idx=None):
        #todo: confirm remove item
        if idx != None:
            self.remove_callback(self.current_list[idx])
            self.list_form.clear_frame()
            self.list_form.build_frame()

    def __init__(self,parent=None):
        self.create_form(parent)
