import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__gui_list_controller
import List_Object
import test__data

new_called = False
edit_called = False
save_called = False
close_called = False
cancel_called = False
remove_called = False
call_item = ''
index = 0

def new_call():
    global new_called
    new_called = True

def save_call():
    global save_called
    save_called = True

def edit_call(name,list_window):
    global edit_called
    global call_item
    edit_called = True
    call_item = name

def close_call():
    global close_called
    close_called = True

def cancel_call():
    global cancel_called
    cancel_called = True

def remove_call(list_item):
    global remove_called
    global call_item
    remove_called = True
    call_item = list_item

class test_GUI_List_Controller(unittest.TestCase):
    def test_list_controller_create(self):
        list_controller = test__gui_list_controller.GUI_controller()
        list_controller.create_form()
        self.assertNotEqual(list_controller.get_form(),None)

    def test_list_controller_load(self):
        list_controller = test__gui_list_controller.GUI_controller()
        list_controller.create_form()
        list_controller.load_data('TEST',test__data.test_set1,edit_call,remove_call,close_call)
        self.assertEqual(list_controller.get_current_set(),test__data.test_set1)

    def test_list_controller_close(self):
        list_controller = test__gui_list_controller.GUI_controller()
        list_controller.create_form()
        list_controller.load_data('TEST',test__data.test_set1,edit_call,remove_call,close_call)
        self.assertNotEqual(list_controller.get_form(),None)
        list_controller.close_call()
        self.assertEqual(list_controller.get_form(),None)

    def test_load_form_edit(self):
        list_controller = test__gui_list_controller.GUI_controller()
        list_controller.create_form()
        list_controller.load_data('TEST',test__data.test_set1,edit_call,remove_call,close_call)
        list_form = list_controller.get_form()
        list_controller.edit_call(1)
        for item in list_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_remove(self):
        list_controller = test__gui_list_controller.GUI_controller()
        list_controller.create_form()
        list_controller.load_data('TEST',test__data.test_set1,edit_call,remove_call,close_call)
        self.remove_called = False
        list_controller.remove_call(1)
        self.assertTrue(remove_called)
        self.assertEqual(call_item.name,'test2')

if __name__ == '__main__':
    unittest.main(verbosity=2)
