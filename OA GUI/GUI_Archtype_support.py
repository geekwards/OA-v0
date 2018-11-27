#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 25, 2018 01:38:26 PM EST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))

import ArchType

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    global w

    top_level.destroy()
    w = None

def btnClose_Click():
    destroy_window()

def loadForm(archtype):
    global w
    global top_level

    top_level.title("Archtype - " + archtype.name)
    w.lblTitle.config(text="Archtype - " + archtype.name)
    w.roName.config(text=archtype.name)
    w.txtDescription.delete("1.0",'end')
    w.txtDescription.insert('end',archtype.description)
    w.roProficiency.config(text=archtype.proficiency)
    w.roSTR.config(text=str(archtype.strBonus))
    w.roPER.config(text=str(archtype.perBonus))
    w.roINT.config(text=str(archtype.intBonus))
    w.roDEX.config(text=str(archtype.dexBonus))
    w.roCHA.config(text=str(archtype.chaBonus))
    w.roVIT.config(text=str(archtype.vitBonus))
    w.roMAG.config(text=str(archtype.magBonus))
    w.roStamina.config(text=str(archtype.staminaBonus))
    w.roAttack.config(text=str(archtype.attackBonus))
    w.roReflex.config(text=str(archtype.reflexBonus))
    w.roFeats.config(text=archtype.feats)
    w.roMvmt.config(text=str(archtype.movement))
    w.roSkillPts.config(text=str(archtype.skillPoints))
    w.roLvlHealth.config(text=archtype.levelHealth)

if __name__ == '__main__':
    import GUI_Archtype.py
    GUI_Archtype.py.vp_start_gui()
