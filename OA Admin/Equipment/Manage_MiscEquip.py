import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Misc_Equipment
import List_Object
import GUI_Equipment_Controller

class Manage_misc_equipment:
    def save_stuff(self,stuff,fullsave=False):
        global current_set

        current_set.update(stuff)
        if fullsave:
            self.save_misc_equipment()

    def save_misc_equipment(self,filename=None,backup_filename=None):
        global current_set

        if not current_set.equals(loaded_set):
            data=ET.Element('miscEquipment')
            for mclothing in current_set.all_clothes:
                l=ET.SubElement(data,'equip')
                ET.SubElement(l,'name').text = mclothing.name
                ET.SubElement(l,'shortDescription').text = mclothing.short_description
                ET.SubElement(l,'description').text = mclothing.description
                ET.SubElement(l,'cost').text = mclothing.cost
                ET.SubElement(l,'weight').text = mclothing.weight
                ET.SubElement(l,'health').text = mclothing.health
                ET.SubElement(l,'capacity').text = mclothing.capacity
                ET.SubElement(l,'special').text = mclothing.special
 
            if filename == None:
                filename = app_config.file_path + app_config.misc_equip_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_misc_equip_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_stuff(self,stuff):
        global current_set

        current_set.remove(stuff)

    def close_edit_stuff(self):
        global sup_gui

        self.launch_misc_equipment_list(sup_gui)

    def launch_edit_stuff(self,parent,name,supress_gui=False):
        global current_set
        global sup_gui

        sup_gui = supress_gui
        misc_equipment_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            stuff = current_set.get_stuff(name)
        else:
            stuff = Misc_Equipment.Stuff('','')

        if supress_gui:
            return misc_equipment_controller
        else:
            misc_equipment_controller.load_data('Misc Equipment',stuff,self.save_stuff,self.close_edit_stuff)
    
    def launch_misc_equipment_list(self,supress_gui=False):
        global current_set
        global list_controller

        if list_controller == None:
            list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return list_controller
        else:
            list_controller.load_data('Misc Equipment',current_set.list_of_misc_equipment,self.launch_edit_stuff,self.remove_stuff,self.save_stuff)

    def load_misc_equipment(self,filename=None):
        global current_set
        global loaded_set

        current_set = Misc_Equipment.Misc_equipment()   

        if filename == None:
            filename = app_config.file_path + app_config.misc_equip_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for stuff in data_root:
            new_stuff_name = stuff.find('name').text or 'UNKNOWN'
            new_stuff_short_description = stuff.find('shortDescription').text or 'UNKNOWN'
            new_stuff = Misc_Equipment.Stuff(new_stuff_name,new_stuff_short_description)
            new_stuff.description = stuff.find('description').text or 'UNKNOWN'
            new_stuff.cost = stuff.find('cost').text or 0
            new_stuff.weight = stuff.find('weight').text or 0
            new_stuff.health = stuff.find('health').text or 0
            new_stuff.capacity = stuff.find('capacity').text or 0
            new_stuff.speical = stuff.find('special').text or 'none'
            current_set.add_new(new_stuff)

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
    manager = Manage_misc_equipment()

    manager.load_misc_equipment()
    manager.launch_misc_equipment_list()
