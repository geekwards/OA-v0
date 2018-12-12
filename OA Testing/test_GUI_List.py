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
callindex = -1

def edit_item(list_window,idx):
    global editcalled
    global callindex

    editcalled = True
    callindex = idx

def remove_item(idx):
    global removecalled
    global callindex

    removecalled = True
    callindex = idx

class test_GUI_List(unittest.TestCase):

    def test_load_form(self):
        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        self.assertEqual(len(list_form.f1.winfo_children()),12)
        self.assertEqual((list_form.f1.winfo_children()[0].cget('text')),'Edit')
        self.assertEqual((list_form.f1.winfo_children()[11].cget('text')),'Remove')
        self.assertEqual((list_form.f1.winfo_children()[7].cget('text')),'Testing2 - TestDesc2')

    def test_load_form_close(self):
        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        GUI_List.close_click()
        self.assertFalse(list_window == None)

    def test_load_form_new(self):
        global editcalled
        global callindex

        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        editcalled = False
        callindex = -1

        GUI_List.new_click()
        self.assertTrue(editcalled)
        self.assertEqual(callindex,None)

    def test_load_form_edit1(self):
        global editcalled
        global callindex

        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        editcalled = False
        callindex = -1

        GUI_List.edit_click(1)
        self.assertTrue(editcalled)
        self.assertEqual(callindex,1)

    def test_load_form_edit2(self):
        global editcalled
        global callindex

        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        editcalled = False
        callindex = -1

        GUI_List.edit_click(2)
        self.assertTrue(editcalled)
        self.assertEqual(callindex,2)

    def test_load_form_remove1(self):
        global removecalled
        global callindex

        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        removecalled = False
        callindex = -1

        GUI_List.remove_click(1)
        self.assertTrue(removecalled)
        self.assertEqual(callindex,1)

    def test_load_form_remove1(self):
        global removecalled
        global callindex

        list_window,list_form = GUI_List.create_list_form(None)
        GUI_List.build_list("TESTING",test_set,edit_item,remove_item)

        removecalled = False
        callindex = -1

        GUI_List.remove_click(3)
        self.assertTrue(removecalled)
        self.assertEqual(callindex,3)

if __name__ == '__main__':
    unittest.main(verbosity=2)
