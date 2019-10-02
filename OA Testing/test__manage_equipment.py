import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Equipment
import test__gui_equipment_controller
import test__gui_list_controller
import test__manage_money
import test__manage_food
import test__manage_clothing
import test__manage_miscequip
import test__manage_containers
import test__manage_armor
import test__manage_weapons

class Manage_data(Manage_Equipment.Manage_equipment):
    def set_controller(self,parent=None):
        self.edit_controller = test__gui_equipment_controller.GUI_controller(parent)
        self.list_controller = test__gui_list_controller.GUI_controller(parent)
    
    def get_edit_controller(self):
        return self.edit_controller

    def get_list_controller(self):
        return self.list_controller

    def launch_edit(self,name,parent=None):
        if name == 'Money':
            equip_manage = test__manage_money.Manage_data()
        elif name == 'Food':
            equip_manage = test__manage_food.Manage_data()
        elif name == 'Clothing':
            equip_manage = test__manage_clothing.Manage_data()
        elif name == 'Misc Equipment':
            equip_manage = test__manage_miscequip.Manage_data()
        elif name == 'Container':
            equip_manage = test__manage_containers.Manage_data()
        elif name == 'Armor':
            equip_manage = test__manage_armor.Manage_data()
        elif name == 'Weapon':
            equip_manage = test__manage_weapons.Manage_data()
        equip_manage.load_set() 
        equip_manage.launch_list(name,parent)