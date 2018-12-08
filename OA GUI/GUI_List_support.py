#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 24, 2018 07:20:13 AM EST  platform: Windows NT
#    Nov 24, 2018 09:36:47 PM EST  platform: Windows NT

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import ListObject

def cancel_click():
    destroy_window()

def new_click():
    global edit_call
    global top_level
    edit_call(top_level, None)

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

def refresh_frame():
    global w
    global top_level

    w.f1.destroy()

    w.f1 = tk.Frame(top_level)
    w.f1.grid(sticky='nsew', row=2, column=0, padx=20, pady=20)

    w.f1.grid_columnconfigure(0, weight=1)
    w.f1.grid_columnconfigure(1, weight=3)
    w.f1.grid_columnconfigure(2, weight=1)

def build_list(list_type, list_items, editcall, removecall):
    # Function to fill in  List management GUI_List
    global w
    global top_level
    global edit_call
    global remove_call

    edit_call = editcall
    remove_call = removecall

    top_level.title("OA Manager - " + list_type)
    w.lbltitle.config(text=list_type)

    refresh_frame()

    idx=0

    for list_item in list_items:
        add_list_item(idx,list_item.name, list_item.short_description, editcall, removecall)
        idx+=1

def add_list_item(idx,name, short_description, editcall, removecall):
    global w
    global top_level

    w.f1.edit_list_item = tk.Button(w.f1, text ="Edit" + str(idx), command=lambda: editcall(top_level, idx))
    w.f1.edit_list_item.grid(sticky='nsew', row=idx+2, column=0, padx=5, pady=5)

    w.f1.lbl_list_item = tk.Label(w.f1, text=name + ' - ' + short_description)
    w.f1.lbl_list_item.grid(sticky='w', row=idx+2, column=1, padx=5, pady=5)

    w.f1.edit_list_item = tk.Button(w.f1, text ="Remove" + str(idx), command=lambda: removecall(idx))
    w.f1.edit_list_item.grid(sticky='nsew', row=idx+2, column=2, padx=5, pady=5)

if __name__ == '__main__':
    import GUI_List
    GUI_List.vp_start_gui()
