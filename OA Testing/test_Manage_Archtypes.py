import unittest

import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Archtypes

class test_Manage_Archtypes(unittest.TestCase):

    def test_load_archtypes(self):

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        loaded = Manage_Archtypes.get_loaded_set()

        self.assertTrue(len(loaded.get_all())>0)

    def test_save_archtype(self):

        Manage_Archtypes.load_archtypes(app_config.test_file_path + app_config.test_filename)
        loaded = Manage_Archtypes.get_loaded_set()
        num_Arch = len(loaded.get_all())

        self.assertEqual(loaded[1].name,'Test2')
        clone = loaded[1].clone()

        clone.short_description = 'MODIFIED TEST'
        Manage_Archtypes.save_archtype(1,clone)
        loaded2 = Manage_Archtypes.get_loaded_set()

        self.assertEqual(loaded[1].name,loaded2[1].name)
        self.assertNotEqual(loaded[1].short_description,loaded2[1].short_description)
        self.assertEqual(len(loaded.get_all()),num_Arch)


if __name__ == '__main__':
    unittest.main(verbosity=2)
