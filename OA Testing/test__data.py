import Archtype
import List_Object
import Misc_List
import Race
import Base_Object
import Armor
import Clothing
import Container
import Focus
import Food
import Misc_Equipment

#Base_Object
test_base_obj1 = Base_Object.Item('test1','testdesc1')
test_base_obj2 = Base_Object.Item('test1','testdesc1')
test_base_obj3 = Base_Object.Item('test3','testdesc3')
test_base_obj4 = Base_Object.Item('test4','testdesc4')
test_base_obj_empty = Base_Object.Item('','')

#Base_Object_Set
test_base_obj_set = Base_Object.Set_of_Items()
test_base_obj_set.add_new(test_base_obj1)
test_base_obj_set.add_new(test_base_obj2)
test_base_obj_set.add_new(test_base_obj3)

test_base_obj_set2 = Base_Object.Set_of_Items()
test_base_obj_set2.add_new(test_base_obj1)
test_base_obj_set2.add_new(test_base_obj2)
test_base_obj_set2.add_new(test_base_obj3)

test_base_obj_set3 = Base_Object.Set_of_Items()
test_base_obj_set3.add_new(test_base_obj3)
test_base_obj_set3.add_new(test_base_obj4)

#Base_equip
test_base_equip1 = Base_Object.Item('test1','testdesc1')
test_base_equip2 = Base_Object.Item('test1','testdesc1')
test_base_equip3 = Base_Object.Item('test3','testdesc3')
test_base_equip4 = Base_Object.Item('test4','testdesc4')
test_base_equip_empty = Base_Object.Item('','')

#Base_equipment
test_base_equipment = Base_Object.Set_of_Items()
test_base_equipment.add_new(test_base_equip1)
test_base_equipment.add_new(test_base_equip2)
test_base_equipment.add_new(test_base_equip3)

test_base_equipment2 = Base_Object.Set_of_Items()
test_base_equipment2.add_new(test_base_equip1)
test_base_equipment2.add_new(test_base_equip2)
test_base_equipment2.add_new(test_base_equip3)

test_base_equipment3 = Base_Object.Set_of_Items()
test_base_equipment3.add_new(test_base_equip3)
test_base_equipment3.add_new(test_base_equip4)

#Garment
test_garment1 = Clothing.Garment('test1','testdesc1')
test_garment2 = Clothing.Garment('test1','testdesc1')
test_garment3 = Clothing.Garment('test3','testdesc3')
test_garment4 = Clothing.Garment('test4','testdesc4')
test_garment_empty = Clothing.Garment('','')

#Clothing
test_clothing = Clothing.Clothing()
test_clothing.add_new(test_garment1)
test_clothing.add_new(test_garment2)
test_clothing.add_new(test_garment3)

test_clothing2 = Clothing.Clothing()
test_clothing2.add_new(test_garment1)
test_clothing2.add_new(test_garment2)
test_clothing2.add_new(test_garment3)

test_clothing3 = Clothing.Clothing()
test_clothing3.add_new(test_garment3)
test_clothing3.add_new(test_garment4)

#Container
test_container1 = Container.Container('test1','testdesc1')
test_container2 = Container.Container('test1','testdesc1')
test_container3 = Container.Container('test3','testdesc3')
test_container4 = Container.Container('test4','testdesc4')
test_container_empty = Container.Container('','')

#Containers
test_containers = Container.Containers()
test_containers.add_new(test_container1)
test_containers.add_new(test_container2)
test_containers.add_new(test_container3)

test_containers2 = Container.Containers()
test_containers2.add_new(test_container1)
test_containers2.add_new(test_container2)
test_containers2.add_new(test_container3)

test_containers3 = Container.Containers()
test_containers3.add_new(test_container3)
test_containers3.add_new(test_container4)

#Misc Equip
test_misc_equip1 = Misc_Equipment.Stuff('test1','testdesc1')
test_misc_equip2 = Misc_Equipment.Stuff('test1','testdesc1')
test_misc_equip3 = Misc_Equipment.Stuff('test3','testdesc3')
test_misc_equip4 = Misc_Equipment.Stuff('test4','testdesc4')
test_misc_equip_empty = Misc_Equipment.Stuff('','')

#Misc Equipment
test_misc_equipment = Misc_Equipment.Misc_equipment()
test_misc_equipment.add_new(test_misc_equip1)
test_misc_equipment.add_new(test_misc_equip2)
test_misc_equipment.add_new(test_misc_equip3)

test_misc_equipment2 = Misc_Equipment.Misc_equipment()
test_misc_equipment2.add_new(test_misc_equip1)
test_misc_equipment2.add_new(test_misc_equip2)
test_misc_equipment2.add_new(test_misc_equip3)

test_misc_equipment3 = Misc_Equipment.Misc_equipment()
test_misc_equipment3.add_new(test_misc_equip3)
test_misc_equipment3.add_new(test_misc_equip4)

