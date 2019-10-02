import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__gui_picklist_controller
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

def save_call(arg1,arg2):
    global save_called
    global call_item
    save_called = True
    call_item = arg1

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

class test_GUI_Picklist(unittest.TestCase):
    def test_picklist_controller_create(self):
        picklist_controller = test__gui_picklist_controller.GUI_controller()
        picklist_controller.create_form()
        self.assertNotEqual(picklist_controller.get_form(),None)

    def test_picklist_controller_load(self):
        picklist_controller = test__gui_picklist_controller.GUI_controller()
        picklist_controller.create_form()
        picklist_controller.load_data('TEST',test__data.test_picklist1,test__data.test_picklist2,save_call)
        self.assertEqual(picklist_controller.get_selected(),test__data.test_picklist4)

    def test_picklist_controller_refresh(self):
        picklist_controller = test__gui_picklist_controller.GUI_controller()
        clone = test__data.test_picklist1
        clone2 = test__data.test_picklist2
        picklist_controller.create_form()
        picklist_controller.load_data('TEST',clone,clone2,save_call)
        picklist_form = picklist_controller.get_form()
        self.assertEqual(picklist_form.f1.winfo_children()[1].get(0,'end'),('test1.4', 'test1.3', 'test1.2', 'test1.1'))
        clone[0] = 'MODIFIED PROF'
        picklist_controller.load_data('TEST',clone,clone2,save_call)
        self.assertEqual(picklist_form.f1.winfo_children()[1].get(0,'end'),('test1.4', 'test1.3', 'test1.2', 'MODIFIED PROF'))

    def test_edit_form_cancel(self):
        picklist_controller = test__gui_picklist_controller.GUI_controller()
        picklist_controller.create_form()
        picklist_controller.load_data('TEST',test__data.test_picklist1,test__data.test_picklist2,save_call)
        picklist_form = picklist_controller.get_form()
        picklist_controller.cancel_call()
        self.assertEqual(picklist_controller.get_form(),None)

    def test_edit_form_save(self):
        global save_called
        save_called = False
        picklist_controller = test__gui_picklist_controller.GUI_controller()
        picklist_controller.create_form()
        picklist_controller.load_data('TEST',test__data.test_picklist1,test__data.test_picklist2,save_call)
        picklist_controller.save_call()
        self.assertTrue(save_called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
