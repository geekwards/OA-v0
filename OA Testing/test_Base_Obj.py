import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Base_Object
import test__data

class test_Base_Object(unittest.TestCase):
    def test_clone(self):
        clone = test__data.test_base_obj1.clone()
        self.assertEqual(clone,test__data.test_base_obj1)

    def test_isempty(self):
        self.assertTrue(test__data.test_base_obj_empty.isempty())
        clone = test__data.test_base_obj_empty.clone()
        clone.name = 'Modified'
        clone.short_description = 'Modified'
        self.assertFalse(clone.isempty())

    def test_equals(self):
        self.assertTrue(test__data.test_base_obj1 == test__data.test_base_obj1b)
        self.assertFalse(test__data.test_base_obj1 == test__data.test_base_obj2)

    def test_equal_bad_data(self):
        try:
            self.assertFalse(test__data.test_base_obj1 == test__data.test_weapon1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')

if __name__ == '__main__':
    unittest.main(verbosity=2)
