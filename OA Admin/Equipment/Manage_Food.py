import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Food
import List_Object
import GUI_Equipment_Controller

class Manage_food(Base_Manage_Data.Manage_data):
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set.equals(self.loaded_set):
            data=ET.Element('food')
            for mfood in self.current_set.all_food:
                l=ET.SubElement(data,'foodType')
                ET.SubElement(l,'name').text = mfood.name
                ET.SubElement(l,'shortDescription').text = mfood.name
                ET.SubElement(l,'description').text = mfood.name
                ET.SubElement(l,'cost').text = mfood.name
                ET.SubElement(l,'weight').text = mfood.name
 
            if filename == None:
                filename = app_config.file_path + app_config.food_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_food_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        food_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            food = self.current_set.get_food(name)
        else:
            food = Food.Food('','')

        if supress_gui:
            return food_controller
        else:
            food_controller.load_data('Food',food,self.save_food,self.close_edit_food)
    
    def load_set(self,filename=None):
        self.current_set = Food.Foods()   

        if filename == None:
            filename = app_config.file_path + app_config.food_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for food in data_root:
            new_food_name = food.find('name').text or 'UNKNOWN'
            new_food_short_description = food.find('shortDescription').text or 'UNKNOWN'
            new_food = Food.Food(new_food_name,new_food_short_description)
            new_food.description = food.find('description').text or 'UNKNOWN'
            new_food.cost = food.find('cost').text or 0
            new_food.weight = food.find('weight').text or 0
            self.current_set.add_new(new_food)

        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Food'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_food()

    manager.load_food()
    manager.launch_food_list()
