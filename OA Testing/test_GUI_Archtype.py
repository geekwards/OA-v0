import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import GUI_Archtype
import Archtype

archsaved = False
incomingarch = Archtype.Archtype('','')
index = 0
test_archtype = Archtype.Archtype('Testing','TestDesc')

def save_archtype(idx,archtype):
    global archsaved
    global index
    global incomingarch

    archsaved = True
    incomingarch = archtype
    index = idx

class test_GUI_Archtype(unittest.TestCase):

    def test_load_form(self):
        archtype_window,archtype_form = GUI_Archtype.create_archtype_form(None)
        GUI_Archtype.load_data(test_archtype, save_archtype, 0)

        self.assertEqual(archtype_form.f1.ename.get(),'Testing')

    def test_load_form_close(self):
        archtype_window, archtype_form = GUI_Archtype.create_archtype_form(None)
        GUI_Archtype.load_data(test_archtype, save_archtype, 0)
        GUI_Archtype.close_click()

        self.assertFalse(archtype_window == None)

    def test_load_form_edit(self):
        archtype_window, archtype_form = GUI_Archtype.create_archtype_form(None)
        GUI_Archtype.load_data(test_archtype, save_archtype, 0)
        GUI_Archtype.edit_click()

        self.assertEqual(archtype_form.left_button.cget('text'),'Cancel')
        self.assertEqual(archtype_form.right_button.cget('text'),'Save')
        self.assertEqual(archtype_form.f1.ename.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.eshortdescription.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.estr.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.eper.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.eint.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.edex.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.echa.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.evit.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.emag.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.estamina.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.eattack.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.ereflex.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.efeats.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.emvmt.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.eskillpts.cget('state'),'normal')
        self.assertEqual(archtype_form.f1.elvlhealth.cget('state'),'normal')

    def test_edit_form_cancel(self):
        archtype_window, archtype_form = GUI_Archtype.create_archtype_form(None)
        GUI_Archtype.load_data(test_archtype, save_archtype, 0)
        GUI_Archtype.edit_click()
        archtype_form.f1.eshortdescription.delete(0,'end')
        archtype_form.f1.eshortdescription.insert(0,'Modified Description')
        self.assertEqual(archtype_form.f1.eshortdescription.get(),'Modified Description')
        GUI_Archtype.cancel_click()

        self.assertEqual(archtype_form.f1.eshortdescription.get(),'TestDesc')
        self.assertEqual(archtype_form.left_button.cget('text'),'Close')
        self.assertEqual(archtype_form.right_button.cget('text'),'Edit')
        self.assertEqual(archtype_form.f1.ename.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eshortdescription.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.estr.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eper.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eint.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.edex.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.echa.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.evit.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.emag.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.estamina.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eattack.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.ereflex.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.efeats.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.emvmt.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eskillpts.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.elvlhealth.cget('state'),'disabled')

    def test_edit_form_save(self):
        global archsaved
        global index
        global incomingarch

        archsaved = False
        incomingarch = Archtype.Archtype('','')

        archtype_window, archtype_form = GUI_Archtype.create_archtype_form(None)
        GUI_Archtype.load_data(test_archtype, save_archtype, 2)
        GUI_Archtype.edit_click()
        archtype_form.f1.eshortdescription.delete(0,'end')
        archtype_form.f1.eshortdescription.insert(0,'Modified Description')
        self.assertEqual(archtype_form.f1.eshortdescription.get(),'Modified Description')
        GUI_Archtype.save_click()

        self.assertTrue(archsaved)
        self.assertEqual(incomingarch.short_description, 'Modified Description')
        self.assertEqual(archtype_form.f1.eshortdescription.get(),'Modified Description')
        self.assertEqual(archtype_form.left_button.cget('text'),'Close')
        self.assertEqual(archtype_form.right_button.cget('text'),'Edit')
        self.assertEqual(archtype_form.f1.ename.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eshortdescription.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.estr.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eper.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eint.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.edex.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.echa.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.evit.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.emag.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.estamina.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eattack.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.ereflex.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.efeats.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.emvmt.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.eskillpts.cget('state'),'disabled')
        self.assertEqual(archtype_form.f1.elvlhealth.cget('state'),'disabled')

if __name__ == '__main__':
    unittest.main(verbosity=2)
