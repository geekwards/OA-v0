import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Clothing
import List_Object
import GUI_Equipment_Controller

class Manage_clothing(Base_Manage_Data.Manage_data):
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set.equals(self.loaded_set):
            data=ET.Element('clothing')
            for mclothing in self.current_set.all_clothes:
                l=ET.SubElement(data,'clothingType')
                ET.SubElement(l,'name').text = mclothing.name
                ET.SubElement(l,'shortDescription').text = mclothing.short_description
                ET.SubElement(l,'description').text = mclothing.description
                ET.SubElement(l,'cost').text = mclothing.cost
                ET.SubElement(l,'weight').text = mclothing.weight
                ET.SubElement(l,'health').text = mclothing.health
                ET.SubElement(l,'capacity').text = mclothing.capacity
                ET.SubElement(l,'special').text = mclothing.special
 
            if filename == None:
                filename = app_config.file_path + app_config.clothing_filename

            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_clothing_filename

            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def launch_edit(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        clothing_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            garment = self.current_set.get_garment(name)
        else:
            garment = Clothing.Garment('','')

        if supress_gui:
            return clothing_controller
        else:
            clothing_controller.load_data('Clothing',garment,self.save_garment,self.close_edit_garment)

    def load_set(self,filename=None):
        self.current_set = Clothing.Clothing()   

        if filename == None:
            filename = app_config.file_path + app_config.clothing_filename

        tree = ET.parse(filename)
        data_root = tree.getroot()

        for garment in data_root:
            new_garment_name = garment.find('name').text or 'UNKNOWN'
            new_garment_short_description = garment.find('shortDescription').text or 'UNKNOWN'
            new_garment = Clothing.Garment(new_garment_name,new_garment_short_description)
            new_garment.description = garment.find('description').text or 'UNKNOWN'
            new_garment.cost = garment.find('cost').text or 0
            new_garment.weight = garment.find('weight').text or 0
            new_garment.health = garment.find('health').text or 0
            new_garment.capacity = garment.find('capacity').text or 0
            new_garment.special = garment.find('special').text or 'none'
            self.current_set.add_new(new_garment)

        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Clothing'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_clothing()

    manager.load_clothing()
    manager.launch_clothing_list()
