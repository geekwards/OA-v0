import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Focus_Controller
import Archtype
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

class test_GUI_Focus(unittest.TestCase):
    def test_focus_controller_create(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        self.assertNotEqual(focus_controller.get_form(),None)

    def test_archtype_controller_load(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        self.assertEqual(focus_controller.get_current_set(),test__data.test_focus1)

    def test_archtype_controller_refresh(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        test__data.test_focus1.short_description = 'test prof'
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        focus_form = focus_controller.get_form()
        self.assertEqual(focus_form.f1.eshortdescr.get(),'test prof')
        clone = test__data.test_focus1.clone()
        clone.short_description = 'MODIFIED PROF'
        focus_controller.load_data(clone,save_call,close_call)
        self.assertEqual(focus_controller.get_current_set(),clone)

    def test_archtype_controller_close(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        self.assertNotEqual(focus_controller.get_form(),None)
        focus_controller.close_call()
        self.assertEqual(focus_controller.get_form(),None)

    def test_load_form_edit(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        focus_form = focus_controller.get_form()
        focus_controller.edit_call()
        for item in focus_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        focus_form = focus_controller.get_form()
        focus_controller.cancel_call()
        for item in focus_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global save_called
        save_called = False
        focus_controller = GUI_Focus_Controller.GUI_focus_controller()
        focus_controller.load_data(test__data.test_focus1,save_call,close_call)
        focus_controller.save_call()
        self.assertTrue(save_called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
