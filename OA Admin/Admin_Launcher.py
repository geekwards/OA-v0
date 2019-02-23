import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import List_Object
import GUI_List_Controller
import Base_Manage_Data
import Manage_Archtypes
import Manage_Foci
import Manage_Misc_Lists
import Manage_Equipment
import Manage_Races
import Manage_Armor
import Manage_Clothing
import Manage_Containers
import Manage_Food
import Manage_MiscEquip
import Manage_Money
import Manage_Weapons

class Manage_all:
    def launch_edit(self,name,parent=None):
        manager = Base_Manage_Data.Manage_data()
        if name == 'Archtypes':
            manager = Manage_Archtypes.Manage_archtypes()
        elif name == 'Equipment':
            manager = Manage_Equipment.Manage_equipment()
        elif name == 'Races':
            manager = Manage_Races.Manage_races()
        elif name == 'Foci':
            manager = Manage_Foci.Manage_foci()
        elif name == 'Misc Lists':
            manager = Manage_Misc_Lists.Manage_misc_lists()
        manager.load_set() 
        manager.launch_list(name,parent)

    def launch_list(self,parent=None):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        self.list_controller.load_data('Manage Data',self.select_list,self.launch_edit,None,None,False)

    def load_set(self,filename=None):
        self.current_set = app_config.admin_Types
        self.select_list = []
        for sel_set in self.current_set:
            self.select_list.append(List_Object.List_object(sel_set[0],''))

    def get_current_set(self):
        return self.current_set.all_items

    def __init__(self,parent=None):
        self.parent = parent
        self.list_controller = None
        self.current_set = None

if __name__ == '__main__':
    manager = Manage_all()

    manager.load_set()
    manager.launch_list()
