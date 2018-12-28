import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype_Controller
import Archtype

arch_save = False
arch_close = False
incomingarch = Archtype.Archtype('','')
index = 0
test_archtype = Archtype.Archtype('Testing','TestDesc')

def save_archtype(arch):
    global arch_save

    arch_save = True

def close_archtype():
    global arch_close

    arch_close = True

class test_GUI_Archtype(unittest.TestCase):

    def test_archtype_controller_create(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        self.assertNotEqual(arch_controller.get_archtype_form(),None)

    def test_archtype_controller_load(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        self.assertEqual(arch_controller.get_current_archtype(),test_archtype)

    def test_archtype_controller_refresh(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        test_archtype.proficiency = 'test prof'
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        arch_form = arch_controller.get_archtype_form()
        self.assertEqual(arch_form.f1.eproficiency.get(),'test prof')

        clone = test_archtype.clone()
        clone.proficiency = 'MODIFIED PROF'

        arch_controller.load_data(clone,save_archtype,close_archtype,True)
        self.assertEqual(arch_controller.get_current_archtype(),clone)

    def test_archtype_controller_close(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        self.assertNotEqual(arch_controller.get_archtype_form(),None)

        arch_controller.close_click()
        self.assertEqual(arch_controller.get_archtype_form(),None)

    def test_load_form_edit(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        arch_form = arch_controller.get_archtype_form()

        arch_controller.edit_click()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        arch_form = arch_controller.get_archtype_form()

        arch_controller.cancel_click()
        for item in arch_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global arch_save
    
        arch_save = False

        arch_controller = GUI_Archtype_Controller.GUI_archtype_controller()
        arch_controller.load_data(test_archtype,save_archtype,close_archtype,True)
        arch_controller.save_click()
        self.assertTrue(arch_save)

if __name__ == '__main__':
    unittest.main(verbosity=2)
