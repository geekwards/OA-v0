import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Equipment_Form
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

class test_GUI_Equipment_Form(unittest.TestCase):
    def test_equipment_create(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        self.assertNotEqual(equip_form,None)

    def test_equipment_form_setup(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        self.assertEqual(equip_form.lbltitle.cget('text'),'test - test1')

    def test_equipment_form_set_edit(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        equip_form.set_edit()
        self.assertEqual(equip_form.left_button.cget('text'),'Cancel')

    def test_equipment_form_set_view(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        equip_form.set_view()
        self.assertEqual(equip_form.left_button.cget('text'),'Close')

    def test_equipment_form_add_item(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        self.assertEqual(equip_form.f1.ename.get(),'test1')

    def test_equipment_form_clear(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        self.assertEqual(equip_form.f1.ename.get(),'test1')
        equip_form.enable_form()
        equip_form.clear_frame()
        self.assertEqual(equip_form.f1.ename.get(),'')

    def test_equipment_form_enable(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        equip_form.enable_form()
        for item in equip_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_equipment_form_disable(self):
        equip_form,equip_window = GUI_Equipment_Form.create_form(None)
        equip_form.add_item('test',test__data.test_base_equip1,edit_call,save_call,close_call,cancel_call)
        equip_form.disable_form()
        for item in equip_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
