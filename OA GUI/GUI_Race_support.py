import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
import app_config

import Race

def init(window,form):
    global race_form
    global race_window

    race_form = form
    race_window = window

def destroy_window():
    global race_window

    race_window.destroy()
    race_window = None

def close_click():
    destroy_window()

def edit_click():
    global current_race
    global rollback_race

    rollback_race = current_race.clone()

def cancel_click():
    global rollback_race
    global race_form

    if not(rollback_race.isempty()):
        race_form.load_form(rollback_race)

def save_click():
    global rollback_race
    global save_callback
    global current_race
    global index

    current_race.name = race_form.f1.ename.get()
    current_race.description = race_form.f1.txtdescription.get("1.0",'end-1c')
    current_race.size = race_form.f1.esize.get()
    current_race.body_type = race_form.f1.ebody_type.get()
    current_race.str_bonus = race_form.f1.estr.get()
    current_race.per_bonus = race_form.f1.eper.get()
    current_race.int_bonus = race_form.f1.eint.get()
    current_race.dex_bonus = race_form.f1.edex.get()
    current_race.cha_bonus = race_form.f1.echa.get()
    current_race.vit_bonus = race_form.f1.evit.get()
    current_race.mag_bonus = race_form.f1.emag.get()
    current_race.will_bonus = race_form.f1.ewill.get()
    current_race.fort_bonus = race_form.f1.efort.get()
    current_race.reflex_bonus = race_form.f1.ereflex.get()

    save_callback(index,current_race)
    race_form.disable_form()

def load_data(race,savecall,idx):
    global race_form
    global save_callback
    global original_race
    global current_race
    global index

    index = idx
    original_race = race.clone()
    current_race = race.clone()

    save_callback = savecall

    race_form.load_form(race)

if __name__ == '__main__':
    import race.py
    GUI_Archtype.py.vp_start_gui()
