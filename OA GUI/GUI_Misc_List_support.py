import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import List_Object

def init(window,form):
    global list_form
    global list_window

    list_form = form
    list_window = window

def destroy_window():
    global list_window

    list_window.destroy()
    list_window = None

def close_click():
    destroy_window()

def edit_click():
    global current_list
    global rollback_list

    rollback_list = current_list.clone()

def remove_click(idx):
    global remove_callback

    remove_callback(current_list.name,idx)
    current_list.remove(current_list.get_list()[idx])
    build_list(current_list)

def cancel_click():
    global rollback_list
    global list_form

    if rollback_list.name > '':
        build_list(rollback_list)

def save_click():
    global rollback_list
    global save_callback
    global current_list
    global index

    if index == 0:
        current_list.name = list_form.etitle.get('')

    for item in list_form.f1.winfo_children():
        current_list.add_new(item)

    save_callback(index,current_list)
    list_form.disable_form()

def load_data(set,savecall,removecall,idx):
    global list_form
    global save_callback
    global remove_callback
    global original_list
    global current_list
    global index

    index = idx
    original_list = set.clone()
    current_list = set.clone()

    save_callback = savecall
    remove_callback = removecall

    build_list(current_list)

def build_list(set):
    global list_form
    global list_window

    idx=0

    list_form.set_form_title(set.name)

    list_form.enable_form()

    for list_item in set.get_list():
        list_form.add_list_item(idx,list_item)
        idx+=1

    list_form.disable_form()

if __name__ == '__main__':
    import GUI_Misc_List.py
    GUI_Misc_List.vp_start_gui()
