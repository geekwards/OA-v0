from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects'))

import GUI_List
import GUI_Archtype
import ArchType

def Editarchtype(idx):
    global mySet

    editRoot = Tk()

    GUI_Archtype.create_Toplevel1(editRoot)

    GUI_Archtype.loadForm(mySet[idx])

    editRoot.mainloop()

def ArchtypeList():
    global mySet

    root = Tk()

    GUI_List.create_Toplevel1(root)

    GUI_List.buildList("ArchTypes", mySet.GetList(), Editarchtype)

    root.mainloop()

if __name__ == '__main__':
    global mySet

    mySet = ArchType.Archtypes()
    mySet.AddNew(ArchType.Archtype("TestArch", "TestDesc"))
    mySet.AddNew(ArchType.Archtype("TestArch2", "TestDesc2"))

    ArchtypeList()
