import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Focus_Form
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

def save_call(arg):
    global save_called
    global call_item
    save_called = True
    call_item = arg

def edit_call(name,list_window):
    global edit_called
    global call_item
    edit_called = True
    call_item = arg

def close_call():
    global close_called
    close_called = True

def cancel_call():
    global cancel_called
    cancel_called = True

def remove_call(arg):
    global remove_called
    global call_item
    remove_called = True
    call_item = arg

def list_call(arg):
    global list_called
    global call_item
    list_called = True
    call_item = arg

class test_GUI_Focus_Form(unittest.TestCase):
    def test_focus_create(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        self.assertNotEqual(focus_form,None)

    def test_focus_form_setup(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        self.assertEqual(focus_form.lbltitle.cget('text'),'Focus - test1')

    def test_focus_form_set_edit(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        focus_form.set_edit()
        self.assertEqual(focus_form.left_button.cget('text'),'Cancel')

    def test_focus_form_set_view(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        focus_form.set_view()
        self.assertEqual(focus_form.left_button.cget('text'),'Close')

    def test_focus_form_add_item(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        self.assertEqual(focus_form.f1.ename.get(),'test1')

    def test_focus_form_clear(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        self.assertEqual(focus_form.f1.ename.get(),'test1')
        focus_form.enable_form()
        focus_form.clear_frame()
        self.assertEqual(focus_form.f1.ename.get(),'')

    def test_focus_form_enable(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        focus_form.enable_form()
        for item in focus_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_focus_form_disable(self):
        focus_form,focus_window = GUI_Focus_Form.create_form(None)
        focus_form.add_item(test__data.test_focus1,edit_call,save_call,close_call,cancel_call,list_call)
        focus_form.disable_form()
        for item in focus_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
