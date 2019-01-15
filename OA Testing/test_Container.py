import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Container
import test__data

class test_Container(unittest.TestCase):
    def test_container_create(self):
        test_container = Container.Container('','')
        self.assertTrue(test_container.isempty())

    def test_container_equal(self):
        self.assertTrue(test__data.test_container1 == test__data.test_container2)

    def test_container_inequality(self):
        self.assertFalse(test__data.test_container1 == test__data.test_container3)

    def test_container_clone(self):
        clone = test__data.test_container1.clone()
        self.assertTrue(test__data.test_container1 == clone)
        clone.short_description = 'modified short desc'
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality2(self):
        clone = test__data.test_container1.clone()
        clone.name = 'changed name'
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality3(self):
        clone = test__data.test_container1.clone()
        clone.short_description = 'changed shortdesc'
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality4(self):
        clone = test__data.test_container1.clone()
        clone.description = 'changed desc'
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality5(self):
        clone = test__data.test_container1.clone()
        clone.value = 10
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality6(self):
        clone = test__data.test_container1.clone()
        clone.weight = 15
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality7(self):
        clone = test__data.test_container1.clone()
        clone.health = 20
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality8(self):
        clone = test__data.test_container1.clone()
        clone.capacity = 25
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_inequality9(self):
        clone = test__data.test_container1.clone()
        clone.special = 'changed spec'
        self.assertFalse(test__data.test_container1 == clone)

    def test_container_isempty_not(self):
        self.assertFalse(test__data.test_container1.isempty())

    def test_container_isempty(self):
        self.assertTrue(test__data.test_container_empty.isempty())

if __name__ == '__main__':
    unittest.main(verbosity=2)
