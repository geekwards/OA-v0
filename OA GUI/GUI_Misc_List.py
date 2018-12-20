import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import GUI_Misc_List_support

def create_misc_list_form(parent):
    global list_window
    global list_form

    if parent == None:
        list_window = tk.Tk()
    else:
        list_window = tk.Toplevel(parent)
    list_form = MiscListForm(list_window)
    GUI_Misc_List_support.init(list_window,list_form)
    return (list_window,list_form)

def destroy_list_form():
    global list_window

    list_window.destroy()
    list_window = None

def close_click():
    GUI_Misc_List_support.close_click()

def edit_click():
    global list_form

    list_form.set_for_edit()
    GUI_Misc_List_support.edit_click()

def cancel_click():
    global list_form

    list_form.set_for_view()
    GUI_Misc_List_support.cancel_click()

def remove_click(idx):
    GUI_Misc_List_support.remove_click(idx)

def save_click():
    global list_form

    list_form.set_for_view()
    GUI_Misc_List_support.save_click()

def new_click():
    global list_form

    list_form.add_list_item(list_form.list_count,'')

def load_data(set,savecall,removecall,idx):
    GUI_Misc_List_support.load_data(set,savecall,removecall,idx)

class MiscListForm:

    def set_for_edit(self):
        self.left_button.config(text='Cancel')
        self.left_button.config(command=cancel_click)
        self.center_button = tk.Button(self.parent,text='New',command=new_click)
        self.center_button.config(width=10,height=2)
        self.center_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button.config(text='Save')
        self.right_button.config(command=save_click)
        self.enable_form()

    def set_for_view(self):
        self.left_button.config(text='Close')
        self.left_button.config(command=close_click)
        self.center_button.destroy()
        self.right_button.config(text='Edit')
        self.right_button.config(command=edit_click)
        self.disable_form()

    def enable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='disabled')

    def set_form_title(self,title):
        if len(title) == 0:
            self.parent.title('AddNew')
            self.etitle = tk.Entry(self.parent)
            self.etitle.config(font=app_config.title_font)
            self.etitle.grid(sticky='nsew',row=0,column=0,rowspan=2,pady=20)
            self.set_for_edit()
        else:
            self.parent.title(title)
            self.lbltitle = tk.Label(self.parent,text=title)
            self.lbltitle.config(font=app_config.title_font)
            self.lbltitle.grid(sticky='nsew',row=0,column=0,rowspan=2,pady=20)

    def add_list_item(self,idx,item):
        self.f1.eitem = tk.Entry(self.f1)
        self.f1.eitem.insert(0,item)
        self.f1.eitem.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        self.f1.edit_list_item = tk.Button(self.f1,text ="Remove",command=lambda: remove_click(idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=2,padx=5,pady=5)
        self.list_count += 1

    def __init__(self,parent):
        self.parent = parent
        self.set_form_title('LIST NOT LOADED')
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,padx=20,pady=20)
        self.left_button = tk.Button(self.parent,text='Close',command=close_click)
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=1,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit',command=edit_click)
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=3,pady=10)
        self.list_count = 0
