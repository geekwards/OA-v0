
import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')
import app_config

import List_Object
import GUI_List_Form

class GUI_list_controller:
    list_form
    list_window
    current_list
    edit_callback
    remove_callback
    close_callback
    set_edit

    def create_form(self,parent=None):
        self.list_form = None
        self.list_window = None
        self.current_list = None
        self.edit_callback = None
        self.remove_callback = None
        self.close_callback = None
        self.set_edit = None
        self.list_form, self.list_window = GUI_List_Form.create_list_form(parent)
        self.set_edit(True)
        
    def load_data(self,title,loaded_list,edit_call,remove_call,close_call,supress_gui=False):
        self.current_list = loaded_list
        self.edit_callback = edit_call
        self.remove_callback = remove_call
        self.close_callback = close_call

        if self.list_form != None:
            self.list_form.setup(title,self.new_click,self.edit_click,self.remove_click,self.close_click,set_edit)
            self.refresh_data()
            if supress_gui:
                return self.list_form
            else:
                self.list_window.mainloop()

    def refresh_data(self):
        self.list_form.clear()
        index=0
        for item in self.current_list:
            self.list_form.add_item(index,item.list_text,self.set_edit)
            index += 1

    def close_click(self):
        if self.close_callback != None:
            self.close_callback()
        self.list_window.destroy()
        self.list_form = None

    def new_click(self):
        self.edit_click(None)

    def edit_click(self,idx):
        if idx==None:
            name = ''
        else:
            name = self.current_list[idx].name

        self.edit_callback(self.list_window,name)

    def remove_click(self,idx):
        #todo: confirm remove item
        self.remove_callback(self.current_list[idx])
        self.refresh_data()

    def set_edit(self,value):
        self.set_edit = value

    def get_list_form(self):
        return self.list_form

    def get_current_list(self):
        return self.current_list

    def __init__(self):
        self.create_form()
