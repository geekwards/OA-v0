import Archtype
import List_Object
import Misc_List
import Race

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

#List_Object
test_object1 = List_Object.List_object('Testing','Test description')

test_object2 = List_Object.List_object('Testing','Test description')

#Misc_List
test_misc_list1 = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
test_misc_list1b = Misc_List.Misc_list('Test1',['Testlist 1.1','Testlist 1.2','Testlist 1.3'])
test_misc_list2 = Misc_List.Misc_list('Test2',['Testlist 2.1','Testlist 2.2','Testlist 2.3'])

#Misc_Lists
test_misc_lists1 = Misc_List.Misc_lists()
test_misc_list2b = Misc_List.Misc_list('Test2',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])
test_misc_list3 = Misc_List.Misc_list('Test3',['Testlist 3.1','Testlist 3.2','Testlist 3.3'])

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
test_race1.foci = 'foci'
test_race1.feats = 'feats'
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
test_race1.languages_bonus = 10

test_race2 = Race.Race('test')
test_race2.short_description = 'test short descr'
test_race2.description = 'This is a test description.'
test_race2.size = 'size'
test_race2.body = 'body'
test_race2.foci = 'foci'
test_race2.feats = 'feats'
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
test_race2.languages_bonus = 10

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

