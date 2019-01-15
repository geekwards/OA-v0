import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Focus
import test__data

class test_Foci(unittest.TestCase):
    def test_focus_create_and_isempty(self):
        test_foci = Focus.Foci()
        self.assertTrue(test_foci.isempty())

    def test_focus_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_foci),3)
        self.assertEqual(test__data.test_foci.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_foci.get_item('test3').short_description,'testdesc3')

    def test_focus_get_list(self):
        self.assertEqual(len(test__data.test_foci),3)
        self.assertEqual(test__data.test_foci.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_foci.list_of_items[1].name,'test1')

    def test_focus_update(self):
        self.assertEqual(len(test__data.test_foci),2)
        self.assertEqual(test__data.test_foci.all_items[0].name,'test1')
        self.assertEqual(test__data.test_foci.all_items[1].name,'test3')
        test__data.test_foci.update(test__data.test_focus3)
        self.assertEqual(test__data.test_foci.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_foci.all_items[1].short_description,'testdesc3')

    def test_focus_update_new(self):
        self.assertEqual(len(test__data.test_foci),2)
        self.assertEqual(test__data.test_foci.all_items[0].name,'test1')
        self.assertEqual(test__data.test_foci.all_items[1].name,'test3')
        test__data.test_foci.update(test__data.test_focus3)
        self.assertEqual(test__data.test_foci.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_foci.all_items[1].name,'test3')

    def test_focus_remove(self):
        self.assertEqual(len(test__data.test_foci),3)
        test__data.test_foci.remove(test__data.test_focus2)
        self.assertEqual(len(test__data.test_foci),2)
        self.assertEqual(test__data.test_foci.all_items[1].name,'test3')

    def test_focus_equals(self):
        self.assertTrue(test__data.test_foci == test__data.test_foci2)

    def test_focus_notequals(self):
        self.assertFalse(test__data.test_foci == test__data.test_foci3)

    def test_focus_clone(self):
        clone = test__data.test_foci.clone()
        self.assertTrue(test__data.test_foci == clone)
        clone.get_item('test3').short_description = 'modified short descr'
        self.assertFalse(test__data.test_foci == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
