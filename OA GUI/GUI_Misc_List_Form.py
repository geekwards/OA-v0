try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

def create_misc_list_form(parent):
    if parent == None:
        misc_list_window = tk.Tk()
    else:
        misc_list_window = tk.Toplevel(parent)
    
    misc_list_form = GUI_misc_list_form(misc_list_window)
    return misc_list_form,misc_list_window

class GUI_misc_list_form:
    #todo: formatting
    def setup(self,list_title,new_call,close_call,edit_call,save_call,cancel_call):
        global new_click
        global close_click
        global edit_click
        global save_click
        global cancel_click

        new_click = new_call
        close_click = close_call
        edit_click = edit_call
        save_click = save_call
        cancel_click = cancel_call

        self.parent.title("OA Manager - " + list_title)
        self.lbltitle.config(text=list_title)
        self.left_button.config(command=close_click)
        self.center_button.config(command=new_click)
        self.right_button.config(command=edit_click)
        self.clear()
        
    def set_edit(self,for_new=False):
        global cancel_click
        global save_click

        if for_new:
            self.lbltitle.destroy()
            self.etitle = tk.Entry(self.parent)
            self.etitle.grid(sticky='w',row=0,column=1,padx=5,pady=5)

        self.left_button.config(text='Cancel')
        self.left_button.config(command=cancel_click)
        self.center_button.config(state='normal')
        self.right_button.config(text='Save')
        self.right_button.config(command=save_click)
        self.enable_form()

    def set_view(self):
        global close_click
        global edit_click

        self.left_button.config(text='Close')
        self.left_button.config(command=close_click)
        self.center_button.config(state='disabled')
        self.right_button.config(text='Edit')
        self.right_button.config(command=edit_click)
        self.disable_form()

    def clear(self):
        self.f1.destroy()
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=1)

    def enable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='disabled')

    def add_item(self,idx,item_text):
        self.f1.elist_item = tk.Entry(self.f1)
        self.f1.elist_item.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        self.f1.elist_item.insert(0,item_text)

    def __init__(self,parent):
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
        self.center_button = tk.Button(self.parent,text='New')
        self.center_button.config(width=10,height=2)
        self.center_button.grid(sticky='sw',row=3,column=1,padx=20,pady=20)
        self.right_button = tk.Button(self.parent,text='Edit')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='sw',row=3,column=2,padx=20,pady=20)
