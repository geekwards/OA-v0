import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_List_Form
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
class test_GUI_List_Form(unittest.TestCase):
    def test_list_form_create(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        self.assertNotEqual(list_form,None)

    def test_list_form_setup(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup_form('list_title',new_call,close_call,edit_call,remove_call)
        self.assertEqual(list_form.lbltitle.cget('text'),'list_title')

    def test_list_form_add_item(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup_form('list_title',new_call,close_call,edit_call,remove_call)
        list_form.add_item(0,'item1')
        list_form.add_item(0,'item2')
        self.assertEqual(len(list_form.f1.winfo_children()),6)

    def test_list_form_clear(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup_form('list_title',new_call,close_call,edit_call,remove_call)
        list_form.add_item(0,'item1')
        list_form.add_item(0,'item2')
        self.assertEqual(len(list_form.f1.winfo_children()),6)

        list_form.clear_frame()
        self.assertEqual(len(list_form.f1.winfo_children()),0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
