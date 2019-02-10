import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype_Form
import Archtype
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

def edit_call(list_window,arg):
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
class test_GUI_Archtype_Form(unittest.TestCase):
    def test_archtype_create(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        self.assertNotEqual(arch_form,None)

    def test_arch_form_setup(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        self.assertEqual(arch_form.lbltitle.cget('text'),'Archtype - test1')

    def test_arch_form_set_edit(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        arch_form.set_edit()
        self.assertEqual(arch_form.left_button.cget('text'),'Cancel')

    def test_arch_form_set_view(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        arch_form.set_view()
        self.assertEqual(arch_form.left_button.cget('text'),'Close')

    def test_arch_form_add_item(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        self.assertEqual(arch_form.f1.ename.get(),'test1')

    def test_arch_form_clear(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        self.assertEqual(arch_form.f1.ename.get(),'test1')
        arch_form.enable_form()
        arch_form.clear_frame()
        self.assertEqual(arch_form.f1.ename.get(),'')

    def test_arch_form_enable(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        arch_form.enable_form()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_arch_form_disable(self):
        arch_form,arch_window = GUI_Archtype_Form.create_form(None)
        arch_form.add_item(test__data.test_archtype1,close_call,cancel_call,edit_call,save_call)
        arch_form.disable_form()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
