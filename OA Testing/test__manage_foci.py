import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config
import Manage_Foci
 
class Manage_data(Manage_Foci.Manage_foci):
    def get_language_data(self):
        langlist = []
        self.load_combo_data(app_config.test_file_path + app_config.test_lookups_misc_filename)
        for lang in self.languages.all_items:
            langlist.append(lang.name)
        return langlist
