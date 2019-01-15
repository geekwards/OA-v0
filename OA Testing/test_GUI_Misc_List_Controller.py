import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List_Controller
import List_Object
import Misc_List
import test__data

new_called = False
edit_called = False
save_called = False
close_called = False
cancel_called = False
remove_called = False
call_name = ''
index = 0

def new_call():
    global new_called
    new_called = True

def save_call(arg):
    global save_called
    save_called = True

def edit_call(list_window,name):
    global edit_called
    global call_name
    edit_called = True
    call_name = name

def close_call():
    global close_called
    close_called = True

def cancel_call():
    global cancel_called
    cancel_called = True

def remove_call(list_item):
    global remove_called
    remove_called = True

class test_GUI_Misc_List_Controller(unittest.TestCase):
    def test_misc_controller_create_form(self):
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        self.assertNotEqual(misc_controller.get_form(),None)

    def test_misc_controller_load(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        self.assertEqual(misc_controller.get_current_set(),test_misc_list)

    def test_misc_controller_new(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        misc_form = misc_controller.get_form()
        misc_controller.new_call()
        self.assertEqual(len(misc_form.f1.winfo_children()),8)

    def test_misc_controller_close(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        self.assertNotEqual(misc_controller.get_form(),None)
        misc_controller.close_call()
        self.assertEqual(misc_controller.get_form(),None)
 
    def test_misc_controller_edit(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        misc_form = misc_controller.get_form()
        self.assertEqual(len(misc_form.f1.winfo_children()),6)
        misc_controller.edit_call()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_controller_save(self):
        global save_called
        save_called = False
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        misc_controller.save_call()
        self.assertTrue(save_called)

    def test_misc_controller_cancel(self):
        item1 = List_Object.List_object('Testlist 1.1','desc 1.1')
        item2 = List_Object.List_object('Testlist 1.2','desc 1.2')
        item3 = List_Object.List_object('Testlist 1.3','desc 1.3')
        test_misc_list = Misc_List.Misc_list('Test1','',[item1,item2,item3])
        misc_controller = GUI_Misc_List_Controller.GUI_misc_list_controller()
        misc_controller.load_data(test_misc_list,save_call,close_call,True)
        misc_form = misc_controller.get_form()
        misc_controller.cancel_call()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
