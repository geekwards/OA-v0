import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List_Form
import Misc_List
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

class test_GUI_Misc_List_Form(unittest.TestCase):
    def test_misc_form_create(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        self.assertNotEqual(misc_form,None)

    def test_misc_form_setup(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        self.assertEqual(misc_form.lbltitle.cget('text'),'list_title')

    def test_misc_form_set_edit(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.set_edit()
        self.assertEqual(misc_form.left_button.cget('text'),'Cancel')

    def test_misc_form_set_view(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.set_view()
        self.assertEqual(misc_form.left_button.cget('text'),'Close')

    def test_misc_form_add_item(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.add_item(0,List_Object.List_object('item1','short desc 1'))
        misc_form.add_item(0,List_Object.List_object('item2','short desc 2'))
        self.assertEqual(len(misc_form.f1.winfo_children()),4)

    def test_misc_form_clear(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.add_item(0,List_Object.List_object('item1','short desc 1'))
        misc_form.add_item(0,List_Object.List_object('item2','short desc 2'))
        self.assertEqual(len(misc_form.f1.winfo_children()),4)
        misc_form.clear_frame()
        self.assertEqual(len(misc_form.f1.winfo_children()),0)

    def test_misc_form_enable(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.add_item(0,List_Object.List_object('item1','short desc 1'))
        misc_form.add_item(0,List_Object.List_object('item2','short desc 2'))
        self.assertEqual(len(misc_form.f1.winfo_children()),4)
        misc_form.enable_form()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_form_disable(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_form(None)
        misc_form.setup_form('list_title',new_call,edit_call,save_call,close_call,cancel_call)
        misc_form.add_item(0,List_Object.List_object('item1','short desc 1'))
        misc_form.add_item(0,List_Object.List_object('item2','short desc 2'))
        self.assertEqual(len(misc_form.f1.winfo_children()),4)
        misc_form.disable_form()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
