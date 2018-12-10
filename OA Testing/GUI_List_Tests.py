import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_List
import List_Object

test_list_item0 = List_Object.Listobject('Testing0','TestDesc0')
test_list_item1 = List_Object.Listobject('Testing1','TestDesc1')
test_list_item2 = List_Object.Listobject('Testing2','TestDesc2')
test_list_item3 = List_Object.Listobject('Testing3','TestDesc3')

test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

editcalled = False
removecalled = False

def edit_item():
    editcalled = True

def remove_item():
    removecalled = True

class GUI_List_Tests(unittest.TestCase):

    def test_load_form(self):
        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        self.assertEqual(len(list_form.f1.winfo_children()),12)
        self.assertEqual((list_form.f1.winfo_children()[0].cget('text')),'Edit')
        self.assertEqual((list_form.f1.winfo_children()[11].cget('text')),'Remove')
        self.assertEqual((list_form.f1.winfo_children()[7].cget('text')),'Testing2 - TestDesc2')

    #
    # def test_load_form_close(self):
    #     test_archtype = Archtype.Archtype('Testing','TestDesc')
    #
    #     archtype_window, archtype_form = GUI_Archtype.create_archtype_form(None)
    #     GUI_Archtype.load_data(test_archtype, save_archtype, 0)
    #     GUI_Archtype.close_click()
    #     self.assertFalse(archtype_window == None)
    #


if __name__ == '__main__':
    unittest.main(verbosity=2)
