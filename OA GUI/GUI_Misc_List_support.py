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

    rollback_list = current_list.copy()

def cancel_click():
    global rollback_list
    global list_form

    if len(rollback_list) > 0:
        list_form.load_form(rollback_list)

def save_click():
    global rollback_list
    global save_callback
    global current_list
    global index

    for item in list_form.f1.winfo_children():
        current_list.append(item)

    save_callback(index,current_list)
    list_form.disable_form()

def load_data(set,savecall,idx):
    global list_form
    global save_callback
    global original_list
    global current_list
    global index

    index = idx
    original_list = set.copy()
    current_list = set.copy()

    save_callback = savecall

    list_form.load_form(set)

if __name__ == '__main__':
    import list.py
    GUI_Archtype.py.vp_start_gui()
