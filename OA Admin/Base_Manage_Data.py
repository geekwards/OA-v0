import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller

class Manage_data:
    def save_one(self,item,fullsave=False):
        self.current_set.update(item)
        if fullsave:
            self.save_all()

    def save_all(self,filename=None,backup_filename=None):
        raise NotImplementedError("Please Implement this method")

    def remove_item(self,item):
        self.current_set.remove(item)

    def close_edit_item(self):
        self.launch_list(self.sup_gui)

    def launch_edit(self,parent,name,supress_gui=False):
        raise NotImplementedError("Please Implement this method")

    def launch_list(self,name,supress_gui=False):
        self.sup_gui = supress_gui
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()

        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data(name,self.current_set.list_of_items,self.launch_edit,self.remove_item,self.save_all)

    def load_set(self,filename=None):
        raise NotImplementedError("Please Implement this method")

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None
