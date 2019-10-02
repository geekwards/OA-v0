try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

class GUI_misc_list_window:
    def mainloop(self):
        pass

    def destroy(self):
        pass

class GUI_misc_list_form:
    def add_item(self,idx,item):
        self.f1.elist_item = tk.Entry(self.f1)
        self.f1.elist_item.grid(sticky='w',row=idx+2,column=1,padx=5,pady=5)
        self.f1.elist_item.insert(0,item.name)
        self.f1.txtdescription = tk.Text(self.f1,height=5,width=20)
        self.f1.txtdescription.grid(sticky='w',row=idx+2,column=2,padx=5,pady=5)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.txtdescription.insert('end',item.short_description)

    def setup_form(self,list_title,new_call,edit_call,save_call,close_call,cancel_call):
        self.new_click = new_call
        self.edit_click = edit_call
        self.save_click = save_call
        self.close_click = close_call
        self.cancel_click = cancel_call
        self.lbltitle.config(text=list_title)
        self.left_button.config(command=self.close_click)
        self.center_button.config(command=self.new_click)
        self.right_button.config(command=self.edit_click)
        self.clear_frame()
        
    def set_edit(self,for_new=False):
        if for_new:
            self.lbltitle.destroy()
            self.etitle = tk.Entry(self.parent)
            self.etitle.grid(sticky='w',row=0,column=1,padx=5,pady=5)

        self.left_button.config(text='Cancel')
        self.left_button.config(command=self.cancel_click)
        self.center_button.config(state='normal')
        self.right_button.config(text='Save')
        self.right_button.config(command=self.save_click)
        self.enable_form()

    def set_view(self):
        self.left_button.config(text='Close')
        self.left_button.config(command=self.close_click)
        self.center_button.config(state='disabled')
        self.right_button.config(text='Edit')
        self.right_button.config(command=self.edit_click)
        self.disable_form()

    def enable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            item.config(state='disabled')

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
        self.build_frame()
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
