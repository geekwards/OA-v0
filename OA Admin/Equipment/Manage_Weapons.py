import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Weapon
import List_Object
import GUI_Equipment_Controller

class Manage_weapons(Base_Manage_Data.Manage_data):
    def save_one(self,item,filename=None,backup_filename=None):
        if type(item) == Weapon.Weapon and not(item.isempty()):
            super().save_one(item,filename,backup_filename)
        else:
            raise ValueError('expected Weapon object, instead got ' + str(type(item)))

    def remove_item(self,item):
        if type(item) == Weapon.Weapon and not(item.isempty()):
            super().remove_item(item)
        else:
            raise ValueError('expected Weapon object, instead got ' + str(type(item)))
            
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('weapons')
            for mweapon in self.current_set.all_items:
                l=ET.SubElement(data,'weapon')
                ET.SubElement(l,'name').text = mweapon.name
                ET.SubElement(l,'shortDescription').text = mweapon.short_description
                ET.SubElement(l,'description').text = mweapon.description
                ET.SubElement(l,'value').text = mweapon.value
                ET.SubElement(l,'weight').text = mweapon.weight
                ET.SubElement(l,'health').text = mweapon.health
                ET.SubElement(l,'capacity').text = mweapon.capacity
                ET.SubElement(l,'hands').text = mweapon.hands
                ET.SubElement(l,'weaponType').text = mweapon.weapon_type
                ET.SubElement(l,'range').text = mweapon.range
                ET.SubElement(l,'ammoType').text = mweapon.ammo_type
                ET.SubElement(l,'special').text = mweapon.special
                dt=ET.SubElement(l,'damageTypes')
                for dmgtype in mweapon.damage_types:
                    ET.SubElement(dt,'damageType',name=dmgtype.name).text = dmgtype.short_description
 
            if filename == None:
                filename = app_config.file_path + app_config.weapon_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_weapon_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        weapon_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            weapon = self.current_set.get_item(name)
        else:
            weapon = Weapon.Weapon('','')

        if supress_gui:
            return weapon_controller
        else:
            weapon_controller.load_data('Weapon',weapon,self.save_weapon,self.close_edit_weapon)

    def load_set(self,filename=None):
        self.current_set = Weapon.Weapons()   

        if filename == None:
            filename = app_config.file_path + app_config.weapon_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for weapon in data_root:
            new_weapon_name = weapon.find('name').text or 'UNKNOWN'
            new_weapon_short_description = weapon.find('shortDescription').text or 'UNKNOWN'
            new_weapon = Weapon.Weapon(new_weapon_name,new_weapon_short_description)
            new_weapon.description = weapon.find('description').text or 'UNKNOWN'
            new_weapon.value = weapon.find('value').text or 0
            new_weapon.weight = weapon.find('weight').text or 0
            new_weapon.health = weapon.find('health').text or 0
            new_weapon.capacity = weapon.find('capacity').text or 0
            new_weapon.hands = weapon.find('hands').text or 0
            new_weapon.weapon_type = weapon.find('weaponType').text or ''
            new_weapon.range = weapon.find('range').text or 0
            new_weapon.ammo_type = weapon.find('ammoType').text or ''
            new_weapon.special = weapon.find('special').text or 'none'
            for dt in weapon.findall('damageTypes/damageType'):
                dmgtype = List_Object.List_object(dt.attrib.get('name'),dt.text)
                new_weapon.damage_types.append(dmgtype)
            self.current_set.add_new(new_weapon)

        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Weapons'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_weapons()

    manager.load_weapons()
    manager.launch_weapon_list()
