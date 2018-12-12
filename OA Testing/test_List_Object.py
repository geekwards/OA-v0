import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import List_Object

class test_List_Object(unittest.TestCase):

    def test_create_list_object(self):
        test_object = List_Object.Listobject('Testing','Test description')

        self.assertEqual(test_object.name,'Testing')
        self.assertEqual(test_object.short_description,'Test description')

if __name__ == '__main__':
    unittest.main(verbosity=2)
