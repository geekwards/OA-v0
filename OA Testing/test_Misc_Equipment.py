import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Misc_Equipment
import test__data

class test_Misc_Equipment(unittest.TestCase):
    def test_add(self):
        self.assertEqual(test__data.test_miscequipment1.list_of_items,test__data.test_miscequipment1_listofitems_add)
        self.assertEqual(test__data.test_miscequipment1.all_items,test__data.test_miscequipment1_allitems_add)

    def test_add_neg(self):
        clone = test__data.test_miscequipment1.clone()
        try:
            clone.add_new(test__data.test_weapon1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')

    def test_add_empty(self):
        clone = test__data.test_miscequipment1.clone()
        try:
            clone.add_new(test__data.test_miscequip_empty)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')

    def test_remove(self):
        clone = test__data.test_miscequipment1.clone()
        self.assertEqual(len(clone),3)
        clone.add_new(test__data.test_miscequip4)
        self.assertEqual(len(clone),4)
        clone.remove(test__data.test_miscequip3)
        self.assertEqual(len(clone),3)
        self.assertEqual(clone.list_of_items,test__data.test_miscequipment1_listofitems_remove)
        self.assertEqual(clone.all_items,test__data.test_miscequipment1_allitems_remove)

    def test_remove_dne(self):
        clone = test__data.test_miscequipment1.clone()
        self.assertEqual(len(clone),3)
        try:
            clone.remove(test__data.test_miscequip4)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')

    def test_clone(self):
        clone = test__data.test_miscequipment1.clone()
        self.assertEqual(clone,test__data.test_miscequipment1)

    def test_isempty(self):
        self.assertEqual(len(test__data.test_miscequipment_empty),0)
        self.assertTrue(test__data.test_miscequipment_empty.isempty())
        clone = test__data.test_miscequipment_empty.clone()
        clone.add_new(test__data.test_miscequip1)
        self.assertFalse(clone.isempty())

    def test_update(self):
        clone = test__data.test_miscequipment1.clone()
        self.assertTrue(len(clone),3)
        self.assertTrue(clone.get_item('test1').special,'spec1')
        clone.update(test__data.test_miscequip1c)
        self.assertTrue(len(clone),3)
        self.assertTrue(clone.get_item('test1').special,'MODIFIED')

    def test_update_DNE(self):
        clone = test__data.test_miscequipment1.clone()
        self.assertTrue(len(clone),3)
        self.assertTrue(clone.get_item('test1').special,'spec1')
        clone.update(test__data.test_miscequip4)
        self.assertTrue(len(clone),4)
        self.assertTrue(clone.get_item('test4').special,'spec4')

    def test_get_item_DNE(self):
        self.assertTrue(len(test__data.test_miscequipment1),3)
        value = test__data.test_miscequipment1.get_item('test4')
        self.assertTrue(value,None)

    def test_equal_diff_obj(self):
        try:
            self.assertFalse(test__data.test_miscequipment1 == test__data.test_weapons1)
        except ValueError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised:' + str(e))
        else:
            self.fail('ExpectedException not raised')

if __name__ == '__main__':
    unittest.main(verbosity=2)
