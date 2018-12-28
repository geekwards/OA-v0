import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_List_Controller
import List_Object

test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

listsaved = False
listremoved = False
listedit = False
listnew = False
listclose = False
listcancel = False
call_name = ''
index = 0

def save_list():
    global listsaved

    listsaved = True

def edit_list(list_window,name):
    global listedit
    global call_name

    listedit = True
    call_name = name

def remove_list(list_item):
    global listremoved
    global call_name

    listremoved = True
    call_name = list_item.name

def new_list():
    global listnew

    listnew = True

def close_list():
    global listclose

    listclose = True

def cancel_list():
    global listcancel

    listcancel = True

class test_GUI_List_Controller(unittest.TestCase):
    def test_list_controller_create_form(self):
        list_controller = GUI_List_Controller.GUI_list_controller()
        self.assertNotEqual(list_controller.get_list_form(),None)

    def test_list_controller_load(self):
        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        self.assertEqual(list_controller.get_current_list(),test_set)

    def test_list_controller_refresh(self):
        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        list_form = list_controller.get_list_form()
        self.assertEqual(len(list_form.f1.winfo_children()),12) 

        list_controller.get_current_list().append(List_Object.List_object('testingmore',''))
        list_controller.refresh_data()
        self.assertEqual(len(list_form.f1.winfo_children()),15)

    def test_list_controller_new(self):
        global edit_list
        global call_name

        test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
        test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
        test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
        test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

        test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        self.assertEqual(list_controller.get_current_list()[1].name,'Testing1')
        self.assertEqual(len(list_controller.get_current_list()),4)        

        list_controller.edit_click(None)

        self.assertTrue(edit_list)
        self.assertEqual(call_name,'')  

    def test_list_controller_close(self):
        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        self.assertNotEqual(list_controller.get_list_form(),None)

        list_controller.close_click()
        self.assertEqual(list_controller.get_list_form(),None)

    def test_list_controller_edit(self):
        global edit_list
        global call_name

        test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
        test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
        test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
        test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

        test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        self.assertEqual(list_controller.get_current_list()[1].name,'Testing1')
        self.assertEqual(len(list_controller.get_current_list()),4)        

        list_controller.edit_click(1)

        self.assertTrue(edit_list)
        self.assertEqual(call_name,'Testing1')    

    def test_list_controller_remove(self):
        global remove_list
        global call_name

        test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
        test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
        test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
        test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

        test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

        list_controller = GUI_List_Controller.GUI_list_controller()
        list_controller.load_data('list_title',test_set,edit_list,remove_list,close_list,True)
        self.assertEqual(list_controller.get_current_list()[1].name,'Testing1')
        self.assertEqual(len(list_controller.get_current_list()),4)        

        list_controller.remove_click(1)

        self.assertTrue(remove_list)
        self.assertEqual(call_name,'Testing1')        

if __name__ == '__main__':
    unittest.main(verbosity=2)
