import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Money
import test__data

class test_Monies(unittest.TestCase):
    def test_monies_create_and_isempty(self):
        test_monies = Money.Monies()
        self.assertTrue(test_monies.isempty())

    def test_monies_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_monies),3)
        self.assertEqual(test__data.test_monies.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_monies.get_item('test3').short_description,'testdesc3')

    def test_monies_get_list(self):
        self.assertEqual(len(test__data.test_monies),3)
        self.assertEqual(test__data.test_monies.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_monies.list_of_items[1].name,'test1')

    def test_monies_update(self):
        self.assertEqual(len(test__data.test_monies),2)
        self.assertEqual(test__data.test_monies.all_items[0].name,'test1')
        self.assertEqual(test__data.test_monies.all_items[1].name,'test3')
        test__data.test_monies.update(test__data.test_money3)
        self.assertEqual(test__data.test_monies.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_monies.all_items[1].short_description,'testdesc3')

    def test_monies_update_new(self):
        self.assertEqual(len(test__data.test_monies),2)
        self.assertEqual(test__data.test_monies.all_items[0].name,'test1')
        self.assertEqual(test__data.test_monies.all_items[1].name,'test3')
        test__data.test_monies.update(test__data.test_money3)
        self.assertEqual(test__data.test_monies.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_monies.all_items[1].name,'test3')

    def test_monies_remove(self):
        self.assertEqual(len(test__data.test_monies),3)
        test__data.test_monies.remove(test__data.test_money2)
        self.assertEqual(len(test__data.test_monies),2)
        self.assertEqual(test__data.test_monies.all_items[1].name,'test3')

    def test_monies_equals(self):
        self.assertTrue(test__data.test_monies == test__data.test_monies2)

    def test_monies_notequals(self):
        self.assertFalse(test__data.test_monies == test__data.test_monies3)

    def test_monies_clone(self):
        clone = test__data.test_monies.clone()
        self.assertTrue(test__data.test_monies == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_monies == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
