import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Misc_List
import List_Object

listsaved = False
incominglist = []
incominglist.append(List_Object.Listobject('',''))
index = 0
test_misc_list = []
test_misc_list.append(List_Object.Listobject('Testing',''))

def save_misc_list(idx,misc_list):
    global listsaved
    global index
    global incominglist

    listsaved = True
    incominglist = misc_list
    index = idx

class test_GUI_Misc_List(unittest.TestCase):

    def test_load_form(self):
        list_window,list_form = GUI_Misc_List.create_misc_list_form(None)
        GUI_Misc_List.load_data(test_misc_list, save_misc_list, 0)

        self.assertEqual(misc_list_form.f1.ename.get(),'Testing')

    def test_load_form_close(self):
        list_window,list_form = GUI_Misc_List.create_misc_list_form(None)
        GUI_Misc_List.load_data(test_misc_list, save_misc_list, 0)
        GUI_Misc_List.close_click()

        self.assertFalse(list_window == None)

    def test_load_form_edit(self):
        list_window,list_form = GUI_Misc_List.create_misc_list_form(None)
        GUI_Misc_List.load_data(test_misc_list, save_misc_list, 0)
        GUI_Misc_List.edit_click()

        self.assertEqual(list_form.left_button.cget('text'),'Cancel')
        self.assertEqual(list_form.right_button.cget('text'),'Save')

        for item in list_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'normal')

    def test_edit_form_cancel(self):
        list_window,list_form = GUI_Misc_List.create_misc_list_form(None)
        GUI_Misc_List.load_data(test_misc_list, save_misc_list, 0)
        GUI_Misc_List.edit_click()
        list_form.f1.eshortdescription.delete(0,'end')
        list_form.f1.eshortdescription.insert(0,'Modified Description')
        self.assertEqual(list_form.f1.eshortdescription.get(),'Modified Description')
        GUI_Archtype.cancel_click()

        self.assertEqual(list_form.f1.eshortdescription.get(),'TestDesc')
        self.assertEqual(list_form.left_button.cget('text'),'Close')
        self.assertEqual(list_form.right_button.cget('text'),'Edit')

        for item in list_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

    def test_edit_form_save(self):
        global listsaved
        global index
        global incominglist

        listsaved = False
        incominglist = List_Object.Listobject('','')

        list_window, list_form = GUI_Misc_List.create_misc_list_form(None)
        GUI_Misc_List.load_data(test_misc_list, save_misc_list, 2)
        GUI_Misc_List.edit_click()
        list_form.f1.eshortdescription.delete(0,'end')
        list_form.f1.eshortdescription.insert(0,'Modified Description')
        self.assertEqual(list_form.f1.eshortdescription.get(),'Modified Description')
        GUI_Misc_List.save_click()

        self.assertTrue(listsaved)
        self.assertEqual(list_form.f1.eshortdescription.get(),'Modified Description')
        self.assertEqual(list_form.left_button.cget('text'),'Close')
        self.assertEqual(list_form.right_button.cget('text'),'Edit')

        for item in list_form.f1.winfo_children():
            self.assertEqual(item.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
