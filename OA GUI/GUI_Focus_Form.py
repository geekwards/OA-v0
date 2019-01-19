try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import tkinter.ttk as ttk

def create_form(parent):
    if parent == None:
        focus_window = tk.Tk()
    else:
        focus_window = tk.Toplevel(parent)
    
    focus_form = GUI_focus_form(focus_window)
    return focus_form,focus_window

class GUI_focus_form:
    def add_item(self,focus,edit_call,save_call,close_call,cancel_call,list_call):
        self.close_click = close_call
        self.cancel_click = cancel_call
        self.edit_click = edit_call
        self.save_click = save_call

        self.enable_form()
        self.parent.title("Focus - " + focus.name)
        self.lbltitle.config(text="Focus - " + focus.name)
        self.clear_frame()
        self.f1.ename.insert(0,focus.name)
        self.f1.eshortdescr.insert(0,focus.short_description)
        self.f1.txtdescription.insert('end',focus.description)
        for lang in focus.languages_bonus:
            self.f1.lstlangs.insert(0,lang.name.strip() + ': ' + lang.short_description.strip())
        self.f1.btneditlang.config(command=lambda: list_call('Languages'))
        self.f1.estr.insert(0,focus.str_bonus)
        self.f1.eper.insert(0,focus.per_bonus)
        self.f1.eint.insert(0,focus.int_bonus)
        self.f1.edex.insert(0,focus.dex_bonus)
        self.f1.echa.insert(0,focus.cha_bonus)
        self.f1.evit.insert(0,focus.vit_bonus)
        self.f1.emag.insert(0,focus.mag_bonus)
        self.f1.estrskill.insert(0,focus.str_skill_bonus)
        self.f1.eperskill.insert(0,focus.per_skill_bonus)
        self.f1.eintskill.insert(0,focus.int_skill_bonus)
        self.f1.edexskill.insert(0,focus.dex_skill_bonus)
        self.f1.echaskill.insert(0,focus.cha_skill_bonus)
        self.f1.evitskill.insert(0,focus.vit_skill_bonus)
        self.f1.emagskill.insert(0,focus.mag_skill_bonus)
        self.f1.ewill.insert(0,focus.will_bonus)
        self.f1.efortitude.insert(0,focus.fortitude_bonus)
        self.f1.ereflex.insert(0,focus.reflex_bonus)
        
        self.disable_form()

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

    def clear_frame(self):
        self.f1.destroy()
        self.build_frame()
    
    def build_frame(self):
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=1,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.grid(sticky='w',row=1,column=2,columnspan=3)
        self.f1.lblshortdescr = tk.Label(self.f1,text='Short Description')
        self.f1.lblshortdescr.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.eshortdescr = tk.Entry(self.f1)
        self.f1.eshortdescr.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lbldescription = tk.Label(self.f1,text='Description')
        self.f1.lbldescription.grid(sticky='ne',row=3,column=1,padx=5)
        self.f1.txtdescription = tk.Text(self.f1,height=5,width=40)
        self.f1.txtdescription.grid(sticky='w',row=3,column=2,columnspan=3)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.lbllanguages = tk.Label(self.f1,text='Languages')
        self.f1.lbllanguages.grid(sticky='ne',row=4,column=1,padx=5)
        self.f1.lstlangs = tk.Listbox(self.f1,height=5,width=40)
        self.f1.lstlangs.grid(sticky='w',row=4,column=2,columnspan=3)
        self.f1.btneditlang = tk.Button(self.f1,text='edit')
        self.f1.btneditlang.config(height=2,width=10)
        self.f1.btneditlang.grid(sticky='e',row=4,column=4)
        self.f1.lblbonuses = tk.Label(self.f1,text='Bonuses')
        self.f1.lblbonuses.grid(sticky='se',row=5,column=1,pady=10)
        self.f1.lblstr = tk.Label(self.f1,text='STR Bonus')
        self.f1.lblstr.grid(sticky='e',row=6,column=1,padx=5)
        self.f1.estr = tk.Entry(self.f1)
        self.f1.estr.grid(sticky='w',row=6,column=2)
        self.f1.lblper = tk.Label(self.f1,text='PER Bonus')
        self.f1.lblper.grid(sticky='e',row=7,column=1,padx=5)
        self.f1.eper = tk.Entry(self.f1)
        self.f1.eper.grid(sticky='w',row=7,column=2)
        self.f1.lblint = tk.Label(self.f1,text='INT Bonus')
        self.f1.lblint.grid(sticky='e',row=8,column=1,padx=5)
        self.f1.eint = tk.Entry(self.f1)
        self.f1.eint.grid(sticky='w',row=8,column=2)
        self.f1.lbldex = tk.Label(self.f1,text='DEX Bonus')
        self.f1.lbldex.grid(sticky='e',row=9,column=1,padx=5)
        self.f1.edex = tk.Entry(self.f1)
        self.f1.edex.grid(sticky='w',row=9,column=2)
        self.f1.lblcha = tk.Label(self.f1,text='CHA Bonus')
        self.f1.lblcha.grid(sticky='e',row=10,column=1,padx=5)
        self.f1.echa = tk.Entry(self.f1)
        self.f1.echa.grid(sticky='w',row=10,column=2)
        self.f1.lblvit = tk.Label(self.f1,text='VIT Bonus')
        self.f1.lblvit.grid(sticky='e',row=11,column=1,padx=5)
        self.f1.evit = tk.Entry(self.f1)
        self.f1.evit.grid(sticky='w',row=11,column=2)
        self.f1.lblmag = tk.Label(self.f1,text='MAG Bonus')
        self.f1.lblmag.grid(sticky='e',row=12,column=1,padx=5)
        self.f1.emag = tk.Entry(self.f1)
        self.f1.emag.grid(sticky='w',row=12,column=2)
        self.f1.lblstrskill = tk.Label(self.f1,text='STR Skill Pts')
        self.f1.lblstrskill.grid(sticky='e',row=6,column=3,padx=5)
        self.f1.estrskill = tk.Entry(self.f1)
        self.f1.estrskill.grid(sticky='w',row=6,column=4)
        self.f1.lblperskill = tk.Label(self.f1,text='PER Skill Pts')
        self.f1.lblperskill.grid(sticky='e',row=7,column=3,padx=5)
        self.f1.eperskill = tk.Entry(self.f1)
        self.f1.eperskill.grid(sticky='w',row=7,column=4)
        self.f1.lblintskill = tk.Label(self.f1,text='INT Skill Pts')
        self.f1.lblintskill.grid(sticky='e',row=8,column=3,padx=5)
        self.f1.eintskill = tk.Entry(self.f1)
        self.f1.eintskill.grid(sticky='w',row=8,column=4)
        self.f1.lbldexskill = tk.Label(self.f1,text='DEX Skill Pts')
        self.f1.lbldexskill.grid(sticky='e',row=9,column=3,padx=5)
        self.f1.edexskill = tk.Entry(self.f1)
        self.f1.edexskill.grid(sticky='w',row=9,column=4)
        self.f1.lblchaskill = tk.Label(self.f1,text='CHA Skill Pts')
        self.f1.lblchaskill.grid(sticky='e',row=10,column=3,padx=5)
        self.f1.echaskill = tk.Entry(self.f1)
        self.f1.echaskill.grid(sticky='w',row=10,column=4)
        self.f1.lblvitskill = tk.Label(self.f1,text='VIT Skill Pts')
        self.f1.lblvitskill.grid(sticky='e',row=11,column=3,padx=5)
        self.f1.evitskill = tk.Entry(self.f1)
        self.f1.evitskill.grid(sticky='w',row=11,column=4)
        self.f1.lblmagskill = tk.Label(self.f1,text='MAG Skill Pts')
        self.f1.lblmagskill.grid(sticky='e',row=12,column=3,padx=5)
        self.f1.emagskill = tk.Entry(self.f1)
        self.f1.emagskill.grid(sticky='w',row=12,column=4)
        self.f1.lblwill = tk.Label(self.f1,text='Will')
        self.f1.lblwill.grid(sticky='e',row=13,column=1,padx=5)
        self.f1.ewill = tk.Entry(self.f1)
        self.f1.ewill.grid(sticky='w',row=13,column=2)
        self.f1.lblfort = tk.Label(self.f1,text='Fortitude')
        self.f1.lblfort.grid(sticky='e',row=14,column=1,padx=5)
        self.f1.efortitude = tk.Entry(self.f1)
        self.f1.efortitude.grid(sticky='w',row=14,column=2)
        self.f1.lblreflex = tk.Label(self.f1,text='Reflex')
        self.f1.lblreflex.grid(sticky='e',row=15,column=1,padx=5)
        self.f1.ereflex = tk.Entry(self.f1)
        self.f1.ereflex.grid(sticky='w',row=15,column=2)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)

    def __init__(self,parent):
        self.parent = parent
        self.lbltitle = tk.Label(self.parent,text='FOCUS NOT LOADED')
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.build_frame()
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=4,pady=10)
