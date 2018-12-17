import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import GUI_Archtype_support

def create_archtype_form(parent):
    global archtype_window
    global archtype_form

    if parent == None:
        archtype_window = tk.Tk()
    else:
        archtype_window = tk.Toplevel(parent)
    archtype_form = ArchtypeForm(archtype_window)
    GUI_Archtype_support.init(archtype_window,archtype_form)
    return (archtype_window,archtype_form)

def destroy_archtype_form():
    global archtype_window

    archtype_window.destroy()
    archtype_window = None

def close_click():
    GUI_Archtype_support.close_click()

def edit_click():
    global archtype_form

    archtype_form.set_for_edit()
    GUI_Archtype_support.edit_click()

def cancel_click():
    global archtype_form

    archtype_form.set_for_view()
    GUI_Archtype_support.cancel_click()

def save_click():
    global archtype_form

    archtype_form.set_for_view()
    GUI_Archtype_support.save_click()

def load_data(archtype,savecall,idx):
    GUI_Archtype_support.load_data(archtype,savecall,idx)

class ArchtypeForm:

    def set_for_edit(self):
        self.left_button.config(text='Cancel')
        self.left_button.config(command=cancel_click)
        self.right_button.config(text='Save')
        self.right_button.config(command=save_click)
        self.enable_form()

    def set_for_view(self):
        self.left_button.config(text='Close')
        self.left_button.config(command=close_click)
        self.right_button.config(text='Edit')
        self.right_button.config(command=edit_click)
        self.disable_form()

    def enable_form(self):
        self.f1.ename.config(state='normal')
        self.f1.eshortdescription.config(state='normal')
        self.f1.eproficiency.config(state='normal')
        self.f1.estr.config(state='normal')
        self.f1.eper.config(state='normal')
        self.f1.eint.config(state='normal')
        self.f1.edex.config(state='normal')
        self.f1.echa.config(state='normal')
        self.f1.evit.config(state='normal')
        self.f1.emag.config(state='normal')
        self.f1.estamina.config(state='normal')
        self.f1.eattack.config(state='normal')
        self.f1.ereflex.config(state='normal')
        self.f1.efeats.config(state='normal')
        self.f1.emvmt.config(state='normal')
        self.f1.eskillpts.config(state='normal')
        self.f1.elvlhealth.config(state='normal')

    def disable_form(self):
        self.f1.ename.config(state='disabled')
        self.f1.eshortdescription.config(state='disabled')
        self.f1.eproficiency.config(state='disabled')
        self.f1.estr.config(state='disabled')
        self.f1.eper.config(state='disabled')
        self.f1.eint.config(state='disabled')
        self.f1.edex.config(state='disabled')
        self.f1.echa.config(state='disabled')
        self.f1.evit.config(state='disabled')
        self.f1.emag.config(state='disabled')
        self.f1.estamina.config(state='disabled')
        self.f1.eattack.config(state='disabled')
        self.f1.ereflex.config(state='disabled')
        self.f1.efeats.config(state='disabled')
        self.f1.emvmt.config(state='disabled')
        self.f1.eskillpts.config(state='disabled')
        self.f1.elvlhealth.config(state='disabled')

    def load_form(self,archtype):
        if archtype.isempty():
            edit_click()

        self.enable_form()
        self.parent.title("Archtype - " + archtype.name)
        self.lbltitle.config(text="Archtype - " + archtype.name)
        self.f1.ename.delete(0,'end')
        self.f1.ename.insert(0,archtype.name)
        self.f1.eshortdescription.delete(0,'end')
        self.f1.eshortdescription.insert(0,archtype.short_description)
        self.f1.txtdescription.delete("1.0",'end')
        self.f1.txtdescription.insert('end',archtype.description)
        self.f1.eproficiency.delete(0,'end')
        self.f1.eproficiency.insert(0,archtype.proficiency)
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
        self.f1.estamina.delete(0,'end')
        self.f1.estamina.insert(0,archtype.stamina_bonus)
        self.f1.eattack.delete(0,'end')
        self.f1.eattack.insert(0,archtype.attack_bonus)
        self.f1.ereflex.delete(0,'end')
        self.f1.ereflex.insert(0,archtype.reflex_bonus)
        self.f1.efeats.delete(0,'end')
        self.f1.efeats.insert(0,archtype.feats)
        self.f1.emvmt.delete(0,'end')
        self.f1.emvmt.insert(0,archtype.movement)
        self.f1.eskillpts.delete(0,'end')
        self.f1.eskillpts.insert(0,archtype.skill_points)
        self.f1.elvlhealth.delete(0,'end')
        self.f1.elvlhealth.insert(0,archtype.level_health)
        self.disable_form()

    def __init__(self,parent):
        self.parent = parent
        self.parent.title("ARCHTYPE NOT LOADED")
        self.lbltitle = tk.Label(self.parent,text='ARCHTYPE NOT LOADED')
        self.lbltitle.config(font=app_config.title_font)
        self.lbltitle.grid(sticky='nsew',row=0,column=0,columnspan=6,rowspan=2,pady=20)
        self.f1 = tk.Frame(self.parent)
        self.f1.grid(sticky='nsew',row=2,column=0,padx=20,pady=20)
        self.f1.lblname = tk.Label(self.f1,text='Name')
        self.f1.lblname.grid(sticky='e',row=2,column=1,padx=5)
        self.f1.ename = tk.Entry(self.f1)
        self.f1.ename.insert(0,'<NAME>')
        self.f1.ename.grid(sticky='w',row=2,column=2,columnspan=3)
        self.f1.lblproficiency = tk.Label(self.f1, text='Proficiency')
        self.f1.lblproficiency.grid(sticky='e',row=3,column=1,padx=5)
        self.f1.eproficiency = tk.Entry(self.f1)
        self.f1.eproficiency.insert(0,'<PROFICIENCY>')
        self.f1.eproficiency.grid(sticky='w',row=3,column=2,columnspan=3)
        self.f1.lblshortdescription = tk.Label(self.f1,text='Short Description')
        self.f1.lblshortdescription.grid(sticky='e',row=4,column=1,padx=5)
        self.f1.eshortdescription = tk.Entry(self.f1)
        self.f1.eshortdescription.insert(0,'<SHORT DESCR>')
        self.f1.eshortdescription.grid(sticky='w',row=4,column=2,columnspan=3)
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
        self.f1.lblfeats = tk.Label(self.f1,text='Feats')
        self.f1.lblfeats.grid(sticky='e',row=9,column=3,padx=5)
        self.f1.lblmvmt = tk.Label(self.f1,text='Mvmt')
        self.f1.lblmvmt.grid(sticky='e',row=10,column=3,padx=5)
        self.f1.lblskillpts = tk.Label(self.f1,text='Skill Pts')
        self.f1.lblskillpts.grid(sticky='e',row=11,column=3,padx=5)
        self.f1.lblvlhealth = tk.Label(self.f1,text='Lvl Health')
        self.f1.lblvlhealth.grid(sticky='e',row=12,column=3,padx=5)
        self.f1.efeats = tk.Entry(self.f1)
        self.f1.efeats.insert(0,'<FEATS>')
        self.f1.efeats.grid(sticky='w',row=9,column=4)
        self.f1.emvmt = tk.Entry(self.f1)
        self.f1.emvmt.insert(0,'<MVMT>')
        self.f1.emvmt.grid(sticky='w',row=10,column=4)
        self.f1.eskillpts = tk.Entry(self.f1)
        self.f1.eskillpts.insert(0,'<SKILL PTS>')
        self.f1.eskillpts.grid(sticky='w',row=11,column=4)
        self.f1.elvlhealth = tk.Entry(self.f1)
        self.f1.elvlhealth.insert(0,'<LVL HEALTH>')
        self.f1.elvlhealth.grid(sticky='w',row=12, column=4)
        self.f1.lblstamina = tk.Label(self.f1,text='Stamina')
        self.f1.lblstamina.grid(sticky='e',row=13,column=3,padx=5)
        self.f1.estamina = tk.Entry(self.f1)
        self.f1.estamina.insert(0,'<STAMINA>')
        self.f1.estamina.grid(sticky='w',row=13,column=4)
        self.f1.lblattack = tk.Label(self.f1,text='Attack')
        self.f1.lblattack.grid(sticky='e',row=14,column=3,padx=5)
        self.f1.lblreflex = tk.Label(self.f1,text='Reflex')
        self.f1.lblreflex.grid(sticky='e',row=15,column=3,padx=5)
        self.f1.eattack = tk.Entry(self.f1)
        self.f1.eattack.insert(0,'<ATTACK>')
        self.f1.eattack.grid(sticky='w',row=14,column=4)
        self.f1.ereflex = tk.Entry(self.f1)
        self.f1.ereflex.insert(0,'<REFLEX>')
        self.f1.ereflex.grid(sticky='w',row=15,column=4)
        self.f1.grid_columnconfigure(0,weight=1)
        self.f1.grid_columnconfigure(1,weight=3)
        self.f1.grid_columnconfigure(2,weight=3)
        self.f1.grid_columnconfigure(3,weight=1)
        self.f1.grid_columnconfigure(4,weight=3)
        self.f1.grid_columnconfigure(5,weight=3)
        self.f1.grid_columnconfigure(6,weight=1)
        self.left_button = tk.Button(self.parent,text='Close',command=close_click)
        self.left_button.config(width=10,height=2)
        self.left_button.grid(sticky='w',row=16,column=2,pady=10)
        self.right_button = tk.Button(self.parent,text='Edit',command=edit_click)
        self.right_button.config(width=10,height=2)
        self.right_button.grid(sticky='w',row=16,column=4,pady=10)
