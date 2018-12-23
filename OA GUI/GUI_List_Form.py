try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

def create_list_form(parent):
    if parent == None:
        list_window = tk.Tk()
    else:
        list_window = tk.Toplevel(parent)
    
    list_form = GUI_list_form(list_window)
    return list_form, list_window

class GUI_list_form:
    #todo: formatting
    def setup(self,list_title,new_call,close_call,edit_call,remove_call):
        global new_click
        global close_click
        global edit_click
        global remove_click

        new_click = new_call
        close_click = close_call
        edit_click = edit_call
        remove_click = remove_call

        self.parent.title("OA Manager - " + list_title)
        self.lbltitle.config(text=list_title)
        self.left_button.config(command=close_click)
        self.right_button.config(command=new_click)
        self.clear()

    def add_item(self,idx,item_text):
        global edit_click
        global remove_click

        self.f1.edit_list_item = tk.Button(self.f1,text ="Edit",command=lambda: edit_click(idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=0,padx=5,pady=5)
        self.f1.lbl_list_item = tk.Label(self.f1,text=item_text)
        self.f1.lbl_list_item.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        self.f1.edit_list_item = tk.Button(self.f1,text ="Remove",command=lambda: remove_click(idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=2,padx=5,pady=5)

    def clear(self):
        self.f1.destroy()
        self.f1 = tk.Frame()
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=1)

    def __init__(self, parent):
        global close_click
        global new_click

        self.parent = parent
        self.parent.title("LIST NOT LOADED")
        self.f1 = tk.Frame()
        self.clear()
        self.lbltitle = tk.Label(self.parent,text='LIST NOT LOADED')
        #self.lbltitle.configure(font=app_config.title_font)
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=3,rowspan=2,pady=20)
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='sw',row=3,column=0,padx=20,pady=20)
        self.right_button = tk.Button(self.parent,text='NEW')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='sw',row=3,column=2,padx=20,pady=20)
   