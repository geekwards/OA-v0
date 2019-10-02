import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data
import Container
import List_Object
import GUI_Equipment_Controller

class Manage_containers(Base_Manage_Data.Manage_data):
    def save_one(self,item,filename=None,backup_filename=None):
        if type(item) == Container.Container and not(item.isempty()):
            super().save_one(item,filename,backup_filename)
        else:
            raise ValueError('expected Container object, instead got ' + str(type(item)))

    def remove_item(self,item):
        if type(item) == Container.Container and not(item.isempty()):
            super().remove_item(item)
        else:
            raise ValueError('expected Container object, instead got ' + str(type(item)))
            
    def save_all(self,filename=None,backup_filename=None):
        if not self.current_set == self.loaded_set:
            data=ET.Element('containers')
            for mcontainer in self.current_set.all_items:
                l=ET.SubElement(data,'container')
                ET.SubElement(l,'name').text = mcontainer.name
                ET.SubElement(l,'shortDescription').text = mcontainer.short_description
                ET.SubElement(l,'description').text = mcontainer.description
                ET.SubElement(l,'value').text = mcontainer.value
                ET.SubElement(l,'weight').text = mcontainer.weight
                ET.SubElement(l,'health').text = mcontainer.health
                ET.SubElement(l,'capacity').text = mcontainer.capacity
                ET.SubElement(l,'special').text = mcontainer.special
            if filename == None:
                filename = app_config.file_path + app_config.container_filename
            if backup_filename == None:
                backup_filename = app_config.backup_file_path + app_config.backup_container_filename
            copy2(filename,backup_filename)
            f = open(filename,'w')
            f.write(ET.tostring(data, encoding="unicode"))
            f.close()

    def set_controller(self,parent=None):
        self.edit_controller = GUI_Equipment_Controller.GUI_equipment_controller(parent)

    def launch_edit(self,name,parent=None):
        self.edit_controller.create_form(parent)
        if len(name) > 0:
            container = self.current_set.get_item(name)
        else:
            container = Container.Container('','')
        self.edit_controller.load_data('Container',container,self.save_one,self.close_edit_item)

    def load_set(self,filename=None):
        self.current_set = Container.Containers()   
        if filename == None:
            filename = app_config.file_path + app_config.container_filename
        tree = ET.parse(filename)
        data_root = tree.getroot()
        for container in data_root:
            new_container_name = container.find('name').text or 'UNKNOWN'
            new_container_short_description = container.find('shortDescription').text or 'UNKNOWN'
            new_container = Container.Container(new_container_name,new_container_short_description)
            new_container.description = container.find('description').text or 'UNKNOWN'
            new_container.value = container.find('value').text or 0
            new_container.weight = container.find('weight').text or 0
            new_container.health = container.find('health').text or 0
            new_container.capacity = container.find('capacity').text or 0
            new_container.special = container.find('special').text or 'none'
            self.current_set.add_new(new_container)
        self.loaded_set = self.current_set.clone()

    def __init__(self):
        self.name = 'Containers'
        Base_Manage_Data.Manage_data.__init__(self)

if __name__ == '__main__':
    manager = Manage_containers()
    manager.load_containers()
    manager.launch_container_list()
