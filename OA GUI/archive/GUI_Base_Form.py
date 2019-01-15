try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import tkinter.ttk as ttk

class Base_form:
    def set_edit(self):
        self.left_button.config(text='Cancel')
        self.left_button.config(command=self.cancel_click)
        self.right_button.config(text='Save')
        self.right_button.config(command=self.save_click)
        self.enable_form()

    def set_view(self):
        self.left_button.config(text='Close')
        self.left_button.config(command=self.close_click)
        self.right_button.config(text='Edit')
        self.right_button.config(command=self.edit_click)
        self.disable_form()

    def enable_form(self):
        for item in self.f1.winfo_children():
            if item.winfo_class() != 'Frame':
                item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            if item.winfo_class() != 'Frame':
                item.config(state='disabled')

    def clear_form(self):
        raise NotImplementedError

    def setup_form(self):
        raise NotImplementedError

    def add_item(self,race,close_call,cancel_call,edit_call,save_call,list_call):
        raise NotImplementedError

    def __init__(self,parent):
        if parent == None:
            self.parent = tk.Tk()
        else:
            self.parent = tk.Toplevel(parent)
        self.lbltitle = tk.Label(self.parent,text='RACE NOT LOADED')
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.setup_form('',None,None)
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=4,pady=10)
