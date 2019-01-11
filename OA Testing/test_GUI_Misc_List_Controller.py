import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List_Controller
import List_Object
import Misc_List

listsaved = False
listremoved = False
listedit = False
listnew = False
listclose = False
listcancel = False
index = 0

def save_misc_list(misc_list):
    global listsaved

    listsaved = True

def edit_misc_list(idx):
    global listedit
    global index

    listedit = True
    index = idx

def remove_misc_list(idx):
    global listremoved
    global index

    listremoved = True
    index = idx

def new_misc_list():
    global listnew

    listnew = True

def close_misc_list():
    global listclose

    listclose = True

def cancel_misc_list():
    global listcancel

    listcancel = True

class test_GUI_Misc_List_Controller(unittest.TestCase):

    def test_misc_controller_create_form(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        self.assertNotEqual(misc_controller.get_misc_list_form(),None)

    def test_misc_controller_load(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        self.assertEqual(misc_controller.get_current_misc_list(),test_misc_list)

    def test_misc_controller_refresh(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        self.assertEqual(len(misc_form.f1.winfo_children()),6) 

        misc_controller.get_current_misc_list().add_new(List_Object.List_object('testingmore',''))
        misc_controller.refresh_data()
        self.assertEqual(len(misc_form.f1.winfo_children()),8)

    def test_misc_controller_new(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()

        misc_controller.new_click()
        self.assertEqual(len(misc_form.f1.winfo_children()),8)

    def test_misc_controller_close(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        self.assertNotEqual(misc_controller.get_misc_list_form(),None)

        misc_controller.close_click()
        self.assertEqual(misc_controller.get_misc_list_form(),None)
 
    def test_misc_controller_edit(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        self.assertEqual(len(misc_form.f1.winfo_children()),6)

        misc_controller.edit_click()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_controller_save(self):
        global listsaved
    
        listsaved = False
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_controller.save_click()
        self.assertTrue(listsaved)

    def test_misc_controller_cancel(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        misc_controller.cancel_click()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
