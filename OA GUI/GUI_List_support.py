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

def build_list(list_type, list_items, editcall):
    # Function to fill in  List management GUI_List
    global w
    global top_level

    top_level.title("OA Manager - " + list_type)
    w.lbltitle.config(text=list_type)

    idx=0

    for list_item in list_items:
        add_list_item(idx,list_item.name, list_item.short_description, editcall)
        idx+=1

def add_list_item(idx,name, short_description, editcall):
    global w
    global top_level

    x = 10
    y = (idx*30)+80

    w.edit_list_item = tk.Button(top_level, text ="Edit" + str(idx), command=lambda: editcall(top_level, idx))
    w.edit_list_item.place(x=x, y=y, height=25, width=50)

    w.lbl_list_item = tk.Label(top_level, text=name + ' - ' + short_description)
    w.lbl_list_item.place(x=x+60, y=y, height=30, width=400)

if __name__ == '__main__':
    import GUI_List
    GUI_List.vp_start_gui()
