import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Equipment_Controller
import test__data

new_called = False
edit_called = False
save_called = False
close_called = False
cancel_called = False
remove_called = False
call_name = ''
index = 0

def new_call():
    global new_called
    new_called = True

def save_call(arg):
    global save_called
    save_called = True

def edit_call(list_window,name):
    global edit_called
    global call_name
    edit_called = True
    call_name = name

def close_call():
    global close_called
    close_called = True

def cancel_call():
    global cancel_called
    cancel_called = True

def remove_call(list_item):
    global remove_called
    remove_called = True

class test_GUI_Equipment(unittest.TestCase):
    def test_equipment_controller_create(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        self.assertNotEqual(equip_controller.get_form(),None)

    def test_equipment_controller_load(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        self.assertEqual(equip_controller.get_current_set(),test__data.test_base_equip1)

    def test_equipment_controller_refresh(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        test__data.test_base_equip1.description = 'test prof'
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        arch_form = equip_controller.get_form()
        self.assertEqual(arch_form.f1.eweight.get(),'0')
        clone = test__data.test_base_equip1.clone()
        clone.description = 'MODIFIED PROF'
        equip_controller.load_data('equip',clone,save_call,close_call)
        self.assertEqual(equip_controller.get_current_set(),clone)

    def test_equipment_controller_close(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        self.assertNotEqual(equip_controller.get_form(),None)
        equip_controller.close_call()
        self.assertEqual(equip_controller.get_form(),None)

    def test_load_form_edit(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        arch_form = equip_controller.get_form()
        equip_controller.edit_call()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        arch_form = equip_controller.get_form()
        equip_controller.cancel_call()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global save_called
        save_called = False
        equip_controller = GUI_Equipment_Controller.GUI_equipment_controller()
        equip_controller.load_data('equip',test__data.test_base_equip1,save_call,close_call)
        equip_controller.save_call()
        self.assertTrue(save_called)

if __name__ == '__main__':
    unittest.main(verbosity=2)
