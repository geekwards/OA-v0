#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 24, 2018 07:20:13 AM EST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def set_Tk_var():
    global che47
    che47 = tk.StringVar()

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

def buildList(listType):
    # Function to fill in  List management GUI_List
    global w
    top_level.title("OA Manager - " + listType)
    w.lblTitle.config(text=listType)
    w.chkListItem.config(text = "TEST ITEM")

if __name__ == '__main__':
    import GUI_List.py
    GUI_List.py.vp_start_gui()
