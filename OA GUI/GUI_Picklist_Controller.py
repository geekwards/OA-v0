import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')

import app_config
import GUI_Picklist_Form
import List_Object

class GUI_picklist_controller:
    def create_form(self,parent=None):
        self.picklist_form,self.picklist_window = GUI_Picklist_Form.create_form(parent)

    def load_data(self,title,full_list,selected,save_call,score=False):
        self.save_callback = save_call
        if type(selected[0]) == List_Object.List_object:
            self.sel_list = []
            for item in selected:
                self.sel_list.append(item.name + ': ' + item.short_description)
        else:
            self.sel_list = selected
        self.picklist_form.add_lists(title,full_list,self.sel_list,self.cancel_call,self.save_call,score)

    def launch_form(self):
        self.picklist_window.mainloop()
 
    def save_call(self):
        save_list = self.picklist_form.f1.lstselected.get(0,'end')
        save_list = sorted(save_list)
        self.sel_list = sorted(self.sel_list)
        will_save = False
        for idx,item in enumerate(save_list):
            will_save = will_save or (item != self.sel_list[idx])
        if will_save:
            sel_set = []
            for sel_item in save_list:
                selitem = sel_item.split(': ')
                sel_set.append(List_Object.List_object(selitem[0],selitem[1]))
            self.save_callback(self.picklist_form.lbltitle.cget('text'),sel_set)

    def cancel_call(self):
        self.destroy_picklist()

    def get_selected(self):
        return self.sel_list

    def get_form(self):
        return self.picklist_form

    def destroy_picklist(self):
        self.picklist_form = None
        self.picklist_window.destroy()

    def __init__(self):
        self.create_form()