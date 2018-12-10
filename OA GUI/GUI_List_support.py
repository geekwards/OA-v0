try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__),"../..") + '/OA Data Files')
import app_config

import List_Object

def cancel_click():
    destroy_window()

def new_click():
    global edit_call
    global list_window
    edit_call(list_window,None)

def init(window,form):
    global list_form
    global list_window

    list_form = form
    list_window = window

def destroy_window():
    global list_window
    list_window.destroy()
    list_window = None

def build_list(list_type,list_items,editcall,removecall):
    global list_form
    global list_window
    global edit_call
    global remove_call

    edit_call = editcall
    remove_call = removecall

    list_form.build_list(list_type)

    idx=0

    for list_item in list_items:
        list_form.add_list_item(idx,list_item.name,list_item.short_description,editcall,removecall)
        idx+=1
