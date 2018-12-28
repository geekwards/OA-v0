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
test_misc_list = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

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
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        self.assertEqual(misc_controller.get_current_misc_list(),test_misc_list)

    def test_misc_controller_refresh(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        self.assertEqual(len(misc_form.f1.winfo_children()),3) 

        misc_controller.get_current_misc_list().add_new('testingmore')
        misc_controller.refresh_data()
        self.assertEqual(len(misc_form.f1.winfo_children()),4)

    def test_misc_controller_new(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()

        misc_controller.new_click()
        self.assertEqual(len(misc_form.f1.winfo_children()),4)

    def test_misc_controller_close(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        self.assertNotEqual(misc_controller.get_misc_list_form(),None)

        misc_controller.close_click()
        self.assertEqual(misc_controller.get_misc_list_form(),None)

    def test_misc_controller_edit(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        self.assertEqual(len(misc_form.f1.winfo_children()),3)

        misc_controller.edit_click()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_controller_save(self):
        global listsaved
    
        listsaved = False

        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_controller.save_click()
        self.assertTrue(listsaved)

    def test_misc_controller_cancel(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_misc_list,close_misc_list,True)
        misc_form = misc_controller.get_misc_list_form()
        misc_controller.cancel_click()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
