import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Armor
import List_Object
import GUI_Equipment_Controller

class Manage_armor(Base_Manage_Data.Manage_data):
    def save_one(self,item,filename=None,backup_filename=None):
        if type(item) == Armor.Armor and not(item.isempty()):
            super().save_one(item,filename,backup_filename)
        else:
            raise ValueError('expected Armor object, instead got ' + str(type(item)))

    def remove_item(self,item):
        if type(item) == Armor.Armor and not(item.isempty()):
            super().remove_item(item)
        else:
            raise ValueError('expected Armor object, instead got ' + str(type(item)))

    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('armor')
            for marmor in self.current_set.all_items:
                l=ET.SubElement(data,'armorType')
                ET.SubElement(l,'name').text = marmor.name
                ET.SubElement(l,'shortDescription').text = marmor.short_description
                ET.SubElement(l,'description').text = marmor.description
                ET.SubElement(l,'value').text = marmor.value
                ET.SubElement(l,'weight').text = marmor.weight
                ET.SubElement(l,'health').text = marmor.health
                ET.SubElement(l,'capacity').text = marmor.capacity
                ET.SubElement(l,'special').text = marmor.special
                dt=ET.SubElement(l,'damageTypes')
                for damtyp in marmor.damage_types:
                    ET.SubElement(dt,'damageType',name=damtyp.name).text = damtyp.short_description
            if filename == None:
                filename = app_config.file_path + app_config.armor_filename
            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_armor_filename
            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def set_controller(self,parent=None):
        self.edit_controller = GUI_Equipment_Controller.GUI_equipment_controller(parent)
        super().set_controller()

    def launch_edit(self,name,parent=None):
        self.edit_controller.create_form(parent)
        if len(name) > 0:
            armor = self.current_set.get_item(name)
        else:
            armor = Armor.Armor('','')
        self.edit_controller.load_data('Armor',armor,self.save_one,self.close_edit_item)

    def load_set(self,filename=None):
        self.current_set = Armor.Armors()   
        if filename == None:
            filename = app_config.file_path + app_config.armor_filename
        tree = ET.parse(filename)
        data_root = tree.getroot()
        for armor in data_root:
            new_armor_name = armor.find('name').text or 'UNKNOWN'
            new_armor_short_description = armor.find('shortDescription').text or 'UNKNOWN'
            new_armor = Armor.Armor(new_armor_name,new_armor_short_description)
            new_armor.description = armor.find('description').text or 'UNKNOWN'
            new_armor.value = armor.find('value').text or 0
            new_armor.weight = armor.find('weight').text or 0
            new_armor.health = armor.find('health').text or 0
            new_armor.capacity = armor.find('capacity').text or 0
            new_armor.special = armor.find('special').text or 'none'
            for dt in armor.findall('damageTypes/damageType'):
                dmgtype = List_Object.List_object(dt.attrib.get('name'),dt.text)
                new_armor.damage_types.append(dmgtype)
            self.current_set.add_new(new_armor)
        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Armor'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_armor()
    manager.load_armors()
    manager.launch_armor_list()
