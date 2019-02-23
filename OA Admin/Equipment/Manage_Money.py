import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Money
import List_Object
import GUI_Equipment_Controller

class Manage_money(Base_Manage_Data.Manage_data):
    def save_one(self,item,filename=None,backup_filename=None):
        if type(item) == Money.Money and not(item.isempty()):
            super().save_one(item,filename,backup_filename)
        else:
            raise ValueError('expected Money object, instead got ' + str(type(item)))

    def remove_item(self,item):
        if type(item) == Money.Money and not(item.isempty()):
            super().remove_item(item)
        else:
            raise ValueError('expected Money object, instead got ' + str(type(item)))
            
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('money')
            for mmoney in self.current_set.all_items:
                l=ET.SubElement(data,'moneyType')
                ET.SubElement(l,'name').text = mmoney.name
                ET.SubElement(l,'shortDescription').text = mmoney.short_description
                ET.SubElement(l,'description').text = mmoney.description
                ET.SubElement(l,'value').text = mmoney.value
                ET.SubElement(l,'weight').text = mmoney.weight
                ET.SubElement(l,'health').text = mmoney.health
                ET.SubElement(l,'capacity').text = mmoney.capacity
                ET.SubElement(l,'special').text = mmoney.special
            if filename == None:
                filename = app_config.file_path + app_config.money_filename
            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_money_filename
            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,name,parent=None):
        money_controller = GUI_Equipment_Controller.GUI_equipment_controller()            
        if len(name) > 0:
            money = self.current_set.get_item(name)
        else:
            money = Money.Money('','')
        money_controller.load_data('Money',money,self.save_one,self.close_edit_item)
    
    def load_set(self,filename=None):
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
            new_money.value = money.find('value').text or 0
            new_money.weight = money.find('weight').text or 0
            new_money.health = money.find('health').text or 0
            new_money.capacity = money.find('capacity').text or 0
            new_money.special = money.find('special').text or 'UNK'
            self.current_set.add_new(new_money)
        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Money'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_money()
    manager.load_money()
    manager.launch_money_list()
