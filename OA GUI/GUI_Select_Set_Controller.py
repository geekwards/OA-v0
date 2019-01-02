import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Select_Set_Form

class GUI_select_set_controller:
    def create_form(self,parent=None):
        global select_set_form
        global select_set_window

        select_set_form,select_set_window = GUI_Select_Set_Form.create_select_set_form(parent)

    def load_sets(self,title,full_list,selected,save_call,supress_gui=False):
        global select_set_form
        global select_set_window
        global save_callback

        save_callback = save_call

        src_list = [e for e in full_list if e not in selected]

        select_set_form.add_lists(title,src_list,selected,self.cancel_click,self.save_click)
        if supress_gui:
            return select_set_form
        else:
            select_set_window.mainloop()

    def save_click(self):
        global select_set_form
        global save_callback

        save_callback(select_set_form.lstselected.get(0,'end'))

    def cancel_click(self):
        global select_set_form
        global select_set_window

        select_set_window.destroy()
        select_set_form = None
 
    def get_select_set_form(self):
        global select_set_form

        return select_set_form

    def __init__(self):
        self.create_form()