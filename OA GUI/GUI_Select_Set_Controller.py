import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Select_Set_Form

class GUI_select_set_controller:
    select_set_form
    select_set_window
    save_callback
    sel_list

    def create_form(self,parent=None):
        self.select_set_form = None
        self.select_set_window = None
        self.save_callback = None
        self.sel_list = None

        self.select_set_form,self.select_set_window = GUI_Select_Set_Form.create_select_set_form(parent)

    def load_sets(self,title,full_list,selected,save_call,score=False,supress_gui=False):
        self.save_callback = save_call
        self.sel_list = selected

        self.select_set_form.add_lists(title,full_list,selected,self.cancel_click,self.save_click,score)
        if supress_gui:
            return self.select_set_form
        else:
            self.select_set_window.mainloop()

    def save_click(self):
        save_list = select_set_form.f1.lstselected.get(0,'end')
        save_list = sorted(save_list)
        self.sel_list = sorted(self.sel_list)
        will_save = False
        for idx,item in enumerate(save_list):
            will_save = will_save or (item != sel_list[idx])

        if will_save:
            self.save_callback(select_set_form.lbltitle.cget('text'),select_set_form.f1.lstselected.get(0,'end'))

    def cancel_click(self):
        self.destroy_select_set()

    def destroy_select_set(self):
        self.select_set_window.destroy()
        self.select_set_form = None

    def get_select_set_form(self):
        return self.select_set_form

    def __init__(self):
        self.create_form()