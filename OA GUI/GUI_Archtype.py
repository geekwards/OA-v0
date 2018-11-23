#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 23, 2018 07:59:19 AM EST  platform: Windows NT

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

import GUI_Archtype_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    GUI_Archtype_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    GUI_Archtype_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85' 
        _ana2color = '#d9d9d9' # X11 color: 'gray85' 
        font9 = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
            " -underline 0 -overstrike 0"

        top.geometry("600x711+404+111")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblTitle = tk.Label(top)
        self.lblTitle.place(relx=0.017, rely=0.014, height=43, width=577)
        self.lblTitle.configure(activebackground="#f9f9f9")
        self.lblTitle.configure(activeforeground="black")
        self.lblTitle.configure(background="#d9d9d9")
        self.lblTitle.configure(disabledforeground="#a3a3a3")
        self.lblTitle.configure(font=font9)
        self.lblTitle.configure(foreground="#000000")
        self.lblTitle.configure(highlightbackground="#d9d9d9")
        self.lblTitle.configure(highlightcolor="black")
        self.lblTitle.configure(text='''Archtype - <name>''')

        self.lblName = tk.Label(top)
        self.lblName.place(relx=0.033, rely=0.113, height=31, width=68)
        self.lblName.configure(activebackground="#f9f9f9")
        self.lblName.configure(activeforeground="black")
        self.lblName.configure(background="#d9d9d9")
        self.lblName.configure(disabledforeground="#a3a3a3")
        self.lblName.configure(foreground="#000000")
        self.lblName.configure(highlightbackground="#d9d9d9")
        self.lblName.configure(highlightcolor="black")
        self.lblName.configure(text='''Name''')

        self.roName = tk.Label(top)
        self.roName.place(relx=0.167, rely=0.12, height=25, width=200)
        self.roName.configure(activebackground="#f9f9f9")
        self.roName.configure(activeforeground="black")
        self.roName.configure(background="#d9d9d9")
        self.roName.configure(disabledforeground="#a3a3a3")
        self.roName.configure(foreground="#000000")
        self.roName.configure(highlightbackground="#d9d9d9")
        self.roName.configure(highlightcolor="black")
        self.roName.configure(text='''<name>''')

        self.rwName = tk.Entry(top)
        self.rwName.place(relx=0.167, rely=0.12,height=20, relwidth=0.333)
        self.rwName.configure(background="white")
        self.rwName.configure(disabledforeground="#a3a3a3")
        self.rwName.configure(font="TkFixedFont")
        self.rwName.configure(foreground="#000000")
        self.rwName.configure(highlightbackground="#d9d9d9")
        self.rwName.configure(highlightcolor="black")
        self.rwName.configure(insertbackground="black")
        self.rwName.configure(selectbackground="#c4c4c4")
        self.rwName.configure(selectforeground="black")

        self.lblProficiency = tk.Label(top)
        self.lblProficiency.place(relx=0.067, rely=0.183, height=21, width=65)
        self.lblProficiency.configure(activebackground="#f9f9f9")
        self.lblProficiency.configure(activeforeground="black")
        self.lblProficiency.configure(background="#d9d9d9")
        self.lblProficiency.configure(disabledforeground="#a3a3a3")
        self.lblProficiency.configure(foreground="#000000")
        self.lblProficiency.configure(highlightbackground="#d9d9d9")
        self.lblProficiency.configure(highlightcolor="black")
        self.lblProficiency.configure(text='''Proficiency''')

        self.roProficiency = tk.Label(top)
        self.roProficiency.place(relx=0.183, rely=0.183, height=21, width=34)
        self.roProficiency.configure(activebackground="#f9f9f9")
        self.roProficiency.configure(activeforeground="black")
        self.roProficiency.configure(background="#d9d9d9")
        self.roProficiency.configure(disabledforeground="#a3a3a3")
        self.roProficiency.configure(foreground="#000000")
        self.roProficiency.configure(highlightbackground="#d9d9d9")
        self.roProficiency.configure(highlightcolor="black")
        self.roProficiency.configure(text='''Label''')

        self.rwProficiency = tk.Entry(top)
        self.rwProficiency.place(relx=0.183, rely=0.183, height=20
                , relwidth=0.273)
        self.rwProficiency.configure(background="white")
        self.rwProficiency.configure(disabledforeground="#a3a3a3")
        self.rwProficiency.configure(font="TkFixedFont")
        self.rwProficiency.configure(foreground="#000000")
        self.rwProficiency.configure(highlightbackground="#d9d9d9")
        self.rwProficiency.configure(highlightcolor="black")
        self.rwProficiency.configure(insertbackground="black")
        self.rwProficiency.configure(selectbackground="#c4c4c4")
        self.rwProficiency.configure(selectforeground="black")

        self.lblDescription = tk.Label(top)
        self.lblDescription.place(relx=0.05, rely=0.239, height=21, width=66)
        self.lblDescription.configure(activebackground="#f9f9f9")
        self.lblDescription.configure(activeforeground="black")
        self.lblDescription.configure(background="#d9d9d9")
        self.lblDescription.configure(disabledforeground="#a3a3a3")
        self.lblDescription.configure(foreground="#000000")
        self.lblDescription.configure(highlightbackground="#d9d9d9")
        self.lblDescription.configure(highlightcolor="black")
        self.lblDescription.configure(text='''Description''')

        self.txtDescription = tk.Text(top)
        self.txtDescription.place(relx=0.183, rely=0.239, relheight=0.217
                , relwidth=0.557)
        self.txtDescription.configure(background="white")
        self.txtDescription.configure(font="TkTextFont")
        self.txtDescription.configure(foreground="black")
        self.txtDescription.configure(highlightbackground="#d9d9d9")
        self.txtDescription.configure(highlightcolor="black")
        self.txtDescription.configure(insertbackground="black")
        self.txtDescription.configure(selectbackground="#c4c4c4")
        self.txtDescription.configure(selectforeground="black")
        self.txtDescription.configure(width=334)
        self.txtDescription.configure(wrap='word')

        self.lblBonuses = tk.Label(top)
        self.lblBonuses.place(relx=0.067, rely=0.506, height=31, width=74)
        self.lblBonuses.configure(activebackground="#f9f9f9")
        self.lblBonuses.configure(activeforeground="black")
        self.lblBonuses.configure(background="#d9d9d9")
        self.lblBonuses.configure(disabledforeground="#a3a3a3")
        self.lblBonuses.configure(foreground="#000000")
        self.lblBonuses.configure(highlightbackground="#d9d9d9")
        self.lblBonuses.configure(highlightcolor="black")
        self.lblBonuses.configure(text='''Bonuses''')

        self.lblSTR = tk.Label(top)
        self.lblSTR.place(relx=0.05, rely=0.563, height=21, width=26)
        self.lblSTR.configure(activebackground="#f9f9f9")
        self.lblSTR.configure(activeforeground="black")
        self.lblSTR.configure(background="#d9d9d9")
        self.lblSTR.configure(disabledforeground="#a3a3a3")
        self.lblSTR.configure(foreground="#000000")
        self.lblSTR.configure(highlightbackground="#d9d9d9")
        self.lblSTR.configure(highlightcolor="black")
        self.lblSTR.configure(text='''STR''')

        self.roSTR = tk.Label(top)
        self.roSTR.place(relx=0.15, rely=0.563, height=21, width=34)
        self.roSTR.configure(activebackground="#f9f9f9")
        self.roSTR.configure(activeforeground="black")
        self.roSTR.configure(background="#d9d9d9")
        self.roSTR.configure(disabledforeground="#a3a3a3")
        self.roSTR.configure(foreground="#000000")
        self.roSTR.configure(highlightbackground="#d9d9d9")
        self.roSTR.configure(highlightcolor="black")
        self.roSTR.configure(text='''Label''')

        self.rwPER = tk.Entry(top)
        self.rwPER.place(relx=0.133, rely=0.605,height=20, relwidth=0.273)
        self.rwPER.configure(background="white")
        self.rwPER.configure(disabledforeground="#a3a3a3")
        self.rwPER.configure(font="TkFixedFont")
        self.rwPER.configure(foreground="#000000")
        self.rwPER.configure(highlightbackground="#d9d9d9")
        self.rwPER.configure(highlightcolor="black")
        self.rwPER.configure(insertbackground="black")
        self.rwPER.configure(selectbackground="#c4c4c4")
        self.rwPER.configure(selectforeground="black")

        self.lblPER = tk.Label(top)
        self.lblPER.place(relx=0.05, rely=0.605, height=21, width=26)
        self.lblPER.configure(activebackground="#f9f9f9")
        self.lblPER.configure(activeforeground="black")
        self.lblPER.configure(background="#d9d9d9")
        self.lblPER.configure(disabledforeground="#a3a3a3")
        self.lblPER.configure(foreground="#000000")
        self.lblPER.configure(highlightbackground="#d9d9d9")
        self.lblPER.configure(highlightcolor="black")
        self.lblPER.configure(text='''PER''')

        self.roPER = tk.Label(top)
        self.roPER.place(relx=0.15, rely=0.605, height=21, width=34)
        self.roPER.configure(activebackground="#f9f9f9")
        self.roPER.configure(activeforeground="black")
        self.roPER.configure(background="#d9d9d9")
        self.roPER.configure(disabledforeground="#a3a3a3")
        self.roPER.configure(foreground="#000000")
        self.roPER.configure(highlightbackground="#d9d9d9")
        self.roPER.configure(highlightcolor="black")
        self.roPER.configure(text='''Label''')

        self.rwINT = tk.Entry(top)
        self.rwINT.place(relx=0.133, rely=0.647,height=20, relwidth=0.273)
        self.rwINT.configure(background="white")
        self.rwINT.configure(disabledforeground="#a3a3a3")
        self.rwINT.configure(font="TkFixedFont")
        self.rwINT.configure(foreground="#000000")
        self.rwINT.configure(highlightbackground="#d9d9d9")
        self.rwINT.configure(highlightcolor="black")
        self.rwINT.configure(insertbackground="black")
        self.rwINT.configure(selectbackground="#c4c4c4")
        self.rwINT.configure(selectforeground="black")

        self.lblINT = tk.Label(top)
        self.lblINT.place(relx=0.05, rely=0.647, height=21, width=26)
        self.lblINT.configure(activebackground="#f9f9f9")
        self.lblINT.configure(activeforeground="black")
        self.lblINT.configure(background="#d9d9d9")
        self.lblINT.configure(disabledforeground="#a3a3a3")
        self.lblINT.configure(foreground="#000000")
        self.lblINT.configure(highlightbackground="#d9d9d9")
        self.lblINT.configure(highlightcolor="black")
        self.lblINT.configure(text='''INT''')

        self.roINT = tk.Label(top)
        self.roINT.place(relx=0.15, rely=0.647, height=21, width=34)
        self.roINT.configure(activebackground="#f9f9f9")
        self.roINT.configure(activeforeground="black")
        self.roINT.configure(background="#d9d9d9")
        self.roINT.configure(disabledforeground="#a3a3a3")
        self.roINT.configure(foreground="#000000")
        self.roINT.configure(highlightbackground="#d9d9d9")
        self.roINT.configure(highlightcolor="black")
        self.roINT.configure(text='''Label''')

        self.lblDEX = tk.Label(top)
        self.lblDEX.place(relx=0.05, rely=0.689, height=21, width=26)
        self.lblDEX.configure(activebackground="#f9f9f9")
        self.lblDEX.configure(activeforeground="black")
        self.lblDEX.configure(background="#d9d9d9")
        self.lblDEX.configure(disabledforeground="#a3a3a3")
        self.lblDEX.configure(foreground="#000000")
        self.lblDEX.configure(highlightbackground="#d9d9d9")
        self.lblDEX.configure(highlightcolor="black")
        self.lblDEX.configure(text='''DEX''')

        self.lblCHA = tk.Label(top)
        self.lblCHA.place(relx=0.05, rely=0.731, height=21, width=26)
        self.lblCHA.configure(activebackground="#f9f9f9")
        self.lblCHA.configure(activeforeground="black")
        self.lblCHA.configure(background="#d9d9d9")
        self.lblCHA.configure(disabledforeground="#a3a3a3")
        self.lblCHA.configure(foreground="#000000")
        self.lblCHA.configure(highlightbackground="#d9d9d9")
        self.lblCHA.configure(highlightcolor="black")
        self.lblCHA.configure(text='''CHA''')

        self.lblVIT = tk.Label(top)
        self.lblVIT.place(relx=0.05, rely=0.774, height=21, width=26)
        self.lblVIT.configure(activebackground="#f9f9f9")
        self.lblVIT.configure(activeforeground="black")
        self.lblVIT.configure(background="#d9d9d9")
        self.lblVIT.configure(disabledforeground="#a3a3a3")
        self.lblVIT.configure(foreground="#000000")
        self.lblVIT.configure(highlightbackground="#d9d9d9")
        self.lblVIT.configure(highlightcolor="black")
        self.lblVIT.configure(text='''VIT''')

        self.lblMAG = tk.Label(top)
        self.lblMAG.place(relx=0.05, rely=0.816, height=21, width=26)
        self.lblMAG.configure(activebackground="#f9f9f9")
        self.lblMAG.configure(activeforeground="black")
        self.lblMAG.configure(background="#d9d9d9")
        self.lblMAG.configure(disabledforeground="#a3a3a3")
        self.lblMAG.configure(foreground="#000000")
        self.lblMAG.configure(highlightbackground="#d9d9d9")
        self.lblMAG.configure(highlightcolor="black")
        self.lblMAG.configure(text='''MAG''')

        self.rwDEX = tk.Entry(top)
        self.rwDEX.place(relx=0.133, rely=0.689,height=20, relwidth=0.273)
        self.rwDEX.configure(background="white")
        self.rwDEX.configure(disabledforeground="#a3a3a3")
        self.rwDEX.configure(font="TkFixedFont")
        self.rwDEX.configure(foreground="#000000")
        self.rwDEX.configure(highlightbackground="#d9d9d9")
        self.rwDEX.configure(highlightcolor="black")
        self.rwDEX.configure(insertbackground="black")
        self.rwDEX.configure(selectbackground="#c4c4c4")
        self.rwDEX.configure(selectforeground="black")

        self.rwCHA = tk.Entry(top)
        self.rwCHA.place(relx=0.133, rely=0.731,height=20, relwidth=0.273)
        self.rwCHA.configure(background="white")
        self.rwCHA.configure(disabledforeground="#a3a3a3")
        self.rwCHA.configure(font="TkFixedFont")
        self.rwCHA.configure(foreground="#000000")
        self.rwCHA.configure(highlightbackground="#d9d9d9")
        self.rwCHA.configure(highlightcolor="black")
        self.rwCHA.configure(insertbackground="black")
        self.rwCHA.configure(selectbackground="#c4c4c4")
        self.rwCHA.configure(selectforeground="black")

        self.rwVIT = tk.Entry(top)
        self.rwVIT.place(relx=0.133, rely=0.774,height=20, relwidth=0.273)
        self.rwVIT.configure(background="white")
        self.rwVIT.configure(disabledforeground="#a3a3a3")
        self.rwVIT.configure(font="TkFixedFont")
        self.rwVIT.configure(foreground="#000000")
        self.rwVIT.configure(highlightbackground="#d9d9d9")
        self.rwVIT.configure(highlightcolor="black")
        self.rwVIT.configure(insertbackground="black")
        self.rwVIT.configure(selectbackground="#c4c4c4")
        self.rwVIT.configure(selectforeground="black")

        self.rwMAG = tk.Entry(top)
        self.rwMAG.place(relx=0.133, rely=0.816,height=20, relwidth=0.273)
        self.rwMAG.configure(background="white")
        self.rwMAG.configure(disabledforeground="#a3a3a3")
        self.rwMAG.configure(font="TkFixedFont")
        self.rwMAG.configure(foreground="#000000")
        self.rwMAG.configure(highlightbackground="#d9d9d9")
        self.rwMAG.configure(highlightcolor="black")
        self.rwMAG.configure(insertbackground="black")
        self.rwMAG.configure(selectbackground="#c4c4c4")
        self.rwMAG.configure(selectforeground="black")

        self.rwSTR = tk.Entry(top)
        self.rwSTR.place(relx=0.133, rely=0.563,height=20, relwidth=0.273)
        self.rwSTR.configure(background="white")
        self.rwSTR.configure(disabledforeground="#a3a3a3")
        self.rwSTR.configure(font="TkFixedFont")
        self.rwSTR.configure(foreground="#000000")
        self.rwSTR.configure(highlightbackground="#d9d9d9")
        self.rwSTR.configure(highlightcolor="black")
        self.rwSTR.configure(insertbackground="black")
        self.rwSTR.configure(selectbackground="#c4c4c4")
        self.rwSTR.configure(selectforeground="black")

        self.roPDEX = tk.Label(top)
        self.roPDEX.place(relx=0.15, rely=0.689, height=21, width=34)
        self.roPDEX.configure(activebackground="#f9f9f9")
        self.roPDEX.configure(activeforeground="black")
        self.roPDEX.configure(background="#d9d9d9")
        self.roPDEX.configure(disabledforeground="#a3a3a3")
        self.roPDEX.configure(foreground="#000000")
        self.roPDEX.configure(highlightbackground="#d9d9d9")
        self.roPDEX.configure(highlightcolor="black")
        self.roPDEX.configure(text='''Label''')

        self.roCHA = tk.Label(top)
        self.roCHA.place(relx=0.15, rely=0.731, height=21, width=34)
        self.roCHA.configure(activebackground="#f9f9f9")
        self.roCHA.configure(activeforeground="black")
        self.roCHA.configure(background="#d9d9d9")
        self.roCHA.configure(disabledforeground="#a3a3a3")
        self.roCHA.configure(foreground="#000000")
        self.roCHA.configure(highlightbackground="#d9d9d9")
        self.roCHA.configure(highlightcolor="black")
        self.roCHA.configure(text='''Label''')

        self.roVIT = tk.Label(top)
        self.roVIT.place(relx=0.15, rely=0.774, height=21, width=34)
        self.roVIT.configure(activebackground="#f9f9f9")
        self.roVIT.configure(activeforeground="black")
        self.roVIT.configure(background="#d9d9d9")
        self.roVIT.configure(disabledforeground="#a3a3a3")
        self.roVIT.configure(foreground="#000000")
        self.roVIT.configure(highlightbackground="#d9d9d9")
        self.roVIT.configure(highlightcolor="black")
        self.roVIT.configure(text='''Label''')

        self.roMAG = tk.Label(top)
        self.roMAG.place(relx=0.15, rely=0.816, height=21, width=34)
        self.roMAG.configure(activebackground="#f9f9f9")
        self.roMAG.configure(activeforeground="black")
        self.roMAG.configure(background="#d9d9d9")
        self.roMAG.configure(disabledforeground="#a3a3a3")
        self.roMAG.configure(foreground="#000000")
        self.roMAG.configure(highlightbackground="#d9d9d9")
        self.roMAG.configure(highlightcolor="black")
        self.roMAG.configure(text='''Label''')

        self.lblFeats = tk.Label(top)
        self.lblFeats.place(relx=0.483, rely=0.563, height=21, width=26)
        self.lblFeats.configure(activebackground="#f9f9f9")
        self.lblFeats.configure(activeforeground="black")
        self.lblFeats.configure(background="#d9d9d9")
        self.lblFeats.configure(disabledforeground="#a3a3a3")
        self.lblFeats.configure(foreground="#000000")
        self.lblFeats.configure(highlightbackground="#d9d9d9")
        self.lblFeats.configure(highlightcolor="black")
        self.lblFeats.configure(text='''Feats''')

        self.lblMvmt = tk.Label(top)
        self.lblMvmt.place(relx=0.467, rely=0.605, height=21, width=46)
        self.lblMvmt.configure(activebackground="#f9f9f9")
        self.lblMvmt.configure(activeforeground="black")
        self.lblMvmt.configure(background="#d9d9d9")
        self.lblMvmt.configure(disabledforeground="#a3a3a3")
        self.lblMvmt.configure(foreground="#000000")
        self.lblMvmt.configure(highlightbackground="#d9d9d9")
        self.lblMvmt.configure(highlightcolor="black")
        self.lblMvmt.configure(text='''Mvmt''')
        self.lblMvmt.configure(width=46)

        self.lblSkillPts = tk.Label(top)
        self.lblSkillPts.place(relx=0.467, rely=0.647, height=21, width=46)
        self.lblSkillPts.configure(activebackground="#f9f9f9")
        self.lblSkillPts.configure(activeforeground="black")
        self.lblSkillPts.configure(background="#d9d9d9")
        self.lblSkillPts.configure(disabledforeground="#a3a3a3")
        self.lblSkillPts.configure(foreground="#000000")
        self.lblSkillPts.configure(highlightbackground="#d9d9d9")
        self.lblSkillPts.configure(highlightcolor="black")
        self.lblSkillPts.configure(text='''Skill Pts''')
        self.lblSkillPts.configure(width=46)

        self.lblLvlHealth = tk.Label(top)
        self.lblLvlHealth.place(relx=0.45, rely=0.689, height=21, width=66)
        self.lblLvlHealth.configure(activebackground="#f9f9f9")
        self.lblLvlHealth.configure(activeforeground="black")
        self.lblLvlHealth.configure(background="#d9d9d9")
        self.lblLvlHealth.configure(disabledforeground="#a3a3a3")
        self.lblLvlHealth.configure(foreground="#000000")
        self.lblLvlHealth.configure(highlightbackground="#d9d9d9")
        self.lblLvlHealth.configure(highlightcolor="black")
        self.lblLvlHealth.configure(text='''Lvl Health''')
        self.lblLvlHealth.configure(width=66)

        self.rwFeats = tk.Entry(top)
        self.rwFeats.place(relx=0.567, rely=0.563,height=20, relwidth=0.273)
        self.rwFeats.configure(background="white")
        self.rwFeats.configure(disabledforeground="#a3a3a3")
        self.rwFeats.configure(font="TkFixedFont")
        self.rwFeats.configure(foreground="#000000")
        self.rwFeats.configure(highlightbackground="#d9d9d9")
        self.rwFeats.configure(highlightcolor="black")
        self.rwFeats.configure(insertbackground="black")
        self.rwFeats.configure(selectbackground="#c4c4c4")
        self.rwFeats.configure(selectforeground="black")

        self.rwMvmt = tk.Entry(top)
        self.rwMvmt.place(relx=0.567, rely=0.605,height=20, relwidth=0.273)
        self.rwMvmt.configure(background="white")
        self.rwMvmt.configure(disabledforeground="#a3a3a3")
        self.rwMvmt.configure(font="TkFixedFont")
        self.rwMvmt.configure(foreground="#000000")
        self.rwMvmt.configure(highlightbackground="#d9d9d9")
        self.rwMvmt.configure(highlightcolor="black")
        self.rwMvmt.configure(insertbackground="black")
        self.rwMvmt.configure(selectbackground="#c4c4c4")
        self.rwMvmt.configure(selectforeground="black")

        self.rwSkillPts = tk.Entry(top)
        self.rwSkillPts.place(relx=0.567, rely=0.647,height=20, relwidth=0.273)
        self.rwSkillPts.configure(background="white")
        self.rwSkillPts.configure(disabledforeground="#a3a3a3")
        self.rwSkillPts.configure(font="TkFixedFont")
        self.rwSkillPts.configure(foreground="#000000")
        self.rwSkillPts.configure(highlightbackground="#d9d9d9")
        self.rwSkillPts.configure(highlightcolor="black")
        self.rwSkillPts.configure(insertbackground="black")
        self.rwSkillPts.configure(selectbackground="#c4c4c4")
        self.rwSkillPts.configure(selectforeground="black")

        self.rwLvlHealth = tk.Entry(top)
        self.rwLvlHealth.place(relx=0.567, rely=0.689, height=20, relwidth=0.273)

        self.rwLvlHealth.configure(background="white")
        self.rwLvlHealth.configure(disabledforeground="#a3a3a3")
        self.rwLvlHealth.configure(font="TkFixedFont")
        self.rwLvlHealth.configure(foreground="#000000")
        self.rwLvlHealth.configure(highlightbackground="#d9d9d9")
        self.rwLvlHealth.configure(highlightcolor="black")
        self.rwLvlHealth.configure(insertbackground="black")
        self.rwLvlHealth.configure(selectbackground="#c4c4c4")
        self.rwLvlHealth.configure(selectforeground="black")

        self.roFeats = tk.Label(top)
        self.roFeats.place(relx=0.583, rely=0.563, height=21, width=34)
        self.roFeats.configure(activebackground="#f9f9f9")
        self.roFeats.configure(activeforeground="black")
        self.roFeats.configure(background="#d9d9d9")
        self.roFeats.configure(disabledforeground="#a3a3a3")
        self.roFeats.configure(foreground="#000000")
        self.roFeats.configure(highlightbackground="#d9d9d9")
        self.roFeats.configure(highlightcolor="black")
        self.roFeats.configure(text='''Label''')

        self.roMvmt = tk.Label(top)
        self.roMvmt.place(relx=0.583, rely=0.605, height=21, width=34)
        self.roMvmt.configure(activebackground="#f9f9f9")
        self.roMvmt.configure(activeforeground="black")
        self.roMvmt.configure(background="#d9d9d9")
        self.roMvmt.configure(disabledforeground="#a3a3a3")
        self.roMvmt.configure(foreground="#000000")
        self.roMvmt.configure(highlightbackground="#d9d9d9")
        self.roMvmt.configure(highlightcolor="black")
        self.roMvmt.configure(text='''Label''')

        self.roSkillPts = tk.Label(top)
        self.roSkillPts.place(relx=0.583, rely=0.647, height=21, width=34)
        self.roSkillPts.configure(activebackground="#f9f9f9")
        self.roSkillPts.configure(activeforeground="black")
        self.roSkillPts.configure(background="#d9d9d9")
        self.roSkillPts.configure(disabledforeground="#a3a3a3")
        self.roSkillPts.configure(foreground="#000000")
        self.roSkillPts.configure(highlightbackground="#d9d9d9")
        self.roSkillPts.configure(highlightcolor="black")
        self.roSkillPts.configure(text='''Label''')

        self.roLvlHealth = tk.Label(top)
        self.roLvlHealth.place(relx=0.583, rely=0.689, height=21, width=34)
        self.roLvlHealth.configure(activebackground="#f9f9f9")
        self.roLvlHealth.configure(activeforeground="black")
        self.roLvlHealth.configure(background="#d9d9d9")
        self.roLvlHealth.configure(disabledforeground="#a3a3a3")
        self.roLvlHealth.configure(foreground="#000000")
        self.roLvlHealth.configure(highlightbackground="#d9d9d9")
        self.roLvlHealth.configure(highlightcolor="black")
        self.roLvlHealth.configure(text='''Label''')

        self.lblStamina = tk.Label(top)
        self.lblStamina.place(relx=0.45, rely=0.731, height=21, width=66)
        self.lblStamina.configure(activebackground="#f9f9f9")
        self.lblStamina.configure(activeforeground="black")
        self.lblStamina.configure(background="#d9d9d9")
        self.lblStamina.configure(disabledforeground="#a3a3a3")
        self.lblStamina.configure(foreground="#000000")
        self.lblStamina.configure(highlightbackground="#d9d9d9")
        self.lblStamina.configure(highlightcolor="black")
        self.lblStamina.configure(text='''Stamina''')

        self.rwStamina = tk.Entry(top)
        self.rwStamina.place(relx=0.567, rely=0.731,height=20, relwidth=0.273)
        self.rwStamina.configure(background="white")
        self.rwStamina.configure(disabledforeground="#a3a3a3")
        self.rwStamina.configure(font="TkFixedFont")
        self.rwStamina.configure(foreground="#000000")
        self.rwStamina.configure(highlightbackground="#d9d9d9")
        self.rwStamina.configure(highlightcolor="black")
        self.rwStamina.configure(insertbackground="black")
        self.rwStamina.configure(selectbackground="#c4c4c4")
        self.rwStamina.configure(selectforeground="black")

        self.roStamina = tk.Label(top)
        self.roStamina.place(relx=0.583, rely=0.731, height=21, width=34)
        self.roStamina.configure(activebackground="#f9f9f9")
        self.roStamina.configure(activeforeground="black")
        self.roStamina.configure(background="#d9d9d9")
        self.roStamina.configure(disabledforeground="#a3a3a3")
        self.roStamina.configure(foreground="#000000")
        self.roStamina.configure(highlightbackground="#d9d9d9")
        self.roStamina.configure(highlightcolor="black")
        self.roStamina.configure(text='''Label''')

        self.lblAttack = tk.Label(top)
        self.lblAttack.place(relx=0.45, rely=0.774, height=21, width=66)
        self.lblAttack.configure(activebackground="#f9f9f9")
        self.lblAttack.configure(activeforeground="black")
        self.lblAttack.configure(background="#d9d9d9")
        self.lblAttack.configure(disabledforeground="#a3a3a3")
        self.lblAttack.configure(foreground="#000000")
        self.lblAttack.configure(highlightbackground="#d9d9d9")
        self.lblAttack.configure(highlightcolor="black")
        self.lblAttack.configure(text='''Attack''')

        self.lblReflex = tk.Label(top)
        self.lblReflex.place(relx=0.45, rely=0.816, height=21, width=66)
        self.lblReflex.configure(activebackground="#f9f9f9")
        self.lblReflex.configure(activeforeground="black")
        self.lblReflex.configure(background="#d9d9d9")
        self.lblReflex.configure(disabledforeground="#a3a3a3")
        self.lblReflex.configure(foreground="#000000")
        self.lblReflex.configure(highlightbackground="#d9d9d9")
        self.lblReflex.configure(highlightcolor="black")
        self.lblReflex.configure(text='''Reflex''')

        self.rwAttack = tk.Entry(top)
        self.rwAttack.place(relx=0.567, rely=0.774,height=20, relwidth=0.273)
        self.rwAttack.configure(background="white")
        self.rwAttack.configure(disabledforeground="#a3a3a3")
        self.rwAttack.configure(font="TkFixedFont")
        self.rwAttack.configure(foreground="#000000")
        self.rwAttack.configure(highlightbackground="#d9d9d9")
        self.rwAttack.configure(highlightcolor="black")
        self.rwAttack.configure(insertbackground="black")
        self.rwAttack.configure(selectbackground="#c4c4c4")
        self.rwAttack.configure(selectforeground="black")

        self.rwReflex = tk.Entry(top)
        self.rwReflex.place(relx=0.567, rely=0.816,height=20, relwidth=0.273)
        self.rwReflex.configure(background="white")
        self.rwReflex.configure(disabledforeground="#a3a3a3")
        self.rwReflex.configure(font="TkFixedFont")
        self.rwReflex.configure(foreground="#000000")
        self.rwReflex.configure(highlightbackground="#d9d9d9")
        self.rwReflex.configure(highlightcolor="black")
        self.rwReflex.configure(insertbackground="black")
        self.rwReflex.configure(selectbackground="#c4c4c4")
        self.rwReflex.configure(selectforeground="black")

        self.roAttack = tk.Label(top)
        self.roAttack.place(relx=0.583, rely=0.774, height=21, width=34)
        self.roAttack.configure(activebackground="#f9f9f9")
        self.roAttack.configure(activeforeground="black")
        self.roAttack.configure(background="#d9d9d9")
        self.roAttack.configure(disabledforeground="#a3a3a3")
        self.roAttack.configure(foreground="#000000")
        self.roAttack.configure(highlightbackground="#d9d9d9")
        self.roAttack.configure(highlightcolor="black")
        self.roAttack.configure(text='''Label''')

        self.roReflex = tk.Label(top)
        self.roReflex.place(relx=0.583, rely=0.816, height=21, width=34)
        self.roReflex.configure(activebackground="#f9f9f9")
        self.roReflex.configure(activeforeground="black")
        self.roReflex.configure(background="#d9d9d9")
        self.roReflex.configure(disabledforeground="#a3a3a3")
        self.roReflex.configure(foreground="#000000")
        self.roReflex.configure(highlightbackground="#d9d9d9")
        self.roReflex.configure(highlightcolor="black")
        self.roReflex.configure(text='''Label''')

        self.Close = tk.Button(top)
        self.Close.place(relx=0.05, rely=0.886, height=64, width=127)
        self.Close.configure(activebackground="#d9d9d9")
        self.Close.configure(activeforeground="#000000")
        self.Close.configure(background="#d9d9d9")
        self.Close.configure(disabledforeground="#a3a3a3")
        self.Close.configure(foreground="#000000")
        self.Close.configure(highlightbackground="#d9d9d9")
        self.Close.configure(highlightcolor="black")
        self.Close.configure(pady="0")
        self.Close.configure(text='''Close''')
        self.Close.configure(width=127)

        self.Save = tk.Button(top)
        self.Save.place(relx=0.65, rely=0.886, height=64, width=127)
        self.Save.configure(activebackground="#d9d9d9")
        self.Save.configure(activeforeground="#000000")
        self.Save.configure(background="#d9d9d9")
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#d9d9d9")
        self.Save.configure(highlightcolor="black")
        self.Save.configure(pady="0")
        self.Save.configure(text='''Save''')

if __name__ == '__main__':
    vp_start_gui()





