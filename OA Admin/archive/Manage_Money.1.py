import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Money
import List_Object
import GUI_Equipment_Controller

class Manage_money:
    current_set
    loaded_set
    list_controller
    sup_gui

    def save_money(self,money,fullsave=False):
        global self.current_set

        self.current_set.update(money)
        if fullsave:
            self.save_monies()

    def save_monies(self,filename=None,backup_filename=None):
        if not self.current_set.equals(self.loaded_set):
            data=ET.Element('money')
            for mmoney in self.current_set.all_lists:
                l=ET.SubElement(data,'moneyType')
                ET.SubElement(l,'name').text = mmoney.name
                ET.SubElement(l,'shortDescription').text = mmoney.name
                ET.SubElement(l,'description').text = mmoney.name
                ET.SubElement(l,'cost').text = mmoney.name
                ET.SubElement(l,'weight').text = mmoney.name
 
            if filename == None:
                filename = app_config.file_path + app_config.money_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_money_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_money(self,money):
        self.current_set.remove(money)

    def close_edit_money(self):
        self.launch_money_list(self.sup_gui)

    def launch_edit_money(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        money_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            money = self.current_set.get_money(name)
        else:
            money = Money.Money('','')

        if supress_gui:
            return money_controller
        else:
            money_controller.load_data('Money',money,self.save_money,self.close_edit_money)
    
    def launch_money_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Money Types',self.current_set.list_of_money,self.launch_edit_money,self.remove_money,self.save_monies)

    def load_money(self,filename=None):
        self.current_set = Money.Monies()   

        if filename == None:
            filename = app_config.file_path + app_config.money_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for money in data_root:
            new_money_name = money.find('name').text or 'UNKNOWN'
            new_money_short_description = money.find('shortDescription').text or 'UNKNOWN'
            new_money = Money.Money(new_money_name,new_money_short_description)
            new_money.description = money.find('description').text or 'UNKNOWN'
            new_money.cost = money.find('cost').text or 0
            new_money.weight = money.find('weight').text or 0
            self.current_set.add_new(new_money)

        self.loaded_set = self.current_set.clone()

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None

if __name__ == '__main__':
    manager = Manage_money()

    manager.load_money()
    manager.launch_money_list()
