import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config

import GUI_Misc_List_Form

class GUI_misc_list_controller:
    def create_form(self,parent=None):
        global misc_list_form
        global misc_list_window

        misc_list_form,misc_list_window = GUI_Misc_List_Form.create_misc_list_form(parent)

    def load_data(self,loaded_misc_list,save_call,supress_gui=False):
        global current_misc_list
        global rollback_misc_list
        global save_callback
        global misc_list_form
        global misc_list_window

        save_callback = save_call

        current_misc_list = loaded_misc_list
        rollback_misc_list = loaded_misc_list.clone()
        misc_list_form.setup(current_misc_list.name,self.new_click,self.close_click,self.edit_click,self.save_click,self.cancel_click)
        self.refresh_data()
        if supress_gui:
            return misc_list_form
        else:
            misc_list_window.mainloop()

    def refresh_data(self):
        global current_misc_list
        global misc_list_form

        misc_list_form.clear()
        index=0
        for list_item in current_misc_list.all_items:
            misc_list_form.add_item(index,list_item)
            index += 1

        misc_list_form.set_view()

    def new_click(self):
        return False

    def close_click(self):
        global current_misc_list
        global rollback_misc_list
        global misc_list_form
        global misc_list_window

        if not rollback_misc_list.equals(current_misc_list):
            #confirm save
            self.save_click()
        
        misc_list_window.destroy()
        misc_list_form = None

    def edit_click(self):
        global misc_list_form

        misc_list_form.set_edit()

    def save_click(self):
        global save_callback
        global misc_list_form

        save_callback()
        misc_list_form.set_view()

    def cancel_click(self):
        global current_misc_list
        global rollback_misc_list
        global misc_list_form

        if rollback_misc_list.equals(current_misc_list):
            #confirm rollback
            current_misc_list = rollback_misc_list
            self.refresh_data()

        misc_list_form.set_view()

    def get_current_misc_list(self):
        global current_misc_list

        return current_misc_list

    def get_misc_list_form(self):
        global misc_list_form

        return misc_list_form

    def __init__(self):
        self.create_form()