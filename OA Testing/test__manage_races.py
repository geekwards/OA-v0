import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Races

class Manage_data(Manage_Races.Manage_races):
    def get_language_data(self):
        langlist = []
        for lang in self.languages.all_items:
            langlist.append(lang.name)
        return langlist

    def get_sizes_data(self):
        return self.sizes

    def get_bodies_data(self):
        return self.bodies

    def get_foci_data(self):
        focilist = []
        for focus in self.foci:
            focilist.append(focus.name)
        return focilist

    def get_feats_data(self):
        featlist = []
        for feat in self.feats.all_items:
            featlist.append(feat.name)
        return featlist
  
    def __init__(self):
        self.load_combo_data(app_config.test_file_path + app_config.test_lookups_misc_filename,app_config.test_file_path + app_config.test_lookups_foci_filename)
        super().__init__()