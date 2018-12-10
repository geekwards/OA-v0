from time import gmtime, strftime
import sys, os.path
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
admin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN')
gui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA GUI')
object_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Objects')

sys.path.append(admin_path)
sys.path.append(gui_path)
sys.path.append(object_path)
sys.path.append(data_path)

file_path = data_path
filename = "/Archtypes.dat"
backup_file_path = data_path
backup_filename = "/ArchtypesBackup" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"

title_font = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
    " -underline 0 -overstrike 0"
