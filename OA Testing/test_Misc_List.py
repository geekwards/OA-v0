import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List


class test_Misc_List(unittest.TestCase):

    def test_create_misc_list(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

        self.assertEqual(test_object1.name,'Test1')

    def test_misc_list_get_list(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

        self.assertTrue(test_object1.all_items[0],'Testlist 1.1')
        self.assertTrue(test_object1.all_items[1],'Testlist 1.2')
        self.assertTrue(test_object1.all_items[2],'Testlist 1.3')

    def test_misc_list_unequal(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        self.assertFalse(test_object1.equals(test_object2))

    def test_misc_list_clone(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = test_object1.clone()

        self.assertTrue(test_object1.equals(test_object2))

    def test_misc_list_add_new(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

        test_object1.add_new('Testlist 1.4')

        self.assertTrue(test_object1.all_items[0],'Testlist 1.1')
        self.assertTrue(test_object1.all_items[1],'Testlist 1.2')
        self.assertTrue(test_object1.all_items[2],'Testlist 1.3')
        self.assertTrue(test_object1.all_items[3],'Testlist 1.4')

    def test_misc_list_remove(self):
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])

        test_object1.remove('Testlist 1.2')

        self.assertTrue(test_object1.all_items[0],'Testlist 1.1')
        self.assertTrue(test_object1.all_items[1],'Testlist 1.3')

if __name__ == '__main__':
    unittest.main(verbosity=2)
