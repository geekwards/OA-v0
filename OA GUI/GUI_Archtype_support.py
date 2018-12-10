import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import Archtype

def init(window,form):
    global archtype_form
    global archtype_window

    archtype_form = form
    archtype_window = window

def destroy_window():
    global archtype_window

    archtype_window.destroy()
    archtype_window = None

def close_click():
    destroy_window()

def edit_click():
    global current_archtype
    global rollback_archtype

    rollback_archtype = current_archtype.clone()

def cancel_click():
    global rollback_archtype
    global archtype_form

    archtype_form.load_form(rollback_archtype)

def save_click():
    global archtype_form
    global save_callback
    global current_archtype
    global index

    current_archtype.name = archtype_form.f1.ename.get()
    current_archtype.short_description = archtype_form.f1.eshortdescription.get()
    current_archtype.description = archtype_form.f1.txtdescription.get("1.0",'end-1c')
    current_archtype.proficiency = archtype_form.f1.eproficiency.get()
    current_archtype.str_bonus = archtype_form.f1.estr.get()
    current_archtype.per_bonus = archtype_form.f1.eper.get()
    current_archtype.int_bonus = archtype_form.f1.eint.get()
    current_archtype.dex_bonus = archtype_form.f1.edex.get()
    current_archtype.cha_bonus = archtype_form.f1.echa.get()
    current_archtype.vit_bonus = archtype_form.f1.evit.get()
    current_archtype.mag_bonus = archtype_form.f1.emag.get()
    current_archtype.stamina_bonus = archtype_form.f1.estamina.get()
    current_archtype.attack_bonus = archtype_form.f1.eattack.get()
    current_archtype.reflex_bonus = archtype_form.f1.ereflex.get()
    current_archtype.feats = archtype_form.f1.efeats.get()
    current_archtype.movement = archtype_form.f1.emvmt.get()
    current_archtype.skill_points = archtype_form.f1.eskillpts.get()
    current_archtype.level_health = archtype_form.f1.elvlhealth.get()

    save_callback(index,current_archtype)
    disable_form()

def load_data(archtype,savecall,idx):
    global archtype_form
    global save_callback
    global original_archtype
    global current_archtype
    global index

    index = idx
    original_archtype = archtype.clone()
    current_archtype = archtype.clone()

    save_callback = savecall

    archtype_form.load_form(archtype)

if __name__ == '__main__':
    import GUI_Archtype.py
    GUI_Archtype.py.vp_start_gui()
