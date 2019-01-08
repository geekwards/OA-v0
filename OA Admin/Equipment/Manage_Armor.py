import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Armor
import List_Object
import GUI_Equipment_Controller

class Manage_armor:
    current_set
    loaded_set
    sup_gui
    list_controller

    def save_armor(self,armor,fullsave=False):
        self.current_set.update(armor)
        if fullsave:
            self.save_armors()

    def save_armors(self,filename=None,backup_filename=None):
        if not self.current_set.equals(self.loaded_set):
            data=ET.Element('armor')
            for marmor in self.current_set.all_armors:
                l=ET.SubElement(data,'armorType')
                ET.SubElement(l,'name').text = marmor.name
                ET.SubElement(l,'shortDescription').text = marmor.short_description
                ET.SubElement(l,'description').text = marmor.description
                ET.SubElement(l,'cost').text = marmor.cost
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

    def remove_armor(self,armor):
        self.current_set.remove(armor)

    def close_edit_armor(self):
        self.launch_armor_list(self.sup_gui)

    def launch_edit_armor(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        armor_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            armor = self.current_set.get_armor(name)
        else:
            armor = Armor.Armor('','')

        if supress_gui:
            return armor_controller
        else:
            armor_controller.load_data('Armor',armor,self.save_armor,self.close_edit_armor)
    
    def launch_armor_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Armors',self.current_set.list_of_armors,self.launch_edit_armor,self.remove_armor,self.save_armors)

    def load_armors(self,filename=None):
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
            new_armor.cost = armor.find('cost').text or 0
            new_armor.weight = armor.find('weight').text or 0
            new_armor.health = armor.find('health').text or 0
            new_armor.capacity = armor.find('capacity').text or 0
            new_armor.special = armor.find('special').text or 'none'
            for dt in armor.findall('damageTypes/damageType'):
                dmgtype = List_Object.List_object(dt.attrib.get('name'),dt.text)
                new_armor.damage_types.append(dmgtype)
            self.current_set.add_new(new_armor)

        self.loaded_set = self.current_set.clone()

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None

if __name__ == '__main__':
    manager = Manage_armor()

    manager.load_armors()
    manager.launch_armor_list()