#Food
test_food1 = Food.Food('test1','testdesc1')
test_food2 = Food.Food('test1','testdesc1')
test_food3 = Food.Food('test3','testdesc3')
test_food4 = Food.Food('test4','testdesc4')
test_food_empty = Food.Food('','')

#Foods
test_foods = Food.Foods()
test_foods.add_new(test_food1)
test_foods.add_new(test_food2)
test_foods.add_new(test_food3)

test_foods2 = Food.Foods()
test_foods2.add_new(test_food1)
test_foods2.add_new(test_food2)
test_foods2.add_new(test_food3)

test_foods3 = Food.Foods()
test_foods3.add_new(test_food3)
test_foods3.add_new(test_food4)

#Focus
test_focus1 = Focus.Focus('test1','testdesc1')
test_focus2 = Focus.Focus('test1','testdesc1')
test_focus3 = Focus.Focus('test3','testdesc3')
test_focus4 = Focus.Focus('test4','testdesc4')
test_focus_empty = Focus.Focus('','')

#Foci
test_foci = Focus.Foci()
test_foci.add_new(test_focus1)
test_foci.add_new(test_focus2)
test_foci.add_new(test_focus3)

test_foci2 = Focus.Foci()
test_foci2.add_new(test_focus1)
test_foci2.add_new(test_focus2)
test_foci2.add_new(test_focus3)

test_foci3 = Focus.Foci()
test_foci3.add_new(test_focus3)
test_foci3.add_new(test_focus4)

#Archtype
test_archtype1 = Archtype.Archtype('test','testdesc')
test_archtype1.description = "This is a test description."
test_archtype1.proficiency = "Test proficiency"
test_archtype1.str_bonus = 0
test_archtype1.per_bonus = 1
test_archtype1.int_bonus = 2
test_archtype1.dex_bonus = 3
test_archtype1.cha_bonus = 4
test_archtype1.vit_bonus = 5
test_archtype1.mag_bonus = 6
test_archtype1.stamina_bonus = 7
test_archtype1.attack_bonus = 8
test_archtype1.reflex_bonus = 9
test_archtype1.feats = 10
test_archtype1.movement = 11
test_archtype1.skill_points = 12
test_archtype1.level_health = "more health"

test_archtype2 = Archtype.Archtype('test','testdesc')
test_archtype2.description = "This is a test description."
test_archtype2.proficiency = "Test proficiency"
test_archtype2.str_bonus = 0
test_archtype2.per_bonus = 1
test_archtype2.int_bonus = 2
test_archtype2.dex_bonus = 3
test_archtype2.cha_bonus = 4
test_archtype2.vit_bonus = 5
test_archtype2.mag_bonus = 6
test_archtype2.stamina_bonus = 7
test_archtype2.attack_bonus = 8
test_archtype2.reflex_bonus = 9
test_archtype2.feats = 10
test_archtype2.movement = 11
test_archtype2.skill_points = 12
test_archtype2.level_health = "more health"

test_archtype_empty = Archtype.Archtype('','')

#Archtypes
test_archtypes = Archtype.Archtypes()
test_archtype1b = Archtype.Archtype('Test1','TestDesc1b')
test_archtype2b = Archtype.Archtype('Test2','TestDesc2b')
test_archtype3 = Archtype.Archtype('Test3','TestDesc3')

test_archtypes.add_new(test_archtype1)
test_archtypes.add_new(test_archtype2)
test_archtypes.add_new(test_archtype2b)
test_archtypes.add_new(test_archtype3)

test_archtypes2 = Archtype.Archtypes()

test_archtypes2.add_new(test_archtype1)
test_archtypes2.add_new(test_archtype2)
test_archtypes2.add_new(test_archtype2b)
test_archtypes2.add_new(test_archtype3)

test_archtypes3 = Archtype.Archtypes()

test_archtypes3.add_new(test_archtype1)
test_archtypes3.add_new(test_archtype2)
test_archtypes3.add_new(test_archtype3)

#Armor
test_armor1 = Armor.Armor('test1','testdesc1')
test_armor2 = Armor.Armor('test1','testdesc1')
test_armor3 = Armor.Armor('test3','testdesc3')
test_armor4 = Armor.Armor('test4','testdesc4')
test_armor_empty = Armor.Armor('','')

#Armors
test_armors = Armor.Armors()
test_armors.add_new(test_armor1)
test_armors.add_new(test_armor2)
test_armors.add_new(test_armor3)

test_armors2 = Armor.Armors()
test_armors2.add_new(test_armor1)
test_armors2.add_new(test_armor2)
test_armors2.add_new(test_armor3)

test_armors3 = Armor.Armors()
test_armors3.add_new(test_armor3)
test_armors3.add_new(test_armor4)

#List_Object
test_object1 = List_Object.List_object('Testing','Test description')

test_object2 = List_Object.List_object('Testing','Test description')

