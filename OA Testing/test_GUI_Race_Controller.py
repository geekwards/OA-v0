import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import test__gui_race_controller
import Race
import Manage_Misc_Lists
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

class test_GUI_Race(unittest.TestCase):
    def test_race_controller_create(self):
        race_controller = test__gui_race_controller.GUI_controller()
        self.assertNotEqual(race_controller.get_form(),None)

    def test_race_controller_load(self):
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        self.assertEqual(race_controller.get_current_set(),test__data.test_race1)

    def test_race_controller_refresh(self):
        race_controller = test__gui_race_controller.GUI_controller()
        clone = test__data.test_race1.clone()
        clone.short_description = 'test prof'
        race_controller.load_data(clone,save_call,close_call)
        race_form = race_controller.get_form()
        self.assertEqual(race_form.f1.eshortdescr.get(),'test prof')
        clone2 = test__data.test_race1.clone()
        clone2.short_description = 'MODIFIED PROF'
        race_controller.load_data(clone2,save_call,close_call)
        self.assertEqual(race_controller.get_current_set(),clone2)

    def test_race_controller_close(self):
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        self.assertNotEqual(race_controller.get_form(),None)
        race_controller.close_call()
        self.assertEqual(race_controller.get_form(),None)

    def test_load_form_edit(self):
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_form = race_controller.get_form()
        race_controller.edit_call()
        for item in race_form.f1.winfo_children():
            self.assertEqual(str(item.cget('state')),'normal')

    def test_edit_form_cancel(self):
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_form = race_controller.get_form()
        race_controller.cancel_call()
        for item in race_form.f1.winfo_children():
            self.assertEqual(str(item.cget('state')),'disabled')

    def test_edit_form_save(self):
        global save_called
        save_called = False
        race_controller = test__gui_race_controller.GUI_controller()
        clone = test__data.test_race1.clone()
        race_controller.load_data(clone,save_call,close_call)
        race_controller.save_call()
        self.assertTrue(save_called)

    def test_load_picklist(self):
        langs = test__data.test_languages
        sizes = test__data.test_sizes
        bodies = test__data.test_bodies
        foc = test__data.test_foci1
        fea = test__data.test_feats
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_picklists(sizes,bodies,langs,foc,fea)
        self.assertEqual(race_controller.get_langs(),langs)
        self.assertEqual(race_controller.get_sizes(),sizes)
        self.assertEqual(race_controller.get_bodies(),bodies)
        self.assertEqual(race_controller.get_foc(),foc)
        self.assertEqual(race_controller.get_fea(),fea)
 
    def test_edit_picklist(self):
        langs = test__data.test_languages
        sizes = test__data.test_sizes
        bodies = test__data.test_bodies
        foc = test__data.test_foci1
        fea = test__data.test_feats
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_controller.load_picklists(sizes,bodies,langs,foc,fea)
        race_controller.edit_picklist('Languages')
        self.assertEqual(race_controller.get_current_picklist(),['lang1.1: +1', 'lang1.2: +2', 'lang1.3: +3'])
        self.assertEqual(race_controller.get_source_picklist(),['testlang1.1: langscore1.1','testlang1.2: langscore1.2','testlang1.3: langscore1.3'])
        race_controller.edit_picklist('Foci')
        self.assertEqual(race_controller.get_current_picklist(),['foci1.1', 'foci1.2', 'foci1.3'])
        self.assertEqual(race_controller.get_source_picklist(),['test1: testshortdesc1', 'test2: testshortdesc2', 'test3: testshortdesc3'])
        race_controller.edit_picklist('Feats')
        self.assertEqual(race_controller.get_current_picklist(),['feat1.1', 'feat1.2', 'feat1.3'])
        self.assertEqual(race_controller.get_source_picklist(),['testfeat1.1', 'testfeat1.2', 'testfeat1.3'])
 
    def test_save_picklist(self):
        langs = test__data.test_languages
        sizes = test__data.test_sizes
        bodies = test__data.test_bodies
        foc = test__data.test_foci1
        fea = test__data.test_feats
        race_controller = test__gui_race_controller.GUI_controller()
        race_controller.load_data(test__data.test_race1,save_call,close_call)
        race_controller.load_picklists(sizes,bodies,langs,foc,fea)
        race_controller.edit_picklist('Languages')
        race_controller.save_picklist('Languages',langs)
        self.assertEqual(race_controller.get_saved_picklist(),langs)
        race_controller.edit_picklist('Foci')
        race_controller.save_picklist('Foci',foc)
        self.assertEqual(race_controller.get_saved_picklist(),foc)
        race_controller.edit_picklist('Feats')
        race_controller.save_picklist('Feats',fea)
        self.assertEqual(race_controller.get_saved_picklist(),fea)

if __name__ == '__main__':
    unittest.main(verbosity=2)
