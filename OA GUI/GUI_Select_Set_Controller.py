import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Select_Set_Form

class GUI_select_set_controller:
    def create_form(self,parent=None):
        self.select_set_form,self.select_set_window = GUI_Select_Set_Form.create_form(parent)

    def load_data(self,title,full_list,selected,save_call,score=False,supress_gui=False):
        self.save_callback = save_call
        self.sel_list = selected
        self.select_set_form.add_lists(title,full_list,selected,self.cancel_click,self.save_click,score)

    def launch_form(self):
        self.select_set_window.mainloop()

    def save_call(self):
        save_list = self.select_set_form.f1.lstselected.get(0,'end')
        save_list = sorted(save_list)
        self.sel_list = sorted(self.sel_list)
        will_save = False
        for idx,item in enumerate(save_list):
            will_save = will_save or (item != self.sel_list[idx])

        if will_save:
            self.save_callback(self.select_set_form.lbltitle.cget('text'),self.select_set_form.f1.lstselected.get(0,'end'))

    def cancel_call(self):
        self.destroy_select_set()

    def get_form(self):
        return self.select_set_form

    def destroy_select_set(self):
        self.select_set_window.destroy()
        self.select_set_form = None

    def __init__(self):
        self.create_form()