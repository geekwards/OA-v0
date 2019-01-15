try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import tkinter.ttk as ttk

def create_race_form(parent):
    if parent == None:
        race_window = tk.Tk()
    else:
        race_window = tk.Toplevel(parent)
    
    race_form = GUI_race_form(race_window)
    return race_form,race_window

class GUI_race_form:
    cancel_click
    save_click
    close_click
    edit_click

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

    def clear(self):
        self.f1.ename.delete(0,'end')
        self.f1.eshortdescr.delete(0,'end')
        self.f1.txtdescription.delete("1.0",'end')
        self.f1.cbosize.set(0)
        self.f1.cbobody.set(0)
        self.f1.lstfoci.delete(0,'end')
        self.f1.lstfeats.delete(0,'end')
        self.f1.lstlangs.delete(0,'end')
        self.f1.estr.delete(0,'end')
        self.f1.eper.delete(0,'end')
        self.f1.eint.delete(0,'end')
        self.f1.edex.delete(0,'end')
        self.f1.echa.delete(0,'end')
        self.f1.evit.delete(0,'end')
        self.f1.emag.delete(0,'end')
        self.f1.ewill.delete(0,'end')
        self.f1.efortitude.delete(0,'end')
        self.f1.ereflex.delete(0,'end')

    def enable_form(self):
        for item in self.f1.winfo_children():
            if item.winfo_class() != 'Frame':
                item.config(state='normal')

    def disable_form(self):
        for item in self.f1.winfo_children():
            if item.winfo_class() != 'Frame':
                item.config(state='disabled')

    def add_lists(self,sizes,bodies):
        self.f1.cbosize.config(values=sizes)
        self.f1.cbobody.config(values=bodies)

    def add_item(self,race,close_call,cancel_call,edit_call,save_call,list_call):
        self.close_click = close_call
        self.cancel_click = cancel_call
        self.edit_click = edit_call
        self.save_click = save_call

        self.enable_form()
        self.parent.title("Race - " + race.name)
        self.lbltitle.config(text="Race - " + race.name)
        self.clear()
        self.f1.ename.insert(0,race.name)
        self.f1.eshortdescr.insert(0,race.short_description)
        self.f1.txtdescription.insert('end',race.description)
        self.f1.cbosize.set(race.size)
        self.f1.cbobody.set(race.body)
        for focus in race.foci:
            self.f1.lstfoci.insert(0,focus)
        for feat in race.feats:
            self.f1.lstfeats.insert(0,feat)
        for lang in race.languages_bonus:
            self.f1.lstlangs.insert(0,lang.name.strip() + ': ' + lang.short_description.strip())
        self.f1.btneditfeats.config(command=lambda: list_call('Feats'))
        self.f1.btneditfoci.config(command=lambda: list_call('Foci'))
        self.f1.btneditlang.config(command=lambda: list_call('Languages'))
        self.f1.estr.insert(0,race.str_bonus)
        self.f1.eper.insert(0,race.per_bonus)
        self.f1.eint.insert(0,race.int_bonus)
        self.f1.edex.insert(0,race.dex_bonus)
        self.f1.echa.insert(0,race.cha_bonus)
        self.f1.evit.insert(0,race.vit_bonus)
        self.f1.emag.insert(0,race.mag_bonus)
        self.f1.ewill.insert(0,race.will_bonus)
        self.f1.efortitude.insert(0,race.fortitude_bonus)
        self.f1.ereflex.insert(0,race.reflex_bonus)
        
        self.disable_form()

    def __init__(self,parent):
        self.parent = parent
        self.lbltitle = tk.Label(self.parent,text='RACE NOT LOADED')
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lblshortdescr = tk.Label(self.f1,text='Short Description')
        self.f1.lblshortdescr.grid(sticky='e',row=3,column=1,padx=5)
        self.f1.eshortdescr = tk.Entry(self.f1)
        self.f1.eshortdescr.grid(sticky='w',row=3,column=2,columnspan=3)
        self.f1.lbldescription = tk.Label(self.f1,text='Description')
        self.f1.lbldescription.grid(sticky='ne',row=4,column=1,padx=5)
        self.f1.txtdescription = tk.Text(self.f1,height=5,width=40)
        self.f1.txtdescription.grid(sticky='w',row=4,column=2,columnspan=3)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.lblsize = tk.Label(self.f1,text='Size')
        self.f1.lblsize.grid(sticky='e',row=5,column=1,padx=5)
        self.f1.cbosize = ttk.Combobox(self.f1)
        self.f1.cbosize.grid(sticky='w',row=5,column=2,columnspan=3)
        self.f1.lblbody = tk.Label(self.f1,text='Body')
        self.f1.lblbody.grid(sticky='e',row=6,column=1,padx=5)
        self.f1.cbobody = ttk.Combobox(self.f1)
        self.f1.cbobody.grid(sticky='w',row=6,column=2,columnspan=3)
        self.f1.lblfoci = tk.Label(self.f1,text='Foci')
        self.f1.lblfoci.grid(sticky='ne',row=7,column=1,padx=5)
        self.f1.lstfoci = tk.Listbox(self.f1,height=5,width=40)
        self.f1.lstfoci.grid(sticky='w',row=7,column=2,columnspan=3)
        self.f1.btneditfoci = tk.Button(self.f1,text='edit')
        self.f1.btneditfoci.config(height=2,width=10)
        self.f1.btneditfoci.grid(sticky='e',row=7,column=4)
        self.f1.lblfeats = tk.Label(self.f1,text='Feats')
        self.f1.lblfeats.grid(sticky='ne',row=8,column=1,padx=5)
        self.f1.lstfeats = tk.Listbox(self.f1,height=5,width=40)
        self.f1.lstfeats.grid(sticky='w',row=8,column=2,columnspan=3)
        self.f1.btneditfeats = tk.Button(self.f1,text='edit')
        self.f1.btneditfeats.config(height=2,width=10)
        self.f1.btneditfeats.grid(sticky='e',row=8,column=4)
        self.f1.lbllanguages = tk.Label(self.f1,text='Languages')
        self.f1.lbllanguages.grid(sticky='ne',row=9,column=1,padx=5)
        self.f1.lstlangs = tk.Listbox(self.f1,height=5,width=40)
        self.f1.lstlangs.grid(sticky='w',row=9,column=2,columnspan=3)
        self.f1.btneditlang = tk.Button(self.f1,text='edit')
        self.f1.btneditlang.config(height=2,width=10)
        self.f1.btneditlang.grid(sticky='e',row=9,column=4)
        self.f1.lblbonuses = tk.Label(self.f1,text='Bonuses')
        self.f1.lblbonuses.grid(sticky='se',row=10,column=1,pady=10)
        self.f1.lblstr = tk.Label(self.f1,text='STR Skill Pts')
        self.f1.lblstr.grid(sticky='e',row=11,column=1,padx=5)
        self.f1.estr = tk.Entry(self.f1)
        self.f1.estr.grid(sticky='w',row=11,column=2)
        self.f1.lblper = tk.Label(self.f1,text='PER Skill Pts')
        self.f1.lblper.grid(sticky='e',row=12,column=1,padx=5)
        self.f1.eper = tk.Entry(self.f1)
        self.f1.eper.grid(sticky='w',row=12,column=2)
        self.f1.lblint = tk.Label(self.f1,text='INT Skill Pts')
        self.f1.lblint.grid(sticky='e',row=13,column=1,padx=5)
        self.f1.eint = tk.Entry(self.f1)
        self.f1.eint.grid(sticky='w',row=13,column=2)
        self.f1.lbldex = tk.Label(self.f1,text='DEX Skill Pts')
        self.f1.lbldex.grid(sticky='e',row=14,column=1,padx=5)
        self.f1.edex = tk.Entry(self.f1)
        self.f1.edex.grid(sticky='w',row=14,column=2)
        self.f1.lblcha = tk.Label(self.f1,text='CHA Skill Pts')
        self.f1.lblcha.grid(sticky='e',row=15,column=1,padx=5)
        self.f1.echa = tk.Entry(self.f1)
        self.f1.echa.grid(sticky='w',row=15,column=2)
        self.f1.lblvit = tk.Label(self.f1,text='VIT Skill Pts')
        self.f1.lblvit.grid(sticky='e',row=16,column=1,padx=5)
        self.f1.evit = tk.Entry(self.f1)
        self.f1.evit.grid(sticky='w',row=16,column=2)
        self.f1.lblmag = tk.Label(self.f1,text='MAG Skill Pts')
        self.f1.lblmag.grid(sticky='e',row=17,column=1,padx=5)
        self.f1.emag = tk.Entry(self.f1)
        self.f1.emag.grid(sticky='w',row=17,column=2)
        self.f1.lblwill = tk.Label(self.f1,text='Will')
        self.f1.lblwill.grid(sticky='e',row=11,column=3,padx=5)
        self.f1.ewill = tk.Entry(self.f1)
        self.f1.ewill.grid(sticky='w',row=11,column=4)
        self.f1.lblfort = tk.Label(self.f1,text='Fortitude')
        self.f1.lblfort.grid(sticky='e',row=12,column=3,padx=5)
        self.f1.efortitude = tk.Entry(self.f1)
        self.f1.efortitude.grid(sticky='w',row=12,column=4)
        self.f1.lblreflex = tk.Label(self.f1,text='Reflex')
        self.f1.lblreflex.grid(sticky='e',row=13,column=3,padx=5)
        self.f1.ereflex = tk.Entry(self.f1)
        self.f1.ereflex.grid(sticky='w',row=13,column=4)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)
        self.left_button = tk.Button(self.parent,text='Close')
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit')
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=4,pady=10)
