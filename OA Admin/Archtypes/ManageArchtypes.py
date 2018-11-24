from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))

import GUI_List

root = Tk()

GUI_List.create_Toplevel1(root)

GUI_List.buildList("test")

root.mainloop()
