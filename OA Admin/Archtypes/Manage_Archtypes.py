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
    current_set
    loaded_set
    sup_gui
    list_controller

    def save_archtype(self,archtype,fullsave=False):
        self.current_set.update(archtype)
        if fullsave:
            self.save_archtypes()

    def save_archtypes(self,filename=None,backup_filename=None):
        if not(self.loaded_set.equals(self.current_set)):
            data=ET.Element('archtypes')
            for item in self.current_set.all_archtypes:
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
                filename = app_config.file_path + app_config.archtype_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_archtype_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_archtype(self,archtype):
        self.current_set.remove(archtype)

    def close_edit_archtype(self):
        self.launch_archtype_list(self.sup_gui)

    def launch_edit_archtype(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        archtype_controller = GUI_Archtype_Controller.GUI_archtype_controller()

        if supress_gui:
            return archtype_controller
        else:
            archtype_controller.load_data(self.current_set.get_archtype(name),self.save_archtype,self.close_edit_archtype)

    def launch_archtype_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()

        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Archtypes',self.current_set.list_of_archtypes,self.launch_edit_archtype,self.remove_archtype,self.save_archtypes)

    def load_archtypes(self,filename=None):
        self.current_set = Archtype.Archtypes()

        if filename == None:
            filename = app_config.file_path + app_config.archtype_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for archtype in data_root:
            name = archtype.find('name').text or 'UNKNOWN'
            short_descrp = archtype.find('shortDescription').text or ' '
            current_archtype = Archtype.Archtype(name,short_descrp)
            current_archtype.description = archtype.find('description').text or ' '
            current_archtype.proficiency = archtype.find('proficiency').text or ' '
            current_archtype.str_bonus = archtype.find('strBonus').text or 0
            current_archtype.per_bonus = archtype.find('perBonus').text or 0
            current_archtype.int_bonus = archtype.find('intBonus').text or 0
            current_archtype.dex_bonus = archtype.find('dexBonus').text or 0
            current_archtype.cha_bonus = archtype.find('chaBonus').text or 0
            current_archtype.vit_bonus = archtype.find('vitBonus').text or 0
            current_archtype.mag_bonus = archtype.find('magBonus').text or 0
            current_archtype.stamina_bonus = archtype.find('staminaBonus').text or 0
            current_archtype.attack_bonus = archtype.find('attackBonus').text or 0
            current_archtype.reflex_bonus = archtype.find('reflexBonus').text or 0
            current_archtype.feats = archtype.find('feats').text or 0
            current_archtype.movement = archtype.find('movement').text or 0
            current_archtype.skill_points = archtype.find('skillPoints').text or 0
            current_archtype.level_health = archtype.find('levelHealth').text or ' '
            self.current_set.add_new(current_archtype)

        self.loaded_set = self.current_set.clone()

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None

if __name__ == '__main__':
    manager = Manage_archtypes()

    manager.load_archtypes()
    manager.launch_archtype_list()
