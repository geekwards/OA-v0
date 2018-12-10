import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import GUI_List_support

def create_list_form(parent):
    global list_window
    global list_form

    if parent == None:
        list_window = tk.Tk()
    else:
        list_window = tk.Toplevel(parent)
    list_form = ListForm(list_window)
    GUI_List_support.init(list_window,list_form)
    return (list_window,list_form)

def build_list(list_type,list_items,editcall,removecall):
    GUI_List_support.build_list(list_type, list_items, editcall, removecall)

def destroy_list_form():
    global list_window
    list_window.destroy()
    list_window = None

def new_click():
    GUI_List_support.new_click()

def cancel_click():
    GUI_List_support.cancel_click()

class ListForm:

    def build_list(self,list_type):
        self.parent.title("OA Manager - " + list_type)
        self.lbltitle.config(text=list_type)
        self.refresh_frame()

    def add_list_item(self,idx,name,short_description,editcall,removecall):
        self.f1.edit_list_item = tk.Button(self.f1,text ="Edit" + str(idx),command=lambda: editcall(self.parent, idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=0,padx=5,pady=5)
        self.f1.lbl_list_item = tk.Label(self.f1,text=name + ' - ' + short_description)
        self.f1.lbl_list_item.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        self.f1.edit_list_item = tk.Button(self.f1,text ="Remove" + str(idx),command=lambda: removecall(idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=2,padx=5,pady=5)

    def refresh_frame(self):
        self.f1.destroy()
        self.f1 = tk.Frame()
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=1)

    def __init__(self, parent):
        self.parent = parent
        self.parent.title("LIST NOT LOADED")
        self.f1 = tk.Frame()
        self.refresh_frame()
        self.lbltitle = tk.Label(self.parent,text='LIST NOT LOADED')
        self.lbltitle.configure(font=app_config.title_font)
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=3,rowspan=2,pady=20)
        self.left_button = tk.Button(self.parent,text='Cancel',command=cancel_click)
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='sw',row=3,column=0,padx=20,pady=20)
        self.right_button = tk.Button(self.parent,text='NEW',command=new_click)
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='sw',row=3,column=2,padx=20,pady=20)
