import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List_Controller
import Container
import List_Object
import GUI_Equipment_Controller

class Manage_containers:
    current_set
    loaded_set
    sup_gui
    list_controller

    def save_container(self,container,fullsave=False):
        self.current_set.update(container)
        if fullsave:
            self.save_containers()

    def save_containers(self,filename=None,backup_filename=None):
        if not self.current_set.equals(self.loaded_set):
            data=ET.Element('containers')
            for mcontainer in self.current_set.all_clothes:
                l=ET.SubElement(data,'container')
                ET.SubElement(l,'name').text = mcontainer.name
                ET.SubElement(l,'shortDescription').text = mcontainer.short_description
                ET.SubElement(l,'description').text = mcontainer.description
                ET.SubElement(l,'cost').text = mcontainer.cost
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

    def remove_container(self,container):
        self.current_set.remove(container)

    def close_edit_container(self):
        self.launch_container_list(self.sup_gui)

    def launch_edit_container(self,parent,name,supress_gui=False):
        self.sup_gui = supress_gui
        container_controller = GUI_Equipment_Controller.GUI_equipment_controller()            

        if len(name) > 0:
            container = self.current_set.get_container(name)
        else:
            container = Container.Container('','')

        if supress_gui:
            return container_controller
        else:
            container_controller.load_data('Container',container,self.save_container,self.close_edit_container)
    
    def launch_container_list(self,supress_gui=False):
        if self.list_controller == None:
            self.list_controller = GUI_List_Controller.GUI_list_controller()
        
        if supress_gui:
            return self.list_controller
        else:
            self.list_controller.load_data('Containers',self.current_set.list_of_containers,self.launch_edit_container,self.remove_container,self.save_containers)

    def load_containers(self,filename=None):
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
            new_container.cost = container.find('cost').text or 0
            new_container.weight = container.find('weight').text or 0
            new_container.health = container.find('health').text or 0
            new_container.capacity = container.find('capacity').text or 0
            new_container.special = container.find('special').text or 'none'
            self.current_set.add_new(new_container)

        self.loaded_set = self.current_set.clone()

    def get_current_set(self):
        return self.current_set

    def __init__(self):
        self.list_controller = None
        self.current_set = None
        self.loaded_set = None

if __name__ == '__main__':
    manager = Manage_containers()

    manager.load_containers()
    manager.launch_container_list()
