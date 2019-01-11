import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Race
import test__data

class test_Races(unittest.TestCase):

    def test_races_create_and_isempty(self):
        test_races = Race.Races()

        self.assertTrue(test_races.isempty())

    def test_races_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_races),4)
        self.assertEqual(test__data.test_races.get_item('test').short_description,'test short descr')
        self.assertEqual(test__data.test_races.get_item('Test2').short_description,'TestDesc2')

    def test_races_get_list(self):
        self.assertEqual(len(test__data.test_races),4)
        self.assertEqual(test__data.test_races.list_of_items[0].name,'test')
        self.assertEqual(test__data.test_races.list_of_items[1].name,'test')

    def test_races_update(self):
        self.assertEqual(len(test__data.test_races),3)
        self.assertEqual(test__data.test_races.all_items[0].name,'test')
        self.assertEqual(test__data.test_races.all_items[1].name,'Test2')

        test__data.test_races.update(test__data.test_race3)
        self.assertEqual(test__data.test_races.list_of_items[1].short_description,'TestDesc2')
        self.assertEqual(test__data.test_races.all_items[1].short_description,'TestDesc2')

    def test_races_update_new(self):
        self.assertEqual(len(test__data.test_races),3)
        self.assertEqual(test__data.test_races.all_items[0].name,'test')
        self.assertEqual(test__data.test_races.all_items[1].name,'Test2')

        test__data.test_races.update(test__data.test_race3)
        self.assertEqual(test__data.test_races.list_of_items[1].name,'Test2')
        self.assertEqual(test__data.test_races.all_items[1].name,'Test2')
        self.assertEqual(test__data.test_races.list_of_items[2].name,'Test3')
        self.assertEqual(test__data.test_races.all_items[2].name,'Test3')

    def test_races_remove(self):
        self.assertEqual(len(test__data.test_races),4)
        test__data.test_races.remove(test__data.test_races.all_items[1])
        self.assertEqual(len(test__data.test_races),3)
        self.assertEqual(test__data.test_races.all_items[1].name,'Test2')

    def test_races_equals(self):
        self.assertTrue(test__data.test_races == test__data.test_races2)

    def test_races_notequals(self):
        self.assertFalse(test__data.test_races == test__data.test_races3)

    def test_races_clone(self):
        clone = test__data.test_races.clone()
        self.assertTrue(test__data.test_races == clone)

        clone.get_item('Test2').description = 'modified short descr'
        self.assertFalse(test__data.test_races == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
