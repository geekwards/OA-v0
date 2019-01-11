import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import GUI_Focus_Controller
import Manage_Misc_Lists
import Focus
import List_Object
import Misc_List

class Manage_foci:
    current_set
    loaded_set
    list_controller
    sup_gui

    def save_focus(self,focus,fullsave=False):
        self.current_set.update(focus)
        if fullsave:
            self.save_foci()

    def save_foci(self,filename=None,backup_filename=None):
        if not(self.loaded_set.equals(self.current_set)):
            data=ET.Element('foci')
            for item in self.current_set.all_foci:
                r=ET.SubElement(data,'focus')
                ET.SubElement(r,'name').text = item.name
                ET.SubElement(r,'shortDescription').text = item.short_description
                ET.SubElement(r,'description').text = item.description
                ET.SubElement(r,'strBonus').text = item.str_bonus
                ET.SubElement(r,'perBonus').text = item.per_bonus
                ET.SubElement(r,'intBonus').text = item.int_bonus
                ET.SubElement(r,'dexBonus').text = item.dex_bonus
                ET.SubElement(r,'chaBonus').text = item.cha_bonus
                ET.SubElement(r,'vitBonus').text = item.vit_bonus
                ET.SubElement(r,'magBonus').text = item.mag_bonus
                ET.SubElement(r,'strSkill').text = item.str_bonus
                ET.SubElement(r,'perSkill').text = item.per_bonus
                ET.SubElement(r,'intSkill').text = item.int_bonus
                ET.SubElement(r,'dexSkill').text = item.dex_bonus
                ET.SubElement(r,'chaSkill').text = item.cha_bonus
                ET.SubElement(r,'vitSkill').text = item.vit_bonus
                ET.SubElement(r,'magSkill').text = item.mag_bonus
                ET.SubElement(r,'willBonus').text = item.will_bonus
                ET.SubElement(r,'fortitudeBonus').text = item.fortitude_bonus
                ET.SubElement(r,'reflexBonus').text = item.reflex_bonus
                l=ET.SubElement(r,'languagesBonus')
                for lang in item.languages_bonus:
                    ET.SubElement(l,'language',name=lang.name).text = lang.short_description

            if filename == None:
                filename = app_config.file_path + app_config.focus_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_focus_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_focus(self,focus):
        self.current_set.remove(focus)

    def close_edit_focus(self):
        self.launch_focus_list(self.sup_gui)

    def launch_edit_focus(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()

        if supress_gui:
            return focus_controller
        else:
            focus_controller.load_lookups(languages)
            focus_controller.load_data(self.current_set.get_focus(name),self.save_focus,self.close_edit_focus)

    def launch_focus_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()

        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Foci',self.current_set.list_of_foci,self.launch_edit_focus,self.remove_focus,self.save_foci)

    def load_foci(self,filename=None):
        self.current_set = Focus.Foci()

        if filename == None:
            filename = app_config.file_path + app_config.focus_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for focus in data_root:
            name = focus.find('name').text or 'UNKNOWN'
            current_focus = Focus.Focus(name)
            current_focus.short_description = focus.find('shortDescription').text or ' '
            current_focus.description = focus.find('description').text or ' ' 
            current_focus.str_bonus = focus.find('strBonus').text or 0
            current_focus.per_bonus = focus.find('perBonus').text or 0
            current_focus.int_bonus = focus.find('intBonus').text or 0
            current_focus.dex_bonus = focus.find('dexBonus').text or 0
            current_focus.cha_bonus = focus.find('chaBonus').text or 0
            current_focus.vit_bonus = focus.find('vitBonus').text or 0
            current_focus.mag_bonus = focus.find('magBonus').text or 0
            current_focus.str_skill_bonus = focus.find('strSkill').text or 0
            current_focus.per_skill_bonus = focus.find('perSkill').text or 0
            current_focus.int_skill_bonus = focus.find('intSkill').text or 0
            current_focus.dex_skill_bonus = focus.find('dexSkill').text or 0
            current_focus.cha_skill_bonus = focus.find('chaSkill').text or 0
            current_focus.vit_skill_bonus = focus.find('vitSkill').text or 0
            current_focus.mag_skill_bonus = focus.find('magSkill').text or 0
            current_focus.will_bonus = focus.find('willBonus').text or 0
            current_focus.fortitude_bonus = focus.find('fortitudeBonus').text or 0
            current_focus.reflex_bonus = focus.find('reflexBonus').text or 0
            for language in focus.findall('languagesBonus/language'):
                lang = List_Object.List_object(language.attrib.get('name'),language.text)
                current_focus.languages_bonus.append(lang)
            self.current_set.add_new(current_focus)

        self.loaded_set = self.current_set.clone()

    def load_combo_data(self):
        misc_lists = Manage_Misc_Lists.Manage_misc_lists()
        misc_lists.load_misc_lists()
        languages = Misc_List.Misc_lists()
        languages.add_new(misc_lists.get_current_set().get_misc_list('Languages').clone())

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        list_controller = None        
        current_set = None
        loaded_set = None
        self.load_combo_data()

if __name__ == '__main__':
    manager = Manage_foci()

    manager.load_foci()
    manager.launch_focus_list()
