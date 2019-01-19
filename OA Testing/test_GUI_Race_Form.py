import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Race_Form
import Race

import test__data

new_called = False
edit_called = False
save_called = False
close_called = False
cancel_called = False
remove_called = False
picklist_called = False
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

def picklist_call(arg):
    global picklist_called
    global call_item
    picklist_called = True
    call_item = arg

class test_GUI_Race_Form(unittest.TestCase):
    def test_race_create(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        self.assertNotEqual(race_form,None)

    def test_race_form_setup(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        self.assertEqual(race_form.lbltitle.cget('text'),'Race - test1')

    def test_race_form_set_edit(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        race_form.set_edit()
        self.assertEqual(race_form.left_button.cget('text'),'Cancel')

    def test_race_form_set_view(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        race_form.set_view()
        self.assertEqual(race_form.left_button.cget('text'),'Close')

    def test_race_form_add_item(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        self.assertEqual(race_form.f1.ename.get(),'test1')

    def test_race_form_clear(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        self.assertEqual(race_form.f1.ename.get(),'test1')
        race_form.enable_form()
        race_form.clear_frame()
        self.assertEqual(race_form.f1.ename.get(),'')

    def test_race_form_enable(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        race_form.enable_form()
        for item in race_form.f1.winfo_children():
            if not (item.winfo_class() in('TCombobox','Listbox')):
                self.assertEqual(item.cget('state'),'normal')

    def test_race_form_disable(self):
        race_form,race_window = GUI_Race_Form.create_form(None)
        race_form.add_item(test__data.test_race1,edit_call,save_call,close_call,cancel_call,picklist_call)
        race_form.disable_form()
        for item in race_form.f1.winfo_children():
            if not (item.winfo_class() in('TCombobox','Listbox')):
                self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
