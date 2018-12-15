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

def cancel_click():
    global rollback_list
    global list_form

    if not(rollback_list.isempty()):
        list_form.load_form(rollback_list)

def save_click():
    global rollback_list
    global save_callback
    global current_list
    global index

    current_list.name = list_form.f1.ename.get()
    current_list.description = list_form.f1.txtdescription.get("1.0",'end-1c')
    current_list.size = list_form.f1.esize.get()
    current_list.body_type = list_form.f1.ebody_type.get()
    current_list.str_bonus = list_form.f1.estr.get()
    current_list.per_bonus = list_form.f1.eper.get()
    current_list.int_bonus = list_form.f1.eint.get()
    current_list.dex_bonus = list_form.f1.edex.get()
    current_list.cha_bonus = list_form.f1.echa.get()
    current_list.vit_bonus = list_form.f1.evit.get()
    current_list.mag_bonus = list_form.f1.emag.get()
    current_list.will_bonus = list_form.f1.ewill.get()
    current_list.fort_bonus = list_form.f1.efort.get()
    current_list.reflex_bonus = list_form.f1.ereflex.get()

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
