import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Food
import List_Object
import GUI_Equipment_Controller

class Manage_food:
    def save_food(self,food,fullsave=False):
        global current_set

        current_set.update(food)
        if fullsave:
            self.save_foods()

    def save_foods(self,filename=None,backup_filename=None):
        global current_set

        if not current_set.equals(loaded_set):
            data=ET.Element('food')
            for mlist in current_set.all_lists:
                l=ET.SubElement(data,'foodType')
                ET.SubElement(l,'name').text = mlist.name
                ET.SubElement(l,'shortDescription').text = mlist.name
                ET.SubElement(l,'description').text = mlist.name
                ET.SubElement(l,'cost').text = mlist.name
                ET.SubElement(l,'weight').text = mlist.name
 
            if filename == None:
                filename = app_config.file_path + app_config.food_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_food_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def remove_food(self,food):
        global current_set

        current_set.remove(food)

    def close_edit_food(self):
        global sup_gui

        self.launch_food_list(sup_gui)

    def launch_edit_food(self,parent,name,supress_gui=False):
        global current_set
        global sup_gui

        sup_gui = supress_gui
        food_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            food = current_set.get_food(name)
        else:
            food = Food.Food('','')

        if supress_gui:
            return food_controller
        else:
            food_controller.load_data('Food',food,self.save_food,self.close_edit_food)
    
    def launch_food_list(self,supress_gui=False):
        global current_set
        global list_controller

        if list_controller == None:
            list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return list_controller
        else:
            list_controller.load_data('food Types',current_set.list_of_food,self.launch_edit_food,self.remove_food,self.save_foods)

    def load_food(self,filename=None):
        global current_set
        global loaded_set

        current_set = Food.Foods()   

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
            current_set.add_new(new_food)

        loaded_set = current_set.clone()

    def get_current_set(self):
        global current_set

        return current_set

    def __init__(self):
        global current_set
        global list_controller

        list_controller = None
        current_set = None

if __name__ == '__main__':
    manager = Manage_food()

    manager.load_food()
    manager.launch_food_list()
