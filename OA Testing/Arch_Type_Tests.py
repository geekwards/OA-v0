import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Archtype

class Arch_Type_Tests(unittest.TestCase):

    def test_archtype_empty(self):
        test_archtype = Archtype.Archtype('','')

        self.assertTrue(test_archtype.empty())

    def test_archtype_equal(self):
        test_archtype = Archtype.Archtype('test','testdesc')
        test_archtype2 = Archtype.Archtype('test','testdesc')

        self.assertTrue(test_archtype.equals(test_archtype2))

    def test_archtype_clone(self):
        test_archtype = Archtype.Archtype('test','testdesc')
        test_archtype2 = test_archtype.clone()

        self.assertTrue(test_archtype.equals(test_archtype2))

if __name__ == '__main__':
    unittest.main(verbosity=2)
