import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import GUI_Race_Controller
import Manage_Misc_Lists
import Race
import List_Object
import Misc_List
import Manage_Foci
 
class Manage_races(Base_Manage_Data.Manage_data):
    def save_all(self,filename=None,backup_filename=None):
        if not(self.loaded_set == self.current_set):
            data=ET.Element('races')
            for item in self.current_set.all_items:
                r=ET.SubElement(data,'race')
                ET.SubElement(r,'name').text = item.name
                ET.SubElement(r,'shortDescription').text = item.short_description
                ET.SubElement(r,'description').text = item.description
                ET.SubElement(r,'size').text = item.size
                ET.SubElement(r,'body').text = item.body
                fo1=ET.SubElement(r,'foci')
                for focus in item.foci:
                    ET.SubElement(fo1,'focus').text = focus
                fe1=ET.SubElement(r,'feats')
                for feat in item.feats:
                    ET.SubElement(fe1,'feat').text = feat
                ET.SubElement(r,'strBonus').text = item.str_bonus
                ET.SubElement(r,'perBonus').text = item.per_bonus
                ET.SubElement(r,'intBonus').text = item.int_bonus
                ET.SubElement(r,'dexBonus').text = item.dex_bonus
                ET.SubElement(r,'chaBonus').text = item.cha_bonus
                ET.SubElement(r,'vitBonus').text = item.vit_bonus
                ET.SubElement(r,'magBonus').text = item.mag_bonus
                ET.SubElement(r,'willBonus').text = item.will_bonus
                ET.SubElement(r,'fortitudeBonus').text = item.fortitude_bonus
                ET.SubElement(r,'reflexBonus').text = item.reflex_bonus
                l=ET.SubElement(r,'languagesBonus')
                for lang in item.languages_bonus:
                    ET.SubElement(l,'language',name=lang.name).text = lang.short_description

            if filename == None:
                filename = app_config.file_path + app_config.race_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_race_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        race_controller = GUI_Race_Controller.GUI_race_controller()

        if supress_gui:
            return race_controller
        else:
            race_controller.load_lookups(self.sizes,self.bodies,self.languages,self.foci,self.feats)
            race_controller.load_data(self.current_set.get_race(name),self.save_race,self.close_edit_race)

    def load_set(self,filename=None):
        self.current_set = Race.Races()

        if filename == None:
            filename = app_config.file_path + app_config.race_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for race in data_root:
            name = race.find('name').text or 'UNKNOWN'
            current_race = Race.Race(name)
            current_race.short_description = race.find('shortDescription').text or ' '
            current_race.description = race.find('description').text or ' ' 
            current_race.size = race.find('size').text or ' '
            current_race.body = race.find('body').text or ' '
            current_race.str_bonus = race.find('strBonus').text or 0
            current_race.per_bonus = race.find('perBonus').text or 0
            current_race.int_bonus = race.find('intBonus').text or 0
            current_race.dex_bonus = race.find('dexBonus').text or 0
            current_race.cha_bonus = race.find('chaBonus').text or 0
            current_race.vit_bonus = race.find('vitBonus').text or 0
            current_race.mag_bonus = race.find('magBonus').text or 0
            current_race.will_bonus = race.find('willBonus').text or 0
            current_race.fortitude_bonus = race.find('fortitudeBonus').text or 0
            current_race.reflex_bonus = race.find('reflexBonus').text or 0
            for language in race.findall('languagesBonus/language'):
                lang = List_Object.List_object(language.attrib.get('name'),language.text)
                current_race.languages_bonus.append(lang)
            for feat in race.findall('feats/feat'):
                current_race.feats.append(feat.text)
            for focus in race.findall('foci/focus'):
                current_race.foci.append(focus.text)
            self.current_set.add_new(current_race)

        self.loaded_set = self.current_set.clone()

    def load_combo_data(self):
        misc_lists = Manage_Misc_Lists.Manage_misc_lists()
        misc_lists.load_set()
        foci_list = Manage_Foci.Manage_foci()
        foci_list.load_set()
        self.sizes = misc_lists.get_current_set().get_item('Creature Sizes').item_names
        self.bodies = misc_lists.get_current_set().get_item('Creature Body Types').item_names
        self.languages = Misc_List.Misc_lists()
        self.languages.add_new(misc_lists.get_current_set().get_item('Languages').clone())
        self.foci = Misc_List.Misc_lists()
        self.foci.add_new(Misc_List.Misc_list('Foci','',foci_list.get_current_set().all_items))
        feat_types = misc_lists.get_current_set().get_item('Feat Types').item_names
        self.feats = Misc_List.Misc_lists()
        for feat_type in feat_types:
            self.feats.add_new(misc_lists.get_current_set().get_item(feat_type).clone())

    def __init__(self):
        self.name = 'Races'
        self.load_combo_data()
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_races()

    manager.load_races()
    manager.launch_race_list()
