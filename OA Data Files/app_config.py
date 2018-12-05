from time import gmtime, strftime
import sys, os.path
datapath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Data Files')
adminpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA ADMIN')
guipath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA GUI')
objectpath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..") + '/OA Objects')

sys.path.append(adminpath)
sys.path.append(guipath)
sys.path.append(objectpath)
sys.path.append(datapath)


filepath = datapath
filename = "Archtypes.dat"
backup_filepath = datapath
backup_filename = "ArchtypesBackup" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
