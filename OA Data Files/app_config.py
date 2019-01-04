from time import gmtime, strftime
import sys, os.path
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
gui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA GUI')
object_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Objects')
admin_archtypes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Archtypes')
admin_races_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Races')
admin_misc_list_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Misc Lists')
admin_foci_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Foci')

sys.path.append(gui_path)
sys.path.append(object_path)
sys.path.append(data_path)
sys.path.append(admin_archtypes_path)
sys.path.append(admin_races_path)
sys.path.append(admin_misc_list_path)
sys.path.append(admin_foci_path)

file_path = data_path
backup_file_path = data_path
archtype_filename = "/Archtypes.dat"
backup_archtype_filename = "/ArchtypesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
race_filename = "/Races.dat"
backup_race_filename = "/RacesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
misc_list_filename = "/MiscLists.dat"
backup_misc_list_filename = "/MiscListsBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"
focus_filename = "/Foci.dat"
backup_focus_filename = "/FociBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".dat"

test_file_path = data_path + '/test_data'
test_backup_file_path = data_path + '/test_data'
test_archive_filename = "/Archtypes_test.dat"
test_backup_archive_filename = "/ArchtypesBackup_test.dat"
test_race_filename = "/Races_test.dat"
test_backup_race_filename = "/RacesBackup_test.dat"
test_misc_list_filename = "/MiscLists_test.dat"
test_backup_misc_list_filename = "/MiscListsBackup_test.dat"
test_race_filename = "/Foci_test.dat"
test_backup_race_filename = "/FociBackup_test.dat"

title_font = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
    " -underline 0 -overstrike 0"
