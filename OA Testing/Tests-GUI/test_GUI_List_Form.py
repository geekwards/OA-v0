import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_List_Form
import List_Object

test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

listsaved = False
listremoved = False
listedit = False
listnew = False
listclose = False
listcancel = False
index = 0

def save_list(idx,misc_list):
    global listsaved
    global index
    global incominglist

    listsaved = True
    incominglist = misc_list
    index = idx

def edit_list(idx):
    global listedit
    global index

    listedit = True
    index = idx

def remove_list(idx):
    global listremoved
    global index

    listremoved = True
    index = idx

def new_list():
    global listnew

    listnew = True

def close_list():
    global listclose

    listclose = True

def cancel_list():
    global listcancel

    listcancel = True

class test_GUI_List_Form(unittest.TestCase):

    def test_list_form_create(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        self.assertNotEqual(list_form,None)

    def test_list_form_setup(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup('list_title',new_list,close_list,edit_list,remove_list)
        self.assertEqual(list_form.lbltitle.cget('text'),'list_title')

    def test_list_form_add_item(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup('list_title',new_list,close_list,edit_list,remove_list)
        list_form.add_item(0,'item1')
        list_form.add_item(0,'item2')
        self.assertEqual(len(list_form.f1.winfo_children()),6)

    def test_list_form_clear(self):
        list_form,list_window = GUI_List_Form.create_list_form(None)
        list_form.setup('list_title',new_list,close_list,edit_list,remove_list)
        list_form.add_item(0,'item1')
        list_form.add_item(0,'item2')
        self.assertEqual(len(list_form.f1.winfo_children()),6)

        list_form.clear()
        self.assertEqual(len(list_form.f1.winfo_children()),0)

if __name__ == '__main__':
    unittest.main(verbosity=2)
