from time import gmtime, strftime
import sys, os.path
data_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Data Files')
gui_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA GUI')
object_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA Objects')
admin_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN')
admin_archtypes_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Archtypes')
admin_races_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Races')
admin_misc_list_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Misc Lists')
admin_foci_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Foci')
admin_equip_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..") + '/OA ADMIN/Equipment')

sys.path.append(gui_path)
sys.path.append(object_path)
sys.path.append(data_path)
sys.path.append(admin_path)
sys.path.append(admin_archtypes_path)
sys.path.append(admin_races_path)
sys.path.append(admin_misc_list_path)
sys.path.append(admin_foci_path)
sys.path.append(admin_equip_path)

file_path = data_path
backup_file_path = data_path
archtype_filename = "/Archtypes.xml"
backup_archtype_filename = "/ArchtypesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
armor_filename = "/Armor.xml"
backup_armor_filename = "/ArmorBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
clothing_filename = "/Clothing.xml"
backup_clothing_filename = "/ClothingBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
container_filename = "/Containers.xml"
backup_container_filename = "/ContainersBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
focus_filename = "/Foci.xml"
backup_focus_filename = "/FociBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
food_filename = "/Food.xml"
backup_food_filename = "/FoodBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
misc_equip_filename = "/MiscEquipment.xml"
backup_misc_equip_filename = "/MiscEquipmentBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
misc_list_filename = "/MiscLists.xml"
backup_misc_list_filename = "/MiscListsBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
money_filename = "/Money.xml"
backup_money_filename = "/MoneyBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
people_filename = "/People.xml"
backup_people_filename = "/PeopleBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
race_filename = "/Races.xml"
backup_race_filename = "/RacesBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"
weapon_filename = "/Weapons.xml"
backup_weapon_filename = "/WeaponsBackup_" + strftime("%Y%m%d%H%M%S", gmtime()) + ".xml"

test_file_path = data_path + '/test_data'
test_backup_file_path = data_path + '/test_data'
test_archive_filename = "/Archtypes_test.xml"
test_backup_archive_filename = "/ArchtypesBackup_test.xml"
test_race_filename = "/Races_test.xml"
test_backup_race_filename = "/RacesBackup_test.xml"
test_misc_list_filename = "/MiscLists_test.xml"
test_backup_misc_list_filename = "/MiscListsBackup_test.xml"
test_armor_filename = "/Armor_test.xml"
test_backup_armor_filename = "/ArmorBackup_test.xml"
test_clothing_filename = "/Clothing_test.xml"
test_backup_clothing_filename = "/ClothingBackup_test.xml"
test_container_filename = "/Containers_test.xml"
test_backup_container_filename = "/ContainersBackup_test.xml"
test_equipmenttype_filename = "/Equipment_Types_test.xml"
test_backup_equipmenttype_filename = "/Equipment_TypesBackup_test.xml"
test_foci_filename = "/Foci_test.xml"
test_backup_foci_filename = "/FociBackup_test.xml"
test_food_filename = "/Food_test.xml"
test_backup_food_filename = "/FoodBackup_test.xml"
test_misc_equip_filename = "/MiscEquipment_test.xml"
test_backup_misc_equip_filename = "/MiscEquipmentBackup_test.xml"
test_money_filename = "/Money_test.xml"
test_backup_money_filename = "/MoneyBackup_test.xml"
test_weapons_filename = "/Weapons_test.xml"
test_backup_weapons_filename = "/WeaponsBackup_test.xml"
test_lookups_misc_filename = '/lookups_misc_test.xml'
test_lookups_foci_filename = '/lookups_foci_test.xml'

title_font = "-family {Segoe UI} -size 20 -weight bold -slant roman"  \
    " -underline 0 -overstrike 0"
