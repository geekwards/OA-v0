import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List_Form
import Misc_List

listsaved = False
listremoved = False
listedit = False
listnew = False
listclose = False
listcancel = False
index = 0
test_misc_list = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

def save_misc_list(idx,misc_list):
    global listsaved
    global index
    global incominglist

    listsaved = True
    incominglist = misc_list
    index = idx

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

class test_GUI_Misc_List_Form(unittest.TestCase):

    def test_misc_form_create(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        self.assertNotEqual(misc_form,None)

    def test_misc_form_setup(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        self.assertEqual(misc_form.lbltitle.cget('text'),'list_title')

    def test_misc_form_set_edit(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.set_edit()
        self.assertEqual(misc_form.left_button.cget('text'),'Cancel')

    def test_misc_form_set_view(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.set_view()
        self.assertEqual(misc_form.left_button.cget('text'),'Close')

    def test_misc_form_add_item(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.add_item(0,'item1')
        misc_form.add_item(0,'item2')
        self.assertEqual(len(misc_form.f1.winfo_children()),2)

    def test_misc_form_clear(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.add_item(0,'item1')
        misc_form.add_item(0,'item2')
        self.assertEqual(len(misc_form.f1.winfo_children()),2)

        misc_form.clear()
        self.assertEqual(len(misc_form.f1.winfo_children()),0)

    def test_misc_form_enable(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.add_item(0,'item1')
        misc_form.add_item(0,'item2')
        self.assertEqual(len(misc_form.f1.winfo_children()),2)

        misc_form.enable_form()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_form_disable(self):
        misc_form,misc_window = GUI_Misc_List_Form.create_misc_list_form(None)
        misc_form.setup('list_title',new_misc_list,close_misc_list,edit_misc_list,save_misc_list,cancel_misc_list)
        misc_form.add_item(0,'item1')
        misc_form.add_item(0,'item2')
        self.assertEqual(len(misc_form.f1.winfo_children()),2)

        misc_form.disable_form()
        for item in misc_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
