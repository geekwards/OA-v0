import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Race_Controller
import Race
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

class test_GUI_Race(unittest.TestCase):

    def test_race_controller_create(self):
        race_controller = GUI_Race_Controller.GUI_race_controller()
        self.assertNotEqual(race_controller.get_form(),None)

    def test_race_controller_load(self):
        race_controller = GUI_Race_Controller.GUI_race_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        self.assertEqual(race_controller.get_current_set(),test__data.test_race1)

    def test_race_controller_close(self):
        race_controller = GUI_Race_Controller.GUI_race_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        self.assertNotEqual(race_controller.get_form(),None)
        race_controller.close_call()
        self.assertEqual(race_controller.get_form(),None)

    def test_load_form_edit(self):
        race_controller = GUI_Race_Controller.GUI_race_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_form = race_controller.get_form()
        race_controller.edit_call()
        for item in race_form.f1.winfo_children():
            if not (item.winfo_class() in('TCombobox','Listbox')):
                self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        race_controller = GUI_Race_Controller.GUI_race_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_form = race_controller.get_form()
        race_controller.cancel_call()
        for item in race_form.f1.winfo_children():
            if not (item.winfo_class() in('TCombobox','Listbox')):
                self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global save_called
        save_called = False
        race_controller = GUI_Race_Controller.GUI_race_controller()
        race_controller.load_data(test__data.test_race1.clone(),save_call,close_call)
        race_controller.save_call()
        self.assertTrue(save_called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
