import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import List_Object
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
    def launch_edit(self,name,parent=None):
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
        equip_manage.set_controller()
        equip_manage.load_set()
        equip_manage.launch_list(name,parent)

    def set_controller(self,parent=None):
        self.list_controller = GUI_List_Controller.GUI_list_controller(parent)

    def launch_list(self,name,parent=None):
        self.list_controller.create_form()
        self.list_controller.load_data(name,self.select_list,self.launch_edit,None,None,False)

    def load_set(self):
        self.current_set = app_config.equipment_Types
        self.select_list = []
        for sel_set in self.current_set:
            self.select_list.append(List_Object.List_object(sel_set[0],sel_set[1]))

    def get_current_set(self):
        return self.current_set

    def __init__(self,parent=None):
        self.parent = parent
        self.name = 'Equipment'
        super().__init__()
        self.set_controller(parent)

if __name__ == '__main__':
    manager = Manage_equipment()
    manager.load_set()
    manager.launch_list('Equipment')
