import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import GUI_Archtype_Controller
import Archtype

class Manage_archtypes:
    def save_archtype(self,archtype,fullsave=False):
        global current_set

        current_set.update(archtype)
        if fullsave:
            self.save_archtypes()

    def save_archtypes(self,filename=None,backup_filename=None):
        global current_set
        global loaded_set

        if not(loaded_set.equals(current_set)):
            data=ET.Element('archtypes')
            for item in current_set.all_archtypes:
                arch=ET.SubElement(data,'archtype')
                ET.SubElement(arch,'name').text = item.name
                ET.SubElement(arch,'shortDescription').text = item.short_description
                ET.SubElement(arch,'description').text = item.description
                ET.SubElement(arch,'proficiency').text = item.proficiency
                ET.SubElement(arch,'strBonus').text = item.str_bonus
                ET.SubElement(arch,'perBonus').text = item.per_bonus
                ET.SubElement(arch,'intBonus').text = item.int_bonus
                ET.SubElement(arch,'dexBonus').text = item.dex_bonus
                ET.SubElement(arch,'chaBonus').text = item.cha_bonus
                ET.SubElement(arch,'vitBonus').text = item.vit_bonus
                ET.SubElement(arch,'magBonus').text = item.mag_bonus
                ET.SubElement(arch,'staminaBonus').text = item.stamina_bonus
                ET.SubElement(arch,'attackBonus').text = item.attack_bonus
                ET.SubElement(arch,'reflexBonus').text = item.reflex_bonus
                ET.SubElement(arch,'feats').text = item.feats
                ET.SubElement(arch,'movement').text = item.movement
                ET.SubElement(arch,'skillPoints').text = item.skill_points
                ET.SubElement(arch,'levelHealth').text = item.level_health

            if filename == None:
                filename = app_config.file_path + app_config.archive_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_archive_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_archtype(self,archtype):
        global current_set

        current_set.remove(archtype)

    def launch_edit_archtype(self,parent,name,supress_gui=False):
        global current_set

        archtype_controller = GUI_Archtype_Controller.GUI_archtype_controller()

        if supress_gui:
            return archtype_controller
        else:
            archtype_controller.load_data(current_set.get_archtype(name),self.save_archtype)
            self.launch_archtype_list()

    def launch_archtype_list(self,supress_gui=False):
        global current_set
        global list_controller

        if list_controller == None:
            list_controller = GUI_List_Controller.GUI_list_controller()

        if supress_gui:
            return list_controller
        else:
            list_controller.load_data('Archtypes',current_set.list_of_archtypes,self.launch_edit_archtype,self.remove_archtype,self.save_archtypes)

    def load_archtypes(self,filename=None):
        global current_set
        global loaded_set

        current_set = Archtype.Archtypes()

        if filename == None:
            filename = app_config.file_path + app_config.archive_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for archtype in data_root:
            current_archtype = Archtype.Archtype(archtype.find('name').text,archtype.find('shortDescription').text)
            current_archtype.description = archtype.find('description').text
            current_archtype.proficiency = archtype.find('proficiency').text
            current_archtype.str_bonus = archtype.find('strBonus').text
            current_archtype.per_bonus = archtype.find('perBonus').text
            current_archtype.int_bonus = archtype.find('intBonus').text
            current_archtype.dex_bonus = archtype.find('dexBonus').text
            current_archtype.cha_bonus = archtype.find('chaBonus').text
            current_archtype.vit_bonus = archtype.find('vitBonus').text
            current_archtype.mag_bonus = archtype.find('magBonus').text
            current_archtype.stamina_bonus = archtype.find('staminaBonus').text
            current_archtype.attack_bonus = archtype.find('attackBonus').text
            current_archtype.reflex_bonus = archtype.find('reflexBonus').text
            current_archtype.feats = archtype.find('feats').text
            current_archtype.movement = archtype.find('movement').text
            current_archtype.skill_points = archtype.find('skillPoints').text
            current_archtype.level_health = archtype.find('levelHealth').text
            current_set.add_new(current_archtype)

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
    manager = Manage_archtypes()

    manager.load_archtypes()
    manager.launch_archtype_list()
