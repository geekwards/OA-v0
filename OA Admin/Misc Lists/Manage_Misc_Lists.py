import xml.etree.ElementTree as ET
from shutil import copy2

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import GUI_List
import GUI_Misc_List
import List_Object
import Misc_List

list_window = None
current_list_idx = 0

def save_misc_list(idx,misc_list):
    global current_set
    global list_window

    current_set.update(idx,misc_list)

    if list_window != None:
        GUI_List.build_list("Misc Lists",current_set.get_picklist(),launch_edit_misc_list, remove_misc_list)

def save_misc_lists(filename=None,backup_filename=None):
    global current_set

    data=ET.Element('misc_lists')
    for item in current_set:
        r=ET.SubElement(data,'misc_list')
        ET.SubElement(r,'name').text = item.name

    if filename == None:
        filename = app_config.file_path + app_config.filename

    if backup_filename == None:
        backup_filename = app_config.backup_file_path + app_config.backup_filename

    copy2(filename,backup_filename)
    f = open(filename,'w')
    f.write(ET.tostring(data, encoding="unicode"))
    f.close()

def remove_misc_list(list_item_idx):
    global current_set
    global current_list_idx

    current_set[current_list_idx].remove(current_set[current_list_idx].get_list()[list_item_idx])

def launch_edit_misc_list(parent,list_idx,supress_gui=False):
    global current_set
    global misc_list_window
    global current_list_idx

    current_list_idx = list_idx

    misc_list_window = None

    #if misc_list_window == None or not Toplevel.winfo_exists(misc_list_window):
    misc_list_window,misc_list_form = GUI_Misc_List.create_misc_list_form(parent)

    if supress_gui:
        return misc_list_window
    else:
        GUI_Misc_List.load_data(current_set[list_idx],save_misc_list,remove_misc_list,list_idx)
        misc_list_window.mainloop()

def launch_misc_list_list(supress_gui=False):
    global current_set
    global loaded_set
    global list_window

    if list_window == None or not Toplevel.winfo_exists(list_window):
        list_window,list_form = GUI_List.create_list_form(None)

    if supress_gui:
        return list_window
    else:
        GUI_List.build_list("Misc Lists",current_set.get_picklist(),launch_edit_misc_list,remove_misc_list)
        list_window.mainloop()
        if not current_set.equals(loaded_set):
            save_misc_lists()

def load_misc_lists(filename=None):
    global current_set
    global loaded_set

    current_set = Misc_List.Misclists()   

    if filename == None:
        filename = app_config.file_path + app_config.misc_list_filename

    tree = ET.parse(filename)
    data_root = tree.getroot()

    for misc_list in data_root:
        new_list_name = misc_list.find('name').text

        new_list_items = []

        for misc_list_item in misc_list.findall('items/item'):
            new_list_items.append(misc_list_item.text)

        new_list = Misc_List.Misclist(new_list_name,new_list_items)
        current_set.add_new(new_list)

    loaded_set = current_set.clone()

def get_loaded_set():
    global loaded_set

    return loaded_set

if __name__ == '__main__':

    load_misc_lists()
    launch_misc_list_list()
