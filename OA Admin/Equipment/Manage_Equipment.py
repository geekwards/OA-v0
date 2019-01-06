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
    def launch_equipment(self,parent,name,supress_gui=False):
        global sup_gui

        if name == 'Money':
            equip_manage = Manage_Money.Manage_money()
            equip_manage.load_money()
            equip_manage.launch_money_list()
        elif name == 'Food':
            equip_manage = Manage_Food.Manage_food()
            equip_manage.load_food()
            equip_manage.launch_food_list()

    def launch_equipment_list(self,supress_gui=False):
        global current_set
        global list_controller

        if list_controller == None:
            list_controller = GUI_List_Controller.GUI_list_controller()
        
        list_controller.set_edit(False)

        if supress_gui:
            return list_controller
        else:
            list_controller.load_data('Equipment',current_set.all_items,self.launch_equipment,None,None)

    def load_equipment(self,filename=None):
        global current_set

        data_load = Manage_Misc_Lists.Manage_misc_lists()
        data_load.load_misc_lists()
        current_set = data_load.get_current_set().get_misc_list('Equipment Types')

    def __init__(self):
        global current_set
        global list_controller

        list_controller = None
        current_set = None

if __name__ == '__main__':
    manager = Manage_equipment()

    manager.load_equipment()
    manager.launch_equipment_list()
