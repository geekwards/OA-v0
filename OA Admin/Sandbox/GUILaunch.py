from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))

import GUI_List

import ArchType

root = Tk()

GUI_List.create_Toplevel1(root)

tmpArchtypes = ArchType.Archtypes()
tmpArchtypes.AddNew("NewArchtype")

GUI_List.buildList("test")

root.mainloop()
