import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import GUI_Misc_List_Controller
import Misc_List
import List_Object

class Manage_misc_lists(Base_Manage_Data.Manage_data):
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('misc_lists')
            for mlist in self.current_set.all_items:
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

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        misc_list_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()            

        if len(name) > 0:
            misc_list = self.current_set.get_item(name)
        else:
            misc_list = Misc_List.Misc_list('',[])

        if supress_gui:
            return misc_list_controller
        else:
            misc_list_controller.load_data(misc_list,self.save_misc_list,self.close_edit_misc_list)

    def load_set(self,filename=None):
        self.current_set = Misc_List.Misc_lists()   

        if filename == None:
            filename = app_config.file_path + app_config.misc_list_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for misc_list in data_root:
            new_list_name = misc_list.find('listname').text or 'UNKNOWN'

            new_list_items = []

            for misc_list_item in misc_list.findall('items/item'):
                item_name = misc_list_item.find('name').text or ' ' 
                item_short_desc = misc_list_item.find('description').text or ' '
                new_list_items.append(List_Object.List_object(item_name,item_short_desc))

            new_list = Misc_List.Misc_list(new_list_name,'',new_list_items)
            self.current_set.add_new(new_list)

        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Misc Lists'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_misc_lists()

    manager.load_misc_lists()
    manager.launch_misc_list_list()
