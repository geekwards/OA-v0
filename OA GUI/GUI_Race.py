import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import GUI_Race_support

def create_race_form(parent):
    global race_window
    global race_form

    if parent == None:
        race_window = tk.Tk()
    else:
        race_window = tk.Toplevel(parent)
    race_form = RaceForm(race_window)
    GUI_Race_support.init(race_window,race_form)
    return (race_window,race_form)

def destroy_race_form():
    global race_window

    race_window.destroy()
    race_window = None

def close_click():
    GUI_Race_support.close_click()

def edit_click():
    global race_form

    race_form.set_for_edit()
    GUI_Race_support.edit_click()

def cancel_click():
    global race_form

    race_form.set_for_view()
    GUI_Race_support.cancel_click()

def save_click():
    global race_form

    race_form.set_for_view()
    GUI_Race_support.save_click()

def load_data(race,savecall,idx):
    GUI_Race_support.load_data(race,savecall,idx)

class RaceForm:

    def set_for_edit(self):
        self.f1.left_button.config(text='Cancel')
        self.f1.left_button.config(command=cancel_click)
        self.f1.right_button.config(text='Save')
        self.f1.right_button.config(command=save_click)
        self.enable_form()

    def set_for_view(self):
        self.f1.left_button.config(text='Close')
        self.f1.left_button.config(command=close_click)
        self.f1.right_button.config(text='Edit')
        self.f1.right_button.config(command=edit_click)
        self.disable_form()

    def enable_form(self):
        self.f1.ename.config(state='normal')
        self.f1.estr.config(state='normal')
        self.f1.eper.config(state='normal')
        self.f1.eint.config(state='normal')
        self.f1.edex.config(state='normal')
        self.f1.echa.config(state='normal')
        self.f1.evit.config(state='normal')
        self.f1.emag.config(state='normal')
        self.f1.ewill.config(state='normal')
        self.f1.efortitude.config(state='normal')
        self.f1.ereflex.config(state='normal')

    def disable_form(self):
        self.f1.ename.config(state='disabled')
        self.f1.ename.config(state='disabled')
        self.f1.estr.config(state='disabled')
        self.f1.eper.config(state='disabled')
        self.f1.eint.config(state='disabled')
        self.f1.edex.config(state='disabled')
        self.f1.echa.config(state='disabled')
        self.f1.evit.config(state='disabled')
        self.f1.emag.config(state='disabled')
        self.f1.ewill.config(state='disabled')
        self.f1.efortitude.config(state='disabled')
        self.f1.ereflex.config(state='disabled')

    def load_form(self,race):
        if race.isempty():
            edit_click()

        self.enable_form()
        self.parent.title("Race - " + race.name)
        self.lbltitle.config(text="Race - " + race.name)
        self.f1.ename.delete(0,'end')
        self.f1.ename.insert(0,archtype.name)
        self.f1.txtdescription.delete("1.0",'end')
        self.f1.txtdescription.insert('end',archtype.description)
        self.f1.estr.delete(0,'end')
        self.f1.estr.insert(0,archtype.str_bonus)
        self.f1.eper.delete(0,'end')
        self.f1.eper.insert(0,archtype.per_bonus)
        self.f1.eint.delete(0,'end')
        self.f1.eint.insert(0,archtype.int_bonus)
        self.f1.edex.delete(0,'end')
        self.f1.edex.insert(0,archtype.dex_bonus)
        self.f1.echa.delete(0,'end')
        self.f1.echa.insert(0,archtype.cha_bonus)
        self.f1.evit.delete(0,'end')
        self.f1.evit.insert(0,archtype.vit_bonus)
        self.f1.emag.delete(0,'end')
        self.f1.emag.insert(0,archtype.mag_bonus)
        self.f1.ewill.delete(0,'end')
        self.f1.ewill.insert(0,archtype.stamina_bonus)
        self.f1.efortitude.delete(0,'end')
        self.f1.efortitude.insert(0,archtype.attack_bonus)
        self.f1.ereflex.delete(0,'end')
        self.f1.ereflex.insert(0,archtype.reflex_bonus)
        self.disable_form()

    def __init__(self,parent):
        self.parent = parent
        self.parent.title('RACE NOT LOADED')
        self.lbltitle = tk.Label(self.parent,text='RACE NOT LOADED')
        self.lbltitle.config(font=app_config.title_font)
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.insert(0,'<NAME>')
        self.f1.ename.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lbldescription = tk.Label(self.f1,text='Description')
        self.f1.lbldescription.grid(sticky='ne',row=5,column=1,padx=5)
        self.f1.txtdescription = tk.Text(self.f1,height=20,width=40)
        self.f1.txtdescription.grid(sticky='w',row=5,column=2,columnspan=3)
        self.f1.txtdescription.configure(wrap='word')
        self.f1.lblbonuses = tk.Label(self.f1,text='Bonuses')
        self.f1.lblbonuses.grid(sticky='se',row=7,column=1,rowspan=2,pady=10)
        self.f1.lblstr = tk.Label(self.f1,text='STR')
        self.f1.lblstr.grid(sticky='e',row=9,column=1,padx=5)
        self.f1.estr = tk.Entry(self.f1)
        self.f1.estr.insert(0,'<STR>')
        self.f1.estr.grid(sticky='w',row=9,column=2)
        self.f1.lblper = tk.Label(self.f1,text='PER')
        self.f1.lblper.grid(sticky='e',row=10,column=1,padx=5)
        self.f1.eper = tk.Entry(self.f1)
        self.f1.eper.insert(0,'<PER>')
        self.f1.eper.grid(sticky='w',row=10,column=2)
        self.f1.lblint = tk.Label(self.f1,text='INT')
        self.f1.lblint.grid(sticky='e',row=11,column=1,padx=5)
        self.f1.eint = tk.Entry(self.f1)
        self.f1.eint.insert(0,'<INT>')
        self.f1.eint.grid(sticky='w',row=11,column=2)
        self.f1.lbldex = tk.Label(self.f1,text='DEX')
        self.f1.lbldex.grid(sticky='e',row=12,column=1,padx=5)
        self.f1.lblcha = tk.Label(self.f1,text='CHA')
        self.f1.lblcha.grid(sticky='e',row=13,column=1,padx=5)
        self.f1.lblvit = tk.Label(self.f1,text='VIT')
        self.f1.lblvit.grid(sticky='e',row=14,column=1,padx=5)
        self.f1.lblmag = tk.Label(self.f1,text='MAG')
        self.f1.lblmag.grid(sticky='e',row=15,column=1,padx=5)
        self.f1.edex = tk.Entry(self.f1)
        self.f1.edex.insert(0,'<DEX>')
        self.f1.edex.grid(sticky='w',row=12,column=2)
        self.f1.echa = tk.Entry(self.f1)
        self.f1.echa.insert(0,'<CHA>')
        self.f1.echa.grid(sticky='w',row=13,column=2)
        self.f1.evit = tk.Entry(self.f1)
        self.f1.evit.insert(0,'<VIT>')
        self.f1.evit.grid(sticky='w',row=14,column=2)
        self.f1.emag = tk.Entry(self.f1)
        self.f1.emag.insert(0,'<MAG>')
        self.f1.emag.grid(sticky='w',row=15,column=2)
        self.f1.lblwill = tk.Label(self.f1,text='Mvmt')
        self.f1.lblwill.grid(sticky='e',row=10,column=3,padx=5)
        self.f1.lblfort = tk.Label(self.f1,text='Skill Pts')
        self.f1.lblfort.grid(sticky='e',row=11,column=3,padx=5)
        self.f1.ewill = tk.Entry(self.f1)
        self.f1.ewill.insert(0,'<MVMT>')
        self.f1.ewill.grid(sticky='w',row=10,column=4)
        self.f1.efort = tk.Entry(self.f1)
        self.f1.efort.insert(0,'<SKILL PTS>')
        self.f1.efort.grid(sticky='w',row=11,column=4)
        self.f1.lblreflex = tk.Label(self.f1,text='Reflex')
        self.f1.lblreflex.grid(sticky='e',row=15,column=3,padx=5)
        self.f1.ereflex = tk.Entry(self.f1)
        self.f1.ereflex.insert(0,'<REFLEX>')
        self.f1.ereflex.grid(sticky='w',row=15,column=4)
        self.f1.left_button = tk.Button(self.f1,text='Close',command=close_click)
        self.f1.left_button.config(width=10,height=2)
        self.f1.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.f1.right_button = tk.Button(self.f1,text='Edit',command=edit_click)
        self.f1.right_button.config(width=10,height=2)
        self.f1.right_button.grid(sticky='w',row=16,column=4,pady=10)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)
