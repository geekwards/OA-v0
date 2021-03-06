try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import tkinter.ttk as ttk
import easygui

class GUI_picklist_window:
    def mainloop(self):
        pass

    def destroy(self):
        pass

class GUI_picklist_form:
    def move_rt(self):
        sel = self.f1.lstsource.curselection()
        list_item = self.f1.lstsource.get(sel[0])
        if self.include_score:
            score = easygui.enterbox('Enter a score for ' + list_item + '.')
            list_item = list_item + ': ' + score

        self.f1.lstselected.insert(0,list_item)
        self.f1.lstsource.delete(sel[0])
        return False

    def move_lt(self):
        sel = self.f1.lstselected.curselection()
        if self.include_score:
            list_item,score = self.f1.lstselected.get(sel[0]).split(":",1)
        else:   
            list_item = self.f1.lstselected.get(sel[0])

        self.f1.lstsource.insert(0,list_item.strip())
        self.f1.lstselected.delete(sel[0])
        return False
    
    def add_lists(self,title,source_list,selected_list,save_call,cancel_call,score=False):
        self.include_score = score
        self.lbltitle.config(text=title)
        self.left_button.config(command=cancel_call)
        self.right_button.config(command=save_call)
        self.clear_frame()
        for item in source_list:
            self.f1.lstsource.insert(0,item)
        for sel in selected_list:
            self.f1.lstselected.insert(0,sel)

    def clear_frame(self):
        self.f1.destroy()
        self.build_frame()

    def build_frame(self):
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblsource = tk.Label(self.f1,text='Source Set')
        self.f1.lblsource.grid(sticky='nsew',row=2,column=0,pady=5,padx=5)
        self.f1.lstsource = tk.Listbox(self.f1,height=5,width=40,selectmode='single')
        self.f1.lstsource.grid(sticky='w',row=3,column=0,rowspan=3)
        self.f1.btnMoveRt = tk.Button(self.f1,text='>>')
        self.f1.btnMoveRt.config(width=10,height=2)
        self.f1.btnMoveRt.config(command=self.move_rt)
        self.f1.btnMoveRt.grid(sticky='ew',row=3,column=1,padx=5,pady=5)
        self.f1.btnMoveLt = tk.Button(self.f1,text='<<')
        self.f1.btnMoveLt.config(width=10,height=2)
        self.f1.btnMoveLt.config(command=self.move_lt)
        self.f1.btnMoveLt.grid(sticky='ew',row=5,column=1,padx=5,pady=5)
        self.f1.lblselected = tk.Label(self.f1,text='Selected Set')
        self.f1.lblselected.grid(sticky='nsew',row=2,column=2,pady=5,padx=5)
        self.f1.lstselected = tk.Listbox(self.f1,height=5,width=40,selectmode='single')
        self.f1.lstselected.grid(sticky='w',row=3,column=2,rowspan=3)
        self.f1.grid_columnconfigure(0,weight=3)
        self.f1.grid_columnconfigure(1,weight=1)
        self.f1.grid_columnconfigure(2,weight=3)

    def __init__(self,parent=None):
        self.parent = parent
        self.lbltitle = tk.Label(self.parent,text='SET NOT LOADED')
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.build_frame()
        self.left_button = tk.Button(self.parent,text='Cancel')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=6,column=0,pady=5,padx=5)
        self.right_button = tk.Button(self.parent,text='Save')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=6,column=2,pady=5,padx=5)
