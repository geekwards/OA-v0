import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
sys.path.append(datapath)

import app_config

import Base_Manage_Data

class Manage_data(Base_Manage_Data.Manage_data):
    def load_set2(self,data):
        self.current_set = data   
        self.loaded_set = self.current_set.clone()