import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype
import Archtype

class GUI_Archtype_Tests(unittest.TestCase):

    def test_load_form(self):
        test_archtype = Archtype.Archtype('Testing','TestDesc')

        edit_window, top = GUI_Archtype.create_toplevel1(top)

        GUI_Archtype.load_form(current_set[idx], save_archtype, idx)

        print edit_window.f1.ename.get()


if __name__ == '__main__':
    unittest.main(verbosity=2)
