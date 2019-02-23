try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

def create_list_form(parent=None):
    if parent == None:
        list_window = tk.Tk()
    else:
        list_window = tk.Toplevel(parent)
    
    list_form = GUI_list_form(list_window)
    return list_form, list_window

class GUI_list_form:
    def add_item(self,idx,item_text,set_edit=True):
        self.f1.edit_list_item = tk.Button(self.f1,text="View",command=lambda: self.edit_click(idx))
        self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=0,padx=5,pady=5)
        self.f1.lbl_list_item = tk.Label(self.f1,text=item_text)
        self.f1.lbl_list_item.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        if set_edit:
            self.f1.edit_list_item = tk.Button(self.f1,text="Remove",command=lambda: self.remove_click(idx))
            self.f1.edit_list_item.grid(sticky='nsew',row=idx+2,column=2,padx=5,pady=5)

    def setup_form(self,list_title,new_call,edit_call,remove_call,close_call,set_edit=True):
        self.new_click = new_call
        self.close_click = close_call
        self.edit_click = edit_call
        self.remove_click = remove_call

        self.parent.title("OA Manager - " + list_title)
        self.lbltitle.config(text=list_title)
        self.left_button.config(command=self.close_click)
        if set_edit:
            self.right_button.config(command=self.new_click)
        else:
            self.right_button.destroy()

        self.clear_frame()

    def clear_frame(self):
        self.f1.destroy()
        self.build_frame()

    def build_frame(self):
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=1)

    def __init__(self,parent=None):
        self.parent = parent
        self.parent.title("LIST NOT LOADED")
        self.build_frame()
        self.lbltitle = tk.Label(self.parent,text='LIST NOT LOADED')
        #self.lbltitle.configure(font=app_config.title_font)
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=3,rowspan=2,pady=20)
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='sw',row=3,column=0,padx=20,pady=20)
        self.right_button = tk.Button(self.parent,text='NEW')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='sw',row=3,column=2,padx=20,pady=20)
   