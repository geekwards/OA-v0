import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import GUI_Equipment_Controller
import Base_Manage_Data
import Manage_Misc_Lists
import Manage_Armor
import Manage_Clothing
import Manage_Containers
import Manage_Food
import Manage_MiscEquip
import Manage_Money
import Manage_Weapons

class Manage_equipment:
    def launch_edit(self,parent,name,supress_gui=False):
        equip_manage = Base_Manage_Data.Manage_data()
        if name == 'Money':
            equip_manage = Manage_Money.Manage_money()
        elif name == 'Food':
            equip_manage = Manage_Food.Manage_food()
        elif name == 'Clothing':
            equip_manage = Manage_Clothing.Manage_clothing()
        elif name == 'Misc Equipment':
            equip_manage = Manage_MiscEquip.Manage_misc_equipment()
        elif name == 'Container':
            equip_manage = Manage_Containers.Manage_containers()
        elif name == 'Armor':
            equip_manage = Manage_Armor.Manage_armor()
        elif name == 'Weapon':
            equip_manage = Manage_Weapons.Manage_weapons()
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()            
        equip_manage.load_set() 
        equip_data = equip_manage.get_current_set()
        if supress_gui:
            return equip_controller
        else:
            equip_controller.load_data(name,equip_data,self.save_container,self.close_edit_container)


    def launch_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        self.list_controller.load_data('Equipment',self.current_set.all_items,self.launch_edit,None,None,False)
        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.launch_form()

    def load_set(self,filename=None):
        data_load = Manage_Misc_Lists.Manage_misc_lists()
        data_load.load_set(filename)
        self.current_set = data_load.get_current_set().get_item('Equipment Types')

    def get_current_set(self):
        return self.current_set.all_items

    def __init__(self):
        self.list_controller = None
        self.current_set = None

if __name__ == '__main__':
    manager = Manage_equipment()

    manager.load_set()
    manager.launch_list()
