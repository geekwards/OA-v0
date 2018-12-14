import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype

class test_Archtypes(unittest.TestCase):

    def test_archtypes_create(self):
        test_archtypes = Archtype.Archtypes()

        self.assertTrue(test_archtypes.isempty())

    def test_archtypes_add_and_get(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)

        self.assertEqual(len(test_archtypes.get_all()),2)
        self.assertEqual(test_archtypes[0].name,'Test1')
        self.assertEqual(test_archtypes[1].name,'Test2')
        self.assertEqual(test_archtypes.get_all()[0].name,'Test1')
        self.assertEqual(test_archtypes.get_all()[1].name,'Test2')

    def test_archtypes_get_list(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)

        self.assertEqual(len(test_archtypes.get_list()),2)
        self.assertEqual(test_archtypes.get_list()[0].name,'Test1')
        self.assertEqual(test_archtypes.get_list()[1].name,'Test2')

    def test_archtypes_get_list_item(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)

        self.assertEqual(len(test_archtypes.get_list()),2)
        self.assertEqual(test_archtypes.get_list_item(0).name,'Test1')
        self.assertEqual(test_archtypes.get_list_item(1).name,'Test2')

    def test_archtypes_get_list_item(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        self.assertEqual(len(test_archtypes.get_list()),2)
        self.assertEqual(test_archtypes.get_list_item(0).name,'Test1')
        self.assertEqual(test_archtypes.get_list_item(1).name,'Test2')

        test_archtypes.update(1,test_archtype3)
        self.assertEqual(test_archtypes.get_list()[1].name,'Test3')
        self.assertEqual(test_archtypes.get_list_item(1).name,'Test3')

    def test_archtypes_get_list_item_fail(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        self.assertEqual(len(test_archtypes.get_list()),2)
        self.assertEqual(test_archtypes.get_list_item(0).name,'Test1')
        self.assertEqual(test_archtypes.get_list_item(1).name,'Test2')

        test_archtypes.update(2,test_archtype3)
        self.assertEqual(test_archtypes.get_list()[1].name,'Test2')
        self.assertEqual(test_archtypes.get_list_item(1).name,'Test2')
        self.assertEqual(test_archtypes.get_list()[2].name,'Test3')
        self.assertEqual(test_archtypes.get_list_item(2).name,'Test3')


    def test_archtypes_remove(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        test_archtypes.add_new(test_archtype3)

        self.assertEqual(len(test_archtypes.get_all()),3)
        test_archtypes.remove(test_archtype2)
        self.assertEqual(len(test_archtypes.get_all()),2)
        self.assertEqual(test_archtypes.get_all()[1].name,'Test3')

    def test_archtypes_equals(self):
        test_archtypes1 = Archtype.Archtypes()
        test_archtypes2 = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes1.add_new(test_archtype1)
        test_archtypes1.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype1)
        test_archtypes2.add_new(test_archtype2)

        self.assertTrue(test_archtypes1.equals(test_archtypes2))

    def test_archtypes_notequals(self):
        test_archtypes1 = Archtype.Archtypes()
        test_archtypes2 = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes1.add_new(test_archtype1)
        test_archtypes1.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype1)
        test_archtypes2.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype3)

        self.assertFalse(test_archtypes1.equals(test_archtypes2))

    def test_archtypes_clone(self):
        test_archtypes1 = Archtype.Archtypes()
        test_archtypes2 = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes1.add_new(test_archtype1)
        test_archtypes1.add_new(test_archtype2)
        test_archtypes2 = test_archtypes1.clone()

        self.assertTrue(test_archtypes1.equals(test_archtypes2))

if __name__ == '__main__':
    unittest.main(verbosity=2)