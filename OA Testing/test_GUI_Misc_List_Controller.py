import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__gui_misc_list_controller
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

def edit_call(name,list_window):
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
    def test_misclist_controller_create(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        self.assertNotEqual(misclist_controller.get_form(),None)

    def test_misclist_controller_load(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        misclist_controller.load_data(test__data.test_misclist1,save_call,close_call)
        self.assertEqual(misclist_controller.get_current_set(),test__data.test_misclist1)

    def test_misclist_controller_refresh(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        clone = test__data.test_misclist1.clone()
        clone.all_items[0].short_description = 'test prof'
        misclist_controller.create_form()
        misclist_controller.load_data(clone,save_call,close_call)
        misclist_form = misclist_controller.get_form()
        self.assertEqual(misclist_form.f1.winfo_children()[1].get('1.0','end-1c'),'test prof')
        clone = test__data.test_misclist1.clone()
        clone.all_items[0].short_description = 'MODIFIED PROF'
        misclist_controller.load_data(clone,save_call,close_call)
        self.assertEqual(misclist_controller.get_current_set(),clone)

    def test_misclist_controller_close(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        misclist_controller.load_data(test__data.test_misclist1,save_call,close_call)
        self.assertNotEqual(misclist_controller.get_form(),None)
        misclist_controller.close_call()
        self.assertEqual(misclist_controller.get_form(),None)

    def test_load_form_edit(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        misclist_controller.load_data(test__data.test_misclist1,save_call,close_call)
        misclist_form = misclist_controller.get_form()
        misclist_controller.edit_call()
        for item in misclist_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        misclist_controller.load_data(test__data.test_misclist1,save_call,close_call)
        misclist_form = misclist_controller.get_form()
        misclist_controller.cancel_call()
        for item in misclist_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global save_called
        save_called = False
        misclist_controller = test__gui_misc_list_controller.GUI_controller()
        misclist_controller.create_form()
        misclist_controller.load_data(test__data.test_misclist1,save_call,close_call)
        misclist_controller.save_call()
        self.assertTrue(save_called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
