import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_List

class test_Misc_Lists(unittest.TestCase):

    def test_objects_create(self):
        test_objects = Misc_List.Misc_lists()

        self.assertTrue(test_objects.isempty())

    def test_objects_add_and_get(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.all_lists[0].name,'Test1')
        self.assertEqual(test_objects.all_lists[1].name,'Test2')
        self.assertEqual(test_objects.get_misc_list('Test1').name,'Test1')
        self.assertEqual(test_objects.get_misc_list('Test2').name,'Test2')
        self.assertEqual(test_objects.get_misc_list('Test1').all_items[0],'Testlist 1.1')

    def test_objects_get_list(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.get_misc_list('Test1').name,'Test1')
        self.assertEqual(test_objects.get_misc_list('Test2').name,'Test2')

    def test_objects_get_list_item(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.get_misc_list('Test1').name,'Test1')
        self.assertEqual(test_objects.get_misc_list('Test2').name,'Test2')

    def test_objects_get_list_item2(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_object3 = Misc_List.Misc_list('Test2',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.all_lists[0].name,'Test1')
        self.assertEqual(test_objects.all_lists[1].name,'Test2')

        test_objects.update(test_object3)
        self.assertEqual(test_objects.all_lists[1].all_items[0],'Testlist 3.1')
        self.assertEqual(test_objects.all_lists[1].all_items[2],'Testlist 3.3')

    def test_objects_get_list_item_fail(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_object3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.all_lists[0].name,'Test1')
        self.assertEqual(test_objects.all_lists[1].name,'Test2')

        test_objects.update(test_object3)
        self.assertEqual(test_objects.all_lists[1].name,'Test2')
        self.assertEqual(test_objects.list_of_lists[1].name,'Test2')
        self.assertEqual(test_objects.all_lists[2].name,'Test3')
        self.assertEqual(test_objects.list_of_lists[2].name,'Test3')

    def test_objects_remove(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_object3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects.add_new(test_object3)
        self.assertEqual(len(test_objects),3)
        
        test_objects.remove(test_object2)
        self.assertEqual(len(test_objects),2)
        self.assertEqual(test_objects.get_misc_list('Test3').name,'Test3')

    def test_objects_equals(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_objects2 = Misc_List.Misc_lists()

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects2.add_new(test_object1)
        test_objects2.add_new(test_object2)

        self.assertTrue(test_objects.equals(test_objects2))

    def test_objects_notequals(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])
        test_object3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])
        test_objects2 = Misc_List.Misc_lists()
       
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects2.add_new(test_object1)
        test_objects2.add_new(test_object2)
        test_objects2.add_new(test_object3)
        
        self.assertFalse(test_objects.equals(test_objects2))

    def test_objects_clone(self):
        test_objects = Misc_List.Misc_lists()
        test_object1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
        test_object2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects2 = test_objects.clone()

        self.assertTrue(test_objects.equals(test_objects2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
