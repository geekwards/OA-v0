import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller

class Manage_data:
    def save_one(self,item,filename=None,backup_filename=None):
        self.current_set.update(item)
        if filename != None:
            self.save_all(filename,backup_filename)

    def save_all(self,filename=None,backup_filename=None):
        raise NotImplementedError("Please Implement this method")

    def remove_item(self,item):
        self.current_set.remove(item)

    def close_edit_item(self):
        return self.launch_list(self.name,None)

    def launch_edit(self,name,parent=None):
        raise NotImplementedError("Please Implement this method")

    def launch_list(self,name,parent=None):
        self.name = name
        self.list_controller.create_form(parent)
        self.list_controller.load_data(name,self.current_set.list_of_items,self.launch_edit,self.remove_item,self.save_all)

    def load_set(self,filename=None):
        raise NotImplementedError("Please Implement this method")

    def set_controller(self):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None
