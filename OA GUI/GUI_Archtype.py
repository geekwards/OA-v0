#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.18
#  in conjunction with Tcl version 8.6
#    Nov 24, 2018 09:36:38 PM EST  platform: Windows NT

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

import GUI_List_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    GUI_List_support.set_Tk_var()
    top = Toplevel1 (root)
    GUI_List_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    GUI_List_support.set_Tk_var()
    top = Toplevel1 (w)
    GUI_List_support.init(w, top, *args, **kwargs)
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

        top.geometry("543x616+407+109")
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.lblTitle = tk.Label(top)
        self.lblTitle.place(relx=0.018, rely=0.032, height=51, width=514)
        self.lblTitle.configure(activebackground="#f9f9f9")
        self.lblTitle.configure(activeforeground="black")
        self.lblTitle.configure(background="#d9d9d9")
        self.lblTitle.configure(disabledforeground="#a3a3a3")
        self.lblTitle.configure(font=font9)
        self.lblTitle.configure(foreground="#000000")
        self.lblTitle.configure(highlightbackground="#d9d9d9")
        self.lblTitle.configure(highlightcolor="black")
        self.lblTitle.configure(text='''List Title''')

        self.lblListItem = tk.Label(top)
        self.lblListItem.place(relx=0.018, rely=0.179, height=30, width=400)
        self.lblListItem.configure(activebackground="#f9f9f9")
        self.lblListItem.configure(activeforeground="black")
        self.lblListItem.configure(background="#d9d9d9")
        self.lblListItem.configure(disabledforeground="#a3a3a3")
        self.lblListItem.configure(foreground="#000000")
        self.lblListItem.configure(highlightbackground="#d9d9d9")
        self.lblListItem.configure(highlightcolor="black")
        self.lblListItem.configure(justify='left')
        self.lblListItem.configure(text='''List Item''')

        self.EditListItem = tk.Button(top)
        self.EditListItem.place(relx=0.773, rely=0.187, height=25, width=50)
        self.EditListItem.configure(activebackground="#d9d9d9")
        self.EditListItem.configure(activeforeground="#000000")
        self.EditListItem.configure(background="#d9d9d9")
        self.EditListItem.configure(disabledforeground="#a3a3a3")
        self.EditListItem.configure(foreground="#000000")
        self.EditListItem.configure(highlightbackground="#d9d9d9")
        self.EditListItem.configure(highlightcolor="black")
        self.EditListItem.configure(pady="0")
        self.EditListItem.configure(text='''Edit''')

        self.RemoveListItem = tk.Button(top)
        self.RemoveListItem.place(relx=0.866, rely=0.187, height=25, width=50)
        self.RemoveListItem.configure(activebackground="#d9d9d9")
        self.RemoveListItem.configure(activeforeground="#000000")
        self.RemoveListItem.configure(background="#d9d9d9")
        self.RemoveListItem.configure(disabledforeground="#a3a3a3")
        self.RemoveListItem.configure(foreground="#000000")
        self.RemoveListItem.configure(highlightbackground="#d9d9d9")
        self.RemoveListItem.configure(highlightcolor="black")
        self.RemoveListItem.configure(pady="0")
        self.RemoveListItem.configure(text='''Remove''')

        self.chkListItem = tk.Checkbutton(top)
        self.chkListItem.place(relx=0.018, rely=0.179, relheight=0.049
                , relwidth=0.737)
        self.chkListItem.configure(activebackground="#d9d9d9")
        self.chkListItem.configure(activeforeground="#000000")
        self.chkListItem.configure(background="#d9d9d9")
        self.chkListItem.configure(disabledforeground="#a3a3a3")
        self.chkListItem.configure(foreground="#000000")
        self.chkListItem.configure(highlightbackground="#d9d9d9")
        self.chkListItem.configure(highlightcolor="black")
        self.chkListItem.configure(justify='left')
        self.chkListItem.configure(text='''Check''')
        self.chkListItem.configure(variable=GUI_List_support.che47)

        self.Return = tk.Button(top)
        self.Return.place(relx=0.755, rely=0.893, height=64, width=107)
        self.Return.configure(activebackground="#d9d9d9")
        self.Return.configure(activeforeground="#000000")
        self.Return.configure(background="#d9d9d9")
        self.Return.configure(disabledforeground="#a3a3a3")
        self.Return.configure(foreground="#000000")
        self.Return.configure(highlightbackground="#d9d9d9")
        self.Return.configure(highlightcolor="black")
        self.Return.configure(pady="0")
        self.Return.configure(text='''Return''')

        self.Cancel = tk.Button(top)
        self.Cancel.place(relx=0.018, rely=0.893, height=64, width=107)
        self.Cancel.configure(activebackground="#d9d9d9")
        self.Cancel.configure(activeforeground="#000000")
        self.Cancel.configure(background="#d9d9d9")
        self.Cancel.configure(command=GUI_List_support.btnCancel_Click)
        self.Cancel.configure(disabledforeground="#a3a3a3")
        self.Cancel.configure(foreground="#000000")
        self.Cancel.configure(highlightbackground="#d9d9d9")
        self.Cancel.configure(highlightcolor="black")
        self.Cancel.configure(pady="0")
        self.Cancel.configure(text='''Cancel''')

        self.Save = tk.Button(top)
        self.Save.place(relx=0.516, rely=0.893, height=64, width=107)
        self.Save.configure(activebackground="#d9d9d9")
        self.Save.configure(activeforeground="#000000")
        self.Save.configure(background="#d9d9d9")
        self.Save.configure(disabledforeground="#a3a3a3")
        self.Save.configure(foreground="#000000")
        self.Save.configure(highlightbackground="#d9d9d9")
        self.Save.configure(highlightcolor="black")
        self.Save.configure(pady="0")
        self.Save.configure(text='''Save''')

        self.CopyList = tk.Button(top)
        self.CopyList.place(relx=0.239, rely=0.893, height=64, width=107)
        self.CopyList.configure(activebackground="#d9d9d9")
        self.CopyList.configure(activeforeground="#000000")
        self.CopyList.configure(background="#d9d9d9")
        self.CopyList.configure(disabledforeground="#a3a3a3")
        self.CopyList.configure(foreground="#000000")
        self.CopyList.configure(highlightbackground="#d9d9d9")
        self.CopyList.configure(highlightcolor="black")
        self.CopyList.configure(pady="0")
        self.CopyList.configure(text='''Copy List''')

        self.AddListItem = tk.Button(top)
        self.AddListItem.place(relx=0.018, rely=0.244, height=25, width=50)
        self.AddListItem.configure(activebackground="#d9d9d9")
        self.AddListItem.configure(activeforeground="#000000")
        self.AddListItem.configure(background="#d9d9d9")
        self.AddListItem.configure(disabledforeground="#a3a3a3")
        self.AddListItem.configure(foreground="#000000")
        self.AddListItem.configure(highlightbackground="#d9d9d9")
        self.AddListItem.configure(highlightcolor="black")
        self.AddListItem.configure(pady="0")
        self.AddListItem.configure(text='''Add''')

if __name__ == '__main__':
    vp_start_gui()





