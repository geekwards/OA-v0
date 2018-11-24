from Tkinter import *

import sys, os.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI'))

root = Tk()
w = Label(root, text=sys.path)
w.pack()
root.mainloop()
