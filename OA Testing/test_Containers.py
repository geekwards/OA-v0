import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Container
import test__data

class test_Containers(unittest.TestCase):
    def test_container_create_and_isempty(self):
        test_containers = Container.Containers()
        self.assertTrue(test_containers.isempty())

    def test_container_add_and_get_and_len(self):
        self.assertEqual(len(test__data.test_containers),3)
        self.assertEqual(test__data.test_containers.get_item('test1').short_description,'testdesc1')
        self.assertEqual(test__data.test_containers.get_item('test3').short_description,'testdesc3')

    def test_container_get_list(self):
        self.assertEqual(len(test__data.test_containers),3)
        self.assertEqual(test__data.test_containers.list_of_items[0].name,'test1')
        self.assertEqual(test__data.test_containers.list_of_items[1].name,'test1')

    def test_container_update(self):
        self.assertEqual(len(test__data.test_containers),2)
        self.assertEqual(test__data.test_containers.all_items[0].name,'test1')
        self.assertEqual(test__data.test_containers.all_items[1].name,'test3')
        test__data.test_containers.update(test__data.test_base_equip3)
        self.assertEqual(test__data.test_containers.list_of_items[1].short_description,'testdesc3')
        self.assertEqual(test__data.test_containers.all_items[1].short_description,'testdesc3')

    def test_container_update_new(self):
        self.assertEqual(len(test__data.test_containers),2)
        self.assertEqual(test__data.test_containers.all_items[0].name,'test1')
        self.assertEqual(test__data.test_containers.all_items[1].name,'test3')
        test__data.test_containers.update(test__data.test_base_equip3)
        self.assertEqual(test__data.test_containers.list_of_items[1].name,'test3')
        self.assertEqual(test__data.test_containers.all_items[1].name,'test3')

    def test_container_remove(self):
        self.assertEqual(len(test__data.test_containers),3)
        test__data.test_containers.remove(test__data.test_base_equip2)
        self.assertEqual(len(test__data.test_containers),2)
        self.assertEqual(test__data.test_containers.all_items[1].name,'test3')

    def test_container_equals(self):
        self.assertTrue(test__data.test_containers == test__data.test_base_equipment2)

    def test_container_notequals(self):
        self.assertFalse(test__data.test_containers == test__data.test_base_equipment3)

    def test_container_clone(self):
        clone = test__data.test_containers.clone()
        self.assertTrue(test__data.test_containers == clone)
        clone.get_item('test1').short_description = 'modified short descr'
        self.assertFalse(test__data.test_containers == clone)

if __name__ == '__main__':
    unittest.main(verbosity=2)
