import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import GUI_Misc_List_Controller
import Misc_List
import List_Object

class Manage_misc_lists:
    def save_misc_list(self,misc_list,fullsave=False):
        global current_set

        current_set.update(misc_list)
        if fullsave:
            self.save_misc_lists

    def save_misc_lists(self,filename=None,backup_filename=None):
        global current_set

        if not current_set.equals(loaded_set):
            data=ET.Element('misc_lists')
            for mlist in current_set.all_lists:
                l=ET.SubElement(data,'list')
                ET.SubElement(l,'listname').text = mlist.name
                c=ET.SubElement(l,'items')
                for item in mlist.all_items:
                    i=ET.SubElement(c,'item')
                    ET.SubElement(i,'name').text = item.name
                    ET.SubElement(i,'description').text = item.short_description

            if filename == None:
                filename = app_config.file_path + app_config.misc_list_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_misc_list_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_misc_list(self,misc_list):
        global current_set

        current_set.remove(misc_list)

    def close_edit_misc_list(self):
        global sup_gui

        self.launch_misc_list_list(sup_gui)

    def launch_edit_misc_list(self,parent,name,supress_gui=False):
        global current_set
        global sup_gui

        sup_gui = supress_gui
        misc_list_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()            

        if len(name) > 0:
            misc_list = current_set.get_misc_list(name)
        else:
            misc_list = Misc_List.Misc_list('',[])

        if supress_gui:
            return misc_list_controller
        else:
            misc_list_controller.load_data(misc_list,self.save_misc_list,self.close_edit_misc_list)
    
    def launch_misc_list_list(self,supress_gui=False):
        global current_set
        global list_controller

        if list_controller == None:
            list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return list_controller
        else:
            list_controller.load_data('Misc Lists',current_set.list_of_lists,self.launch_edit_misc_list,self.remove_misc_list,self.save_misc_lists)

    def load_misc_lists(self,filename=None):
        global current_set
        global loaded_set

        current_set = Misc_List.Misc_lists()   

        if filename == None:
            filename = app_config.file_path + app_config.misc_list_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for misc_list in data_root:
            new_list_name = misc_list.find('listname').text

            new_list_items = []

            for misc_list_item in misc_list.findall('items/item'):
                item_name = misc_list_item.find('name').text
                item_short_desc = misc_list_item.find('description').text
                new_list_items.append(List_Object.List_object(item_name,item_short_desc))

            new_list = Misc_List.Misc_list(new_list_name,new_list_items)
            current_set.add_new(new_list)

        loaded_set = current_set.clone()

    def get_current_set(self):
        global current_set

        return current_set

    def __init__(self):
        global current_set
        global list_controller

        list_controller = None
        current_set = None

if __name__ == '__main__':
    manager = Manage_misc_lists()

    manager.load_misc_lists()
    manager.launch_misc_list_list()
