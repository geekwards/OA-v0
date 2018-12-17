import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import List_Object

test_objects = List_Object.Listobjects()
test_object1 = List_Object.Listobject('Test1','TestDesc1')
test_object2 = List_Object.Listobject('Test2','TestDesc2')
test_object3 = List_Object.Listobject('Test3','TestDesc3')


class test_objects(unittest.TestCase):

    def test_objects_create(self):
        self.assertTrue(test_objects.isempty())

    def test_objects_add_and_get(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects.get_all()),2)
        self.assertEqual(test_objects[0].name,'Test1')
        self.assertEqual(test_objects[1].name,'Test2')
        self.assertEqual(test_objects.get_all()[0].name,'Test1')
        self.assertEqual(test_objects.get_all()[1].name,'Test2')

    def test_objects_get_list(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects.get_list()),2)
        self.assertEqual(test_objects.get_list()[0].name,'Test1')
        self.assertEqual(test_objects.get_list()[1].name,'Test2')

    def test_objects_get_list_item(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)

        self.assertEqual(len(test_objects.get_list()),2)
        self.assertEqual(test_objects.get_list_item(0).name,'Test1')
        self.assertEqual(test_objects.get_list_item(1).name,'Test2')

    def test_objects_get_list_item(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        self.assertEqual(len(test_objects.get_list()),2)
        self.assertEqual(test_objects.get_list_item(0).name,'Test1')
        self.assertEqual(test_objects.get_list_item(1).name,'Test2')

        test_objects.update(1,test_object3)
        self.assertEqual(test_objects.get_list()[1].name,'Test3')
        self.assertEqual(test_objects.get_list_item(1).name,'Test3')

    def test_objects_get_list_item_fail(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        self.assertEqual(len(test_objects.get_list()),2)
        self.assertEqual(test_objects.get_list_item(0).name,'Test1')
        self.assertEqual(test_objects.get_list_item(1).name,'Test2')

        test_objects.update(2,test_object3)
        self.assertEqual(test_objects.get_list()[1].name,'Test2')
        self.assertEqual(test_objects.get_list_item(1).name,'Test2')
        self.assertEqual(test_objects.get_list()[2].name,'Test3')
        self.assertEqual(test_objects.get_list_item(2).name,'Test3')


    def test_objects_remove(self):
        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects.add_new(test_object3)
        self.assertEqual(len(test_objects.get_all()),3)
        
        test_objects.remove(test_object2)
        self.assertEqual(len(test_objects.get_all()),2)
        self.assertEqual(test_objects.get_all()[1].name,'Test3')

    def test_objects_equals(self):
        test_objects2 = Archtype.Archtypes()

        test_objects.add_new(test_object1)
        test_objects.add_new(test_object2)
        test_objects2.add_new(test_object1)
        test_objects2.add_new(test_object2)

        self.assertTrue(test_objects.equals(test_objects2))

    def test_objects_notequals(self):
        test_objects2 = Archtype.Archtypes()
        
        test_objects1.add_new(test_object1)
        test_objects1.add_new(test_object2)
        test_objects2.add_new(test_object1)
        test_objects2.add_new(test_object2)
        test_objects2.add_new(test_object3)
        
        self.assertFalse(test_objects1.equals(test_objects2))

    def test_objects_clone(self):
        test_objects1.add_new(test_object1)
        test_objects1.add_new(test_object2)
        test_objects2 = test_objects1.clone()

        self.assertTrue(test_objects1.equals(test_objects2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
