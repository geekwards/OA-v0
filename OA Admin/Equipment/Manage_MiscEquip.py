import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Misc_Equipment
import List_Object
import GUI_Equipment_Controller

class Manage_misc_equipment(Base_Manage_Data.Manage_data):
    def save_one(self,item,filename=None,backup_filename=None):
        if type(item) == Misc_Equipment.Misc_equip and not(item.isempty()):
            super().save_one(item,filename,backup_filename)
        else:
            raise ValueError('expected Misc_equip object, instead got ' + str(type(item)))

    def remove_item(self,item):
        if type(item) == Misc_Equipment.Misc_equip and not(item.isempty()):
            super().remove_item(item)
        else:
            raise ValueError('expected Misc_equip object, instead got ' + str(type(item)))
            
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('miscEquipment')
            for mequip in self.current_set.all_items:
                l=ET.SubElement(data,'equip')
                ET.SubElement(l,'name').text = mequip.name
                ET.SubElement(l,'shortDescription').text = mequip.short_description
                ET.SubElement(l,'description').text = mequip.description
                ET.SubElement(l,'value').text = mequip.value
                ET.SubElement(l,'weight').text = mequip.weight
                ET.SubElement(l,'health').text = mequip.health
                ET.SubElement(l,'capacity').text = mequip.capacity
                ET.SubElement(l,'special').text = mequip.special
            if filename == None:
                filename = app_config.file_path + app_config.misc_equip_filename
            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_misc_equip_filename
            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        misc_equipment_controller = GUI_Equipment_Controller.GUI_equipment_controller()            
        if len(name) > 0:
            stuff = self.current_set.get_item(name)
        else:
            stuff = Misc_Equipment.Stuff('','')
        if supress_gui:
            return misc_equipment_controller
        else:
            misc_equipment_controller.load_data('Misc Equipment',stuff,self.save_stuff,self.close_edit_stuff)

    def load_set(self,filename=None):
        self.current_set = Misc_Equipment.Misc_equipment()   
        if filename == None:
            filename = app_config.file_path + app_config.misc_equip_filename
        tree = ET.parse(filename)
        data_root = tree.getroot()
        for stuff in data_root:
            new_stuff_name = stuff.find('name').text or 'UNKNOWN'
            new_stuff_short_description = stuff.find('shortDescription').text or 'UNKNOWN'
            new_stuff = Misc_Equipment.Misc_equip(new_stuff_name,new_stuff_short_description)
            new_stuff.description = stuff.find('description').text or 'UNKNOWN'
            new_stuff.value = stuff.find('value').text or 0
            new_stuff.weight = stuff.find('weight').text or 0
            new_stuff.health = stuff.find('health').text or 0
            new_stuff.capacity = stuff.find('capacity').text or 0
            new_stuff.special = stuff.find('special').text or 'none'
            self.current_set.add_new(new_stuff)
        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Misc Equipment'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_misc_equipment()
    manager.load_misc_equipment()
    manager.launch_misc_equipment_list()
