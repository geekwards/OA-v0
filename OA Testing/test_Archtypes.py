import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype

class test_Archtypes(unittest.TestCase):

    def test_archtypes_create_and_isempty(self):
        test_archtypes = Archtype.Archtypes()

        self.assertTrue(test_archtypes.isempty())

    def test_archtypes_add_and_get_and_len(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)

        self.assertEqual(len(test_archtypes),2)
        self.assertEqual(test_archtypes.get_archtype('Test1').short_description,'TestDesc1')
        self.assertEqual(test_archtypes.get_archtype('Test2').short_description,'TestDesc2')

    def test_archtypes_get_list(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)

        self.assertEqual(len(test_archtypes),2)
        self.assertEqual(test_archtypes.list_of_archtypes[0].name,'Test1')
        self.assertEqual(test_archtypes.list_of_archtypes[1].name,'Test2')

    def test_archtypes_update(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test2','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        self.assertEqual(len(test_archtypes),2)
        self.assertEqual(test_archtypes.all_archtypes[0].name,'Test1')
        self.assertEqual(test_archtypes.all_archtypes[1].name,'Test2')

        test_archtypes.update(test_archtype3)
        self.assertEqual(test_archtypes.list_of_archtypes[1].short_description,'TestDesc3')
        self.assertEqual(test_archtypes.all_archtypes[1].short_description,'TestDesc3')

    def test_archtypes_update_new(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        self.assertEqual(len(test_archtypes),2)
        self.assertEqual(test_archtypes.all_archtypes[0].name,'Test1')
        self.assertEqual(test_archtypes.all_archtypes[1].name,'Test2')

        test_archtypes.update(test_archtype3)
        self.assertEqual(test_archtypes.list_of_archtypes[1].name,'Test2')
        self.assertEqual(test_archtypes.all_archtypes[1].name,'Test2')
        self.assertEqual(test_archtypes.list_of_archtypes[2].name,'Test3')
        self.assertEqual(test_archtypes.all_archtypes[2].name,'Test3')

    def test_archtypes_remove(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        test_archtypes.add_new(test_archtype3)

        self.assertEqual(len(test_archtypes),3)
        test_archtypes.remove(test_archtype2)
        self.assertEqual(len(test_archtypes),2)
        self.assertEqual(test_archtypes.all_archtypes[1].name,'Test3')

    def test_archtypes_equals(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtypes2 = Archtype.Archtypes()

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype1)
        test_archtypes2.add_new(test_archtype2)

        self.assertTrue(test_archtypes.equals(test_archtypes2))

    def test_archtypes_notequals(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')
        test_archtypes2 = Archtype.Archtypes()
        test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype1)
        test_archtypes2.add_new(test_archtype2)
        test_archtypes2.add_new(test_archtype3)

        self.assertFalse(test_archtypes.equals(test_archtypes2))

    def test_archtypes_clone(self):
        test_archtypes = Archtype.Archtypes()
        test_archtype1 = Archtype.Archtype('Test1','TestDesc1')
        test_archtype2 = Archtype.Archtype('Test2','TestDesc2')

        test_archtypes.add_new(test_archtype1)
        test_archtypes.add_new(test_archtype2)
        test_archtypes2 = test_archtypes.clone()
        self.assertTrue(test_archtypes.equals(test_archtypes2))

        test_archtypes2.get_archtype('Test2').short_description = 'modified short descr'
        self.assertFalse(test_archtypes.equals(test_archtypes2))



if __name__ == '__main__':
    unittest.main(verbosity=2)
