import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Manage_Misc_Lists
import Manage_Armor
import Manage_Clothing
import Manage_Containers
import Manage_Food
import Manage_MiscEquip
import Manage_Money
import Manage_Weapons


class Manage_equipment:
    sup_gui
    current_set
    list_controller

    def launch_equipment(self,parent,name,supress_gui=False):
        if name == 'Money':
            equip_manage = Manage_Money.Manage_money()
            equip_manage.load_money()
            equip_manage.launch_money_list()
        elif name == 'Food':
            equip_manage = Manage_Food.Manage_food()
            equip_manage.load_food()
            equip_manage.launch_food_list()
        elif name == 'Clothing':
            equip_manage = Manage_Clothing.Manage_clothing()
            equip_manage.load_clothing()
            equip_manage.launch_clothing_list()
        elif name == 'Misc Equipment':
            equip_manage = Manage_MiscEquip.Manage_misc_equipment()
            equip_manage.load_misc_equipment()
            equip_manage.launch_misc_equipment_list()
        elif name == 'Container':
            container_manage = Manage_Containers.Manage_containers()
            container_manage.load_containers()
            container_manage.launch_container_list()
        elif name == 'Armor':
            armor_manage = Manage_Armor.Manage_armor()
            armor_manage.load_armors()
            armor_manage.launch_armor_list()
        elif name == 'Weapon':
            weapon_manage = Manage_Weapons.Manage_weapons()
            weapon_manage.load_weapons()
            weapon_manage.launch_weapon_list()

    def launch_equipment_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        
        self.list_controller.set_edit(False)

        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Equipment',self.current_set.all_items,self.launch_equipment,None,None)

    def load_equipment(self,filename=None):
        data_load = Manage_Misc_Lists.Manage_misc_lists()
        data_load.load_misc_lists()
        self.current_set = data_load.get_current_set().get_misc_list('Equipment Types')

    def __init__(self):
        list_controller = None
        current_set = None

if __name__ == '__main__':
    manager = Manage_equipment()

    manager.load_equipment()
    manager.launch_equipment_list()
