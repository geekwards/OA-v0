import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype_Form
import Archtype

archsaved = False
archremoved = False
archedit = False
archnew = False
archclose = False
archcancel = False
index = 0
test_archtypes = Archtype.Archtypes()
test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

test_archtypes.add_new(test_archtype1)
test_archtypes.add_new(test_archtype2)

def save_arch(idx,misc_list):
    global listsaved
    global index
    global incominglist

    listsaved = True
    incominglist = misc_list
    index = idx

def edit_arch(idx):
    global listedit
    global index

    listedit = True
    index = idx

def remove_arch(idx):
    global listremoved
    global index

    listremoved = True
    index = idx

def new_arch():
    global listnew

    listnew = True

def close_arch():
    global listclose

    listclose = True

def cancel_arch():
    global listcancel

    listcancel = True

class test_GUI_Archtype_Form(unittest.TestCase):

    def test_archtype_create(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        self.assertNotEqual(arch_form,None)

    def test_arch_form_setup(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)
        self.assertEqual(arch_form.lbltitle.cget('text'),'Archtype - Test1')

    def test_arch_form_set_edit(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)
        arch_form.set_edit()
        self.assertEqual(arch_form.left_button.cget('text'),'Cancel')

    def test_misc_form_set_view(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)
        arch_form.set_view()
        self.assertEqual(arch_form.left_button.cget('text'),'Close')

    def test_misc_form_add_item(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)
        self.assertEqual(arch_form.f1.ename.cget('text'),'Test1')

    def test_misc_form_clear(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)
        self.assertEqual(arch_form.f1.ename.cget('text'),'Test1')

        arch_form.clear()
        self.assertEqual(arch_form.f1.ename.cget('text'),'')

    def test_misc_form_enable(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)

        arch_form.enable_form()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_misc_form_disable(self):
        arch_form,arch_window = GUI_Archtype_Form.create_archtype_form(None)
        arch_form.add_item(test_archtype1,close_arch,cancel_arch,edit_arch,save_arch)

        arch_form.disable_form()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
