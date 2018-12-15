from time import gmtime, strftime
import sys, os.path
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
gui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA GUI')
object_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Objects')
admin_archtypes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Archtypes')
admin_races_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Races')
admin_misc_list_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Misc Lists')

sys.path.append(gui_path)
sys.path.append(object_path)
sys.path.append(data_path)
sys.path.append(admin_archtypes_path)
sys.path.append(admin_races_path)
sys.path.append(admin_misc_list_path)

file_path = data_path
backup_file_path = data_path
archive_filename = "/Archtypes.dat"
backup_archive_filename = "/ArchtypesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
race_filename = "/Races.dat"
backup_race_filename = "/RacesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
race_filename = "/MiscLists.dat"
backup_race_filename = "/MiscListsBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"

test_file_path = data_path + '/test_data'
test_backup_file_path = data_path + '/test_data'
test_archive_filename = "/Archtypes_test.dat"
test_backup_archive_filename = "/ArchtypesBackup_test.dat"
test_race_filename = "/Archtypes_test.dat"
test_backup_race_filename = "/ArchtypesBackup_test.dat"
test_race_filename = "/MiscLists_test.dat"
test_backup_race_filename = "/MiscListsBackup_test.dat"

title_font = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
    " -underline 0 -overstrike 0"