#Misc_List
test_misc_list1 = Misc_List.Misc_list('Test1','desc1',[List_Object.List_object('Testlist 1.1',''),List_Object.List_object('Testlist 1.2',''),List_Object.List_object('Testlist 1.3','')])
test_misc_list1b = Misc_List.Misc_list('Test1','desc1',[List_Object.List_object('Testlist 1.1',''),List_Object.List_object('Testlist 1.2',''),List_Object.List_object('Testlist 1.3','')])
test_misc_list2 = Misc_List.Misc_list('Test2','desc2',[List_Object.List_object('Testlist 2.1',''),List_Object.List_object('Testlist 2.2',''),List_Object.List_object('Testlist 2.3','')])

#Misc_Lists
test_misc_lists1 = Misc_List.Misc_lists()
test_misc_list2b = Misc_List.Misc_list('Test2','desc2',[List_Object.List_object('Testlist 3.1',''),List_Object.List_object('Testlist 3.2',''),List_Object.List_object('Testlist 3.3','')])
test_misc_list3 = Misc_List.Misc_list('Test3','desc3',[List_Object.List_object('Testlist 3.1',''),List_Object.List_object('Testlist 3.2',''),List_Object.List_object('Testlist 3.3','')])

test_misc_lists1.add_new(test_misc_list1)
test_misc_lists1.add_new(test_misc_list2)
test_misc_lists1.add_new(test_misc_list2b)
test_misc_lists1.add_new(test_misc_list3)

test_misc_lists2 = Misc_List.Misc_lists()

test_misc_lists2.add_new(test_misc_list1)
test_misc_lists2.add_new(test_misc_list2)
test_misc_lists2.add_new(test_misc_list2b)
test_misc_lists2.add_new(test_misc_list3)

test_misc_lists3 = Misc_List.Misc_lists()

test_misc_lists3.add_new(test_misc_list1)
test_misc_lists3.add_new(test_misc_list2)
test_misc_lists3.add_new(test_misc_list3)

#Race
test_race1 = Race.Race('test')
test_race1.short_description = 'test short descr'
test_race1.description = 'This is a test description.'
test_race1.size = 'size'
test_race1.body = 'body'
test_race1.foci.append(List_Object.List_object('foci1','focidesc1'))
test_race1.foci.append(List_Object.List_object('foci2','focidesc2'))
test_race1.feats.append(List_Object.List_object('feat1','featdesc1'))
test_race1.feats.append(List_Object.List_object('feat2','featdesc2'))
test_race1.str_bonus = 0
test_race1.per_bonus = 1
test_race1.int_bonus = 2
test_race1.dex_bonus = 3
test_race1.cha_bonus = 4
test_race1.vit_bonus = 5
test_race1.mag_bonus = 6
test_race1.will_bonus = 7
test_race1.fortitude_bonus = 8
test_race1.reflex_bonus = 9
test_race1.languages_bonus.append(List_Object.List_object('testlang1','+5'))
test_race1.languages_bonus.append(List_Object.List_object('testlang2','+3'))

test_race2 = Race.Race('test')
test_race2.short_description = 'test short descr'
test_race2.description = 'This is a test description.'
test_race2.size = 'size'
test_race2.body = 'body'
test_race2.foci.append(List_Object.List_object('foci1','focidesc1'))
test_race2.foci.append(List_Object.List_object('foci2','focidesc2'))
test_race2.feats.append(List_Object.List_object('feat1','featdesc1'))
test_race2.feats.append(List_Object.List_object('feat2','featdesc2'))
test_race2.str_bonus = 0
test_race2.per_bonus = 1
test_race2.int_bonus = 2
test_race2.dex_bonus = 3
test_race2.cha_bonus = 4
test_race2.vit_bonus = 5
test_race2.mag_bonus = 6
test_race2.will_bonus = 7
test_race2.fortitude_bonus = 8
test_race2.reflex_bonus = 9
test_race2.languages_bonus.append(List_Object.List_object('testlang1','+5'))
test_race2.languages_bonus.append(List_Object.List_object('testlang2','+3'))

test_race_empty = Race.Race('')

#Races
test_races = Race.Races()
test_race2b = Race.Race('Test2','TestDesc2')
test_race3 = Race.Race('Test3','TestDesc3')

test_races.add_new(test_race1)
test_races.add_new(test_race2)
test_races.add_new(test_race2b)
test_races.add_new(test_race3)

test_races2 = Race.Races()

test_races2.add_new(test_race1)
test_races2.add_new(test_race2)
test_races2.add_new(test_race2b)
test_races2.add_new(test_race3)

test_races3 = Race.Races()

test_races3.add_new(test_race1)
test_races3.add_new(test_race2)
test_races3.add_new(test_race3)

test_list_item0 = List_Object.List_object('Testing0','TestDesc0')
test_list_item1 = List_Object.List_object('Testing1','TestDesc1')
test_list_item2 = List_Object.List_object('Testing2','TestDesc2')
test_list_item3 = List_Object.List_object('Testing3','TestDesc3')

test_set = [test_list_item0,test_list_item1,test_list_item2,test_list_item3]

