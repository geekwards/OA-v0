import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype
import test__data

class test_Archtypes(unittest.TestCase):
    def test_archtypes_create_and_isempty(self):
        test_archtypes = Archtype.Archtypes()
        self.assertTrue(test_archtypes.isempty())

    def test_archtypes_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_archtypes),4)
        self.assertEqual(test__data.test_archtypes.get_item('test').short_description,'testdesc')
        self.assertEqual(test__data.test_archtypes.get_item('Test2').short_description,'TestDesc2b')

    def test_archtypes_get_list(self):
        self.assertEqual(len(test__data.test_archtypes),4)
        self.assertEqual(test__data.test_archtypes.list_of_items[0].name,'test')
        self.assertEqual(test__data.test_archtypes.list_of_items[1].name,'test')

    def test_archtypes_update(self):
        self.assertEqual(len(test__data.test_archtypes),3)
        self.assertEqual(test__data.test_archtypes.all_items[0].name,'test')
        self.assertEqual(test__data.test_archtypes.all_items[1].name,'Test2')
        test__data.test_archtypes.update(test__data.test_archtype3)
        self.assertEqual(test__data.test_archtypes.list_of_items[1].short_description,'TestDesc2b')
        self.assertEqual(test__data.test_archtypes.all_items[1].short_description,'TestDesc2b')

    def test_archtypes_update_new(self):
        self.assertEqual(len(test__data.test_archtypes),3)
        self.assertEqual(test__data.test_archtypes.all_items[0].name,'test')
        self.assertEqual(test__data.test_archtypes.all_items[1].name,'Test2')
        test__data.test_archtypes.update(test__data.test_archtype3)
        self.assertEqual(test__data.test_archtypes.list_of_items[1].name,'Test2')
        self.assertEqual(test__data.test_archtypes.all_items[1].name,'Test2')
        self.assertEqual(test__data.test_archtypes.list_of_items[2].name,'Test3')
        self.assertEqual(test__data.test_archtypes.all_items[2].name,'Test3')

    def test_archtypes_remove(self):
        self.assertEqual(len(test__data.test_archtypes),4)
        test__data.test_archtypes.remove(test__data.test_archtype2)
        self.assertEqual(len(test__data.test_archtypes),3)
        self.assertEqual(test__data.test_archtypes.all_items[1].name,'Test2')

    def test_archtypes_equals(self):
        self.assertTrue(test__data.test_archtypes == test__data.test_archtypes2)

    def test_archtypes_notequals(self):
        self.assertFalse(test__data.test_archtypes == test__data.test_archtypes3)

    def test_archtypes_clone(self):
        clone = test__data.test_archtypes.clone()
        self.assertTrue(test__data.test_archtypes == clone)
        clone.get_item('Test2').short_description = 'modified short descr'
        self.assertFalse(test__data.test_archtypes == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
