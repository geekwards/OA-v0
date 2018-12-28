import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List

class test_Misc_Lists(unittest.TestCase):

    def test_misc_list_create_and_isempty(self):
        test_misc_lists = Misc_List.Misc_lists()

        self.assertTrue(test_misc_lists.isempty())

    def test_misc_list_add_and_get_and_len(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)

        self.assertEqual(len(test_misc_lists),2)
        self.assertEqual(test_misc_lists.all_lists[0].name,'Test1')
        self.assertEqual(test_misc_lists.all_lists[1].name,'Test2')
        self.assertEqual(test_misc_lists.get_misc_list('Test1').name,'Test1')
        self.assertEqual(test_misc_lists.get_misc_list('Test2').name,'Test2')
        self.assertEqual(test_misc_lists.get_misc_list('Test1').all_items[0],'Testlist 1.1')

    def test_misc_list_update(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_misc_list3 = Misc_List.Misc_list('Test2',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)

        self.assertEqual(len(test_misc_lists),2)
        self.assertEqual(test_misc_lists.all_lists[0].name,'Test1')
        self.assertEqual(test_misc_lists.all_lists[1].name,'Test2')

        test_misc_lists.update(test_misc_list3)
        self.assertEqual(test_misc_lists.all_lists[1].all_items[0],'Testlist 3.1')
        self.assertEqual(test_misc_lists.all_lists[1].all_items[2],'Testlist 3.3')

    def test_misc_list_get_list_item_fail(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_misc_list3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)

        self.assertEqual(len(test_misc_lists),2)
        self.assertEqual(test_misc_lists.all_lists[0].name,'Test1')
        self.assertEqual(test_misc_lists.all_lists[1].name,'Test2')

        test_misc_lists.update(test_misc_list3)
        self.assertEqual(test_misc_lists.all_lists[1].name,'Test2')
        self.assertEqual(test_misc_lists.list_of_lists[1].name,'Test2')
        self.assertEqual(test_misc_lists.all_lists[2].name,'Test3')
        self.assertEqual(test_misc_lists.list_of_lists[2].name,'Test3')

    def test_misc_list_remove(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_misc_list3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)
        test_misc_lists.add_new(test_misc_list3)
        self.assertEqual(len(test_misc_lists),3)
        
        test_misc_lists.remove(test_misc_list2)
        self.assertEqual(len(test_misc_lists),2)
        self.assertEqual(test_misc_lists.get_misc_list('Test3').name,'Test3')

    def test_misc_list_equals(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_objects2 = Misc_List.Misc_lists()

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)
        test_objects2.add_new(test_misc_list1)
        test_objects2.add_new(test_misc_list2)

        self.assertTrue(test_misc_lists.equals(test_objects2))

    def test_misc_list_notequals(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_misc_list3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])
        test_objects2 = Misc_List.Misc_lists()
       
        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)
        test_objects2.add_new(test_misc_list1)
        test_objects2.add_new(test_misc_list2)
        test_objects2.add_new(test_misc_list3)
        
        self.assertFalse(test_misc_lists.equals(test_objects2))

    def test_misc_list_clone(self):
        test_misc_lists = Misc_List.Misc_lists()
        test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_misc_lists.add_new(test_misc_list1)
        test_misc_lists.add_new(test_misc_list2)
        test_objects2 = test_misc_lists.clone()

        self.assertTrue(test_misc_lists.equals(test_objects2))

        test_objects2.all_lists[1].all_items[1] = 'modified'
        self.assertFalse(test_misc_lists.equals(test_objects2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
