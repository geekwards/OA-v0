from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))

import GUI_List
import ArchType

root = Tk()

mySet = ArchType.Archtypes()
mySet.AddNew(ArchType.Archtype("TestArch", "TestDesc"))
mySet.AddNew(ArchType.Archtype("TestArch2", "TestDesc2"))

GUI_List.create_Toplevel1(root)

GUI_List.buildList("ArchType", mySet.GetList())

root.mainloop()
