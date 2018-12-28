
import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')
import app_config

import List_Object
import GUI_List_Form

class GUI_list_controller:
    def create_form(self,parent=None):
        global list_form
        global list_window

        list_form, list_window = GUI_List_Form.create_list_form(parent)
        
    def load_data(self,title,loaded_list,edit_call,remove_call,close_call,supress_gui=False):
        global current_list
        global edit_callback
        global remove_callback
        global close_callback
        global list_form
        global list_window

        current_list = loaded_list
        edit_callback = edit_call
        remove_callback = remove_call
        close_callback = close_call

        if list_form != None:
            list_form.setup(title,self.new_click,self.edit_click,self.remove_click,self.close_click)
            self.refresh_data()
            if supress_gui:
                return list_form
            else:
                list_window.mainloop()

    def refresh_data(self):
        global current_list
        global list_form

        list_form.clear()
        index=0
        for item in current_list:
            list_form.add_item(index,item.list_text)
            index += 1

    def close_click(self):
        global current_list
        global list_form
        global list_window
        global close_callback

        if close_callback != None:
            close_callback()
        list_window.destroy()
        list_form = None

    def new_click(self):
        self.edit_click(None)

    def edit_click(self,idx):
        global edit_callback
        global current_list
        global list_window

        if idx==None:
            name = ''
        else:
            name = current_list[idx].name

        edit_callback(list_window,name)

    def remove_click(self,idx):
        global remove_callback
        global current_list

        #todo: confirm remove item
        remove_callback(current_list[idx])
        self.refresh_data()

    def get_list_form(self):
        global list_form

        return list_form

    def get_current_list(self):
        global current_list

        return current_list

    def __init__(self):
        self.create_form()
