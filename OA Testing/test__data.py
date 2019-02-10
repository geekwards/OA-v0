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
import Money
import Weapon
import Base_Equipment

#Archtype
test_archtype1 = Archtype.Archtype('test1','testshortdesc1')
test_archtype1.description = 'testdesc1'
test_archtype1.proficiency = 'prof1'
test_archtype1.str_bonus = '1.0'
test_archtype1.per_bonus = '1.1'
test_archtype1.int_bonus = '1.2'
test_archtype1.dex_bonus = '1.3'
test_archtype1.cha_bonus = '1.4'
test_archtype1.vit_bonus = '1.5'
test_archtype1.mag_bonus = '1.6'
test_archtype1.stamina_bonus = '1.7'
test_archtype1.attack_bonus = '1.8'
test_archtype1.reflex_bonus = '1.9'
test_archtype1.feats = '1.10'
test_archtype1.movement = '1.11'
test_archtype1.skill_points = '1.12'
test_archtype1.level_health = 'health1'

test_archtype1b = Archtype.Archtype('test1','testshortdesc1')
test_archtype1b.description = 'testdesc1'
test_archtype1b.proficiency = 'prof1'
test_archtype1b.str_bonus = '1.0'
test_archtype1b.per_bonus = '1.1'
test_archtype1b.int_bonus = '1.2'
test_archtype1b.dex_bonus = '1.3'
test_archtype1b.cha_bonus = '1.4'
test_archtype1b.vit_bonus = '1.5'
test_archtype1b.mag_bonus = '1.6'
test_archtype1b.stamina_bonus = '1.7'
test_archtype1b.attack_bonus = '1.8'
test_archtype1b.reflex_bonus = '1.9'
test_archtype1b.feats = '1.10'
test_archtype1b.movement = '1.11'
test_archtype1b.skill_points = '1.12'
test_archtype1b.level_health = 'health1'

test_archtype1c = Archtype.Archtype('test1','testshortdesc1')
test_archtype1c.description = 'testdesc1'
test_archtype1c.proficiency = 'MODIFIED'
test_archtype1c.str_bonus = '1.0'
test_archtype1c.per_bonus = '1.1'
test_archtype1c.int_bonus = '1.2'
test_archtype1c.dex_bonus = '1.3'
test_archtype1c.cha_bonus = '1.4'
test_archtype1c.vit_bonus = '1.5'
test_archtype1c.mag_bonus = '1.6'
test_archtype1c.stamina_bonus = '1.7'
test_archtype1c.attack_bonus = '1.8'
test_archtype1c.reflex_bonus = '1.9'
test_archtype1c.feats = '1.10'
test_archtype1c.movement = '1.11'
test_archtype1c.skill_points = '1.12'
test_archtype1c.level_health = 'health1'

test_archtype2 = Archtype.Archtype('test2','testshortdesc2')
test_archtype2.description = 'testdesc2'
test_archtype2.proficiency = 'prof2'
test_archtype2.str_bonus = '2.0'
test_archtype2.per_bonus = '2.1'
test_archtype2.int_bonus = '2.2'
test_archtype2.dex_bonus = '2.3'
test_archtype2.cha_bonus = '2.4'
test_archtype2.vit_bonus = '2.5'
test_archtype2.mag_bonus = '2.6'
test_archtype2.stamina_bonus = '2.7'
test_archtype2.attack_bonus = '2.8'
test_archtype2.reflex_bonus = '2.9'
test_archtype2.feats = '2.10'
test_archtype2.movement = '2.11'
test_archtype2.skill_points = '2.12'
test_archtype2.level_health = 'health2'

test_archtype3 = Archtype.Archtype('test3','testshortdesc3')
test_archtype3.description = 'testdesc3'
test_archtype3.proficiency = 'prof3'
test_archtype3.str_bonus = '3.0'
test_archtype3.per_bonus = '3.1'
test_archtype3.int_bonus = '3.2'
test_archtype3.dex_bonus = '3.3'
test_archtype3.cha_bonus = '3.4'
test_archtype3.vit_bonus = '3.5'
test_archtype3.mag_bonus = '3.6'
test_archtype3.stamina_bonus = '3.7'
test_archtype3.attack_bonus = '3.8'
test_archtype3.reflex_bonus = '3.9'
test_archtype3.feats = '3.10'
test_archtype3.movement = '3.11'
test_archtype3.skill_points = '3.12'
test_archtype3.level_health = 'health3'

test_archtype4 = Archtype.Archtype('test4','testshortdesc4')
test_archtype4.description = 'testdesc4'
test_archtype4.proficiency = 'prof4'
test_archtype4.str_bonus = '4.0'
test_archtype4.per_bonus = '4.1'
test_archtype4.int_bonus = '4.2'
test_archtype4.dex_bonus = '4.3'
test_archtype4.cha_bonus = '4.4'
test_archtype4.vit_bonus = '4.5'
test_archtype4.mag_bonus = '4.6'
test_archtype4.stamina_bonus = '4.7'
test_archtype4.attack_bonus = '4.8'
test_archtype4.reflex_bonus = '4.9'
test_archtype4.feats = '4.10'
test_archtype4.movement = '4.11'
test_archtype4.skill_points = '4.12'
test_archtype4.level_health = 'health4'

test_archtype_empty = Archtype.Archtype('','')

#Archtypes
test_archtypes1 = Archtype.Archtypes()
test_archtypes1.add_new(test_archtype1)
test_archtypes1.add_new(test_archtype2)
test_archtypes1.add_new(test_archtype3)

test_archtypes2 = Archtype.Archtypes()
test_archtypes2.add_new(test_archtype1)
test_archtypes2.add_new(test_archtype2)
test_archtypes2.add_new(test_archtype3)

test_archtypes3 = Archtype.Archtypes()
test_archtypes3.add_new(test_archtype2)
test_archtypes3.add_new(test_archtype3)
test_archtypes3.add_new(test_archtype4)

test_archtypes4 = Archtype.Archtypes()
test_archtypes4.add_new(test_archtype1)
test_archtypes4.add_new(test_archtype2)
test_archtypes4.add_new(test_archtype3)
test_archtypes4.add_new(test_archtype4)

test_archtypes_empty = Archtype.Archtypes()

test_archtypes1_listofitems_add = [List_Object.List_object(test_archtype1.name,test_archtype1.short_description),List_Object.List_object(test_archtype2.name,test_archtype2.short_description),List_Object.List_object(test_archtype3.name,test_archtype3.short_description)]
test_archtypes1_allitems_add = [test_archtype1,test_archtype2,test_archtype3]

test_archtypes1_listofitems_remove = [List_Object.List_object(test_archtype1.name,test_archtype1.short_description),List_Object.List_object(test_archtype2.name,test_archtype2.short_description),List_Object.List_object(test_archtype4.name,test_archtype4.short_description)]
test_archtypes1_allitems_remove = [test_archtype1,test_archtype2,test_archtype4]


#Armor
test_armor1 = Armor.Armor('test1','testshortdesc1')
test_armor1.description = 'testdesc1'
test_armor1.value = '1.1'
test_armor1.weight = '1.2'
test_armor1.health = '1.3'
test_armor1.capacity = '1.4'
test_armor1.special = 'testspec1'
test_armor1.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_armor1b = Armor.Armor('test1','testshortdesc1')
test_armor1b.description = 'testdesc1'
test_armor1b.value = '1.1'
test_armor1b.weight = '1.2'
test_armor1b.health = '1.3'
test_armor1b.capacity = '1.4'
test_armor1b.special = 'testspec1'
test_armor1b.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_armor1c = Armor.Armor('test1','testshortdesc1')
test_armor1c.description = 'testdesc1'
test_armor1c.value = '1.1'
test_armor1c.weight = '1.2'
test_armor1c.health = '1.3'
test_armor1c.capacity = '1.4'
test_armor1c.special = 'MODIFIED'
test_armor1c.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_armor2 = Armor.Armor('test2','testshortdesc2')
test_armor2.description = 'testdesc2'
test_armor2.value = '2.1'
test_armor2.weight = '2.2'
test_armor2.health = '2.3'
test_armor2.capacity = '2.4'
test_armor2.special = 'testspec2'
test_armor2.damage_types = [List_Object.List_object('dt2.1','dtscore2.1'),List_Object.List_object('dt2.2','dtscore2.2'),List_Object.List_object('dt2.3','dtscore2.3')]

test_armor3 = Armor.Armor('test3','testshortdesc3')
test_armor3.description = 'testdesc3'
test_armor3.value = '3.1'
test_armor3.weight = '3.2'
test_armor3.health = '3.3'
test_armor3.capacity = '3.4'
test_armor3.special = 'testspec3'
test_armor3.damage_types = [List_Object.List_object('dt3.1','dtscore3.1'),List_Object.List_object('dt3.2','dtscore3.2'),List_Object.List_object('dt3.3','dtscore3.3')]

test_armor4 = Armor.Armor('test4','testshortdesc4')
test_armor4.description = 'testdesc4'
test_armor4.value = '4.1'
test_armor4.weight = '4.2'
test_armor4.health = '4.3'
test_armor4.capacity = '4.4'
test_armor4.special = 'testspec4'
test_armor4.damage_types = [List_Object.List_object('dt4.1','dtscore4.1'),List_Object.List_object('dt4.2','dtscore4.2'),List_Object.List_object('dt4.3','dtscore4.3')]

test_armor_empty = Armor.Armor('','')

#Armors
test_armors1 = Armor.Armors()
test_armors1.add_new(test_armor1)
test_armors1.add_new(test_armor2)
test_armors1.add_new(test_armor3)

test_armors2 = Armor.Armors()
test_armors2.add_new(test_armor1)
test_armors2.add_new(test_armor2)
test_armors2.add_new(test_armor3)

test_armors3 = Armor.Armors()
test_armors3.add_new(test_armor2)
test_armors3.add_new(test_armor3)
test_armors3.add_new(test_armor4)

test_armors4 = Armor.Armors()
test_armors4.add_new(test_armor1)
test_armors4.add_new(test_armor2)
test_armors4.add_new(test_armor3)
test_armors4.add_new(test_armor4)

test_armors_empty = Armor.Armors()

test_armors1_listofitems_add = [List_Object.List_object(test_armor1.name,test_armor1.short_description),List_Object.List_object(test_armor2.name,test_armor2.short_description),List_Object.List_object(test_armor3.name,test_armor3.short_description)]
test_armors1_allitems_add = [test_armor1,test_armor2,test_armor3]

test_armors1_listofitems_remove = [List_Object.List_object(test_armor1.name,test_armor1.short_description),List_Object.List_object(test_armor2.name,test_armor2.short_description),List_Object.List_object(test_armor4.name,test_armor4.short_description)]
test_armors1_allitems_remove = [test_armor1,test_armor2,test_armor4]


#Base_equip
test_base_equip1 = Base_Equipment.Equip('test1','testshortdesc1')
test_base_equip1.description = 'testdesc1'
test_base_equip1.value = '1.1'
test_base_equip1.weight = '1.2'
test_base_equip1.health = '1.3'
test_base_equip1.capacity = '1.4'
test_base_equip1.special = 'testspec1'

test_base_equip1b = Base_Equipment.Equip('test1','testshortdesc1')
test_base_equip1b.description = 'testdesc1'
test_base_equip1b.value = '1.1'
test_base_equip1b.weight = '1.2'
test_base_equip1b.health = '1.3'
test_base_equip1b.capacity = '1.4'
test_base_equip1b.special = 'testspec1'

test_base_equip1c = Base_Equipment.Equip('test1','testshortdesc1')
test_base_equip1c.description = 'testdesc1'
test_base_equip1c.value = '1.1'
test_base_equip1c.weight = '1.2'
test_base_equip1c.health = '1.3'
test_base_equip1c.capacity = '1.4'
test_base_equip1c.special = 'MODIFIED'

test_base_equip2 = Base_Equipment.Equip('test2','testshortdesc2')
test_base_equip2.description = 'testdesc2'
test_base_equip2.value = '2.1'
test_base_equip2.weight = '2.2'
test_base_equip2.health = '2.3'
test_base_equip2.capacity = '2.4'
test_base_equip2.special = 'testspec2'

test_base_equip3 = Base_Equipment.Equip('test3','testshortdesc3')
test_base_equip3.description = 'testdesc3'
test_base_equip3.value = '3.1'
test_base_equip3.weight = '3.2'
test_base_equip3.health = '3.3'
test_base_equip3.capacity = '3.4'
test_base_equip3.special = 'testspec3'

test_base_equip4 = Base_Equipment.Equip('test4','testshortdesc4')
test_base_equip4.description = 'testdesc4'
test_base_equip4.value = '4.1'
test_base_equip4.weight = '4.2'
test_base_equip4.health = '4.3'
test_base_equip4.capacity = '4.4'
test_base_equip4.special = 'testspec4'

test_base_equip_empty = Base_Equipment.Equip('','')

#Base_equipment
test_base_equipment1 = Base_Equipment.Base_equipment()
test_base_equipment1.add_new(test_base_equip1)
test_base_equipment1.add_new(test_base_equip2)
test_base_equipment1.add_new(test_base_equip3)

test_base_equipment2 = Base_Equipment.Base_equipment()
test_base_equipment2.add_new(test_base_equip1)
test_base_equipment2.add_new(test_base_equip2)
test_base_equipment2.add_new(test_base_equip3)

test_base_equipment3 = Base_Equipment.Base_equipment()
test_base_equipment3.add_new(test_base_equip2)
test_base_equipment3.add_new(test_base_equip3)
test_base_equipment3.add_new(test_base_equip4)

test_base_equipment_empty = Base_Equipment.Base_equipment()

test_base_equipment1_listofitems_add = [List_Object.List_object(test_base_equip1.name,test_base_equip1.short_description),List_Object.List_object(test_base_equip2.name,test_base_equip2.short_description),List_Object.List_object(test_base_equip3.name,test_base_equip3.short_description)]
test_base_equipment1_allitems_add = [test_base_equip1,test_base_equip2,test_base_equip3]

test_base_equipment1_listofitems_remove = [List_Object.List_object(test_base_equip1.name,test_base_equip1.short_description),List_Object.List_object(test_base_equip2.name,test_base_equip2.short_description),List_Object.List_object(test_base_equip4.name,test_base_equip4.short_description)]
test_base_equipment1_allitems_remove = [test_base_equip1,test_base_equip2,test_base_equip4]


#Base_Object
test_base_obj1 = Base_Object.Item('test1','testshortdesc1')

test_base_obj1b = Base_Object.Item('test1','testshortdesc1')

test_base_obj1c = Base_Object.Item('test1','MODIFIED')

test_base_obj2 = Base_Object.Item('test2','testshortdesc2')

test_base_obj3 = Base_Object.Item('test3','testshortdesc3')

test_base_obj4 = Base_Object.Item('test4','testshortdesc4')

test_base_obj_empty = Base_Object.Item('','')

#Base_Object_Set
test_base_obj_set1 = Base_Object.Set_of_Items()
test_base_obj_set1.add_new(test_base_obj1)
test_base_obj_set1.add_new(test_base_obj2)
test_base_obj_set1.add_new(test_base_obj3)

test_base_obj_set2 = Base_Object.Set_of_Items()
test_base_obj_set2.add_new(test_base_obj1)
test_base_obj_set2.add_new(test_base_obj2)
test_base_obj_set2.add_new(test_base_obj3)

test_base_obj_set3 = Base_Object.Set_of_Items()
test_base_obj_set3.add_new(test_base_obj2)
test_base_obj_set3.add_new(test_base_obj3)
test_base_obj_set3.add_new(test_base_obj4)

test_base_obj_set_empty = Base_Equipment.Base_equipment()

test_base_obj_set1_listofitems_add = [List_Object.List_object(test_base_obj1.name,test_base_obj1.short_description),List_Object.List_object(test_base_obj2.name,test_base_obj2.short_description),List_Object.List_object(test_base_obj3.name,test_base_obj3.short_description)]
test_base_obj_set1_allitems_add = [test_base_obj1,test_base_obj2,test_base_obj3]

test_base_obj_set1_listofitems_remove = [List_Object.List_object(test_base_obj1.name,test_base_obj1.short_description),List_Object.List_object(test_base_obj2.name,test_base_obj2.short_description),List_Object.List_object(test_base_obj4.name,test_base_obj4.short_description)]
test_base_obj_set1_allitems_remove = [test_base_obj1,test_base_obj2,test_base_obj4]


#Garment
test_garment1 = Clothing.Garment('test1','testshortdesc1')
test_garment1.description = 'testdesc1'
test_garment1.value = '1.1'
test_garment1.weight = '1.2'
test_garment1.health = '1.3'
test_garment1.capacity = '1.4'
test_garment1.special = 'testspec1'

test_garment1b = Clothing.Garment('test1','testshortdesc1')
test_garment1b.description = 'testdesc1'
test_garment1b.value = '1.1'
test_garment1b.weight = '1.2'
test_garment1b.health = '1.3'
test_garment1b.capacity = '1.4'
test_garment1b.special = 'testspec1'

test_garment1c = Clothing.Garment('test1','testshortdesc1')
test_garment1c.description = 'testdesc1'
test_garment1c.value = '1.1'
test_garment1c.weight = '1.2'
test_garment1c.health = '1.3'
test_garment1c.capacity = '1.4'
test_garment1c.special = 'MODIFIED'

test_garment2 = Clothing.Garment('test2','testshortdesc2')
test_garment2.description = 'testdesc2'
test_garment2.value = '2.1'
test_garment2.weight = '2.2'
test_garment2.health = '2.3'
test_garment2.capacity = '2.4'
test_garment2.special = 'testspec2'

test_garment3 = Clothing.Garment('test3','testshortdesc3')
test_garment3.description = 'testdesc3'
test_garment3.value = '3.1'
test_garment3.weight = '3.2'
test_garment3.health = '3.3'
test_garment3.capacity = '3.4'
test_garment3.special = 'testspec3'

test_garment4 = Clothing.Garment('test4','testshortdesc4')
test_garment4.description = 'testdesc4'
test_garment4.value = '4.1'
test_garment4.weight = '4.2'
test_garment4.health = '4.3'
test_garment4.capacity = '4.4'
test_garment4.special = 'testspec4'

test_garment_empty = Clothing.Garment('','')

#Clothing
test_clothing1 = Clothing.Clothing()
test_clothing1.add_new(test_garment1)
test_clothing1.add_new(test_garment2)
test_clothing1.add_new(test_garment3)

test_clothing2 = Clothing.Clothing()
test_clothing2.add_new(test_garment1)
test_clothing2.add_new(test_garment2)
test_clothing2.add_new(test_garment3)

test_clothing3 = Clothing.Clothing()
test_clothing3.add_new(test_garment2)
test_clothing3.add_new(test_garment3)
test_clothing3.add_new(test_garment4)

test_clothing4 = Clothing.Clothing()
test_clothing4.add_new(test_garment1)
test_clothing4.add_new(test_garment2)
test_clothing4.add_new(test_garment3)
test_clothing4.add_new(test_garment4)

test_clothing_empty = Clothing.Clothing()

test_clothing1_listofitems_add = [List_Object.List_object(test_garment1.name,test_garment1.short_description),List_Object.List_object(test_garment2.name,test_garment2.short_description),List_Object.List_object(test_garment3.name,test_garment3.short_description)]
test_clothing1_allitems_add = [test_garment1,test_garment2,test_garment3]

test_clothing1_listofitems_remove = [List_Object.List_object(test_garment1.name,test_garment1.short_description),List_Object.List_object(test_garment2.name,test_garment2.short_description),List_Object.List_object(test_garment4.name,test_garment4.short_description)]
test_clothing1_allitems_remove = [test_garment1,test_garment2,test_garment4]


#Container
test_container1 = Container.Container('test1','testshortdesc1')
test_container1.description = 'testdesc1'
test_container1.value = '1.1'
test_container1.weight = '1.2'
test_container1.health = '1.3'
test_container1.capacity = '1.4'
test_container1.special = 'testspec1'

test_container1b = Container.Container('test1','testshortdesc1')
test_container1b.description = 'testdesc1'
test_container1b.value = '1.1'
test_container1b.weight = '1.2'
test_container1b.health = '1.3'
test_container1b.capacity = '1.4'
test_container1b.special = 'testspec1'

test_container1c = Container.Container('test1','testshortdesc1')
test_container1c.description = 'testdesc1'
test_container1c.value = '1.1'
test_container1c.weight = '1.2'
test_container1c.health = '1.3'
test_container1c.capacity = '1.4'
test_container1c.special = 'MODIFIED'

test_container2 = Container.Container('test2','testshortdesc2')
test_container2.description = 'testdesc2'
test_container2.value = '2.1'
test_container2.weight = '2.2'
test_container2.health = '2.3'
test_container2.capacity = '2.4'
test_container2.special = 'testspec2'

test_container3 = Container.Container('test3','testshortdesc3')
test_container3.description = 'testdesc3'
test_container3.value = '3.1'
test_container3.weight = '3.2'
test_container3.health = '3.3'
test_container3.capacity = '3.4'
test_container3.special = 'testspec3'

test_container4 = Container.Container('test4','testshortdesc4')
test_container4.description = 'testdesc4'
test_container4.value = '4.1'
test_container4.weight = '4.2'
test_container4.health = '4.3'
test_container4.capacity = '4.4'
test_container4.special = 'testspec4'

test_container_empty = Container.Container('','')

#Containers
test_containers1 = Container.Containers()
test_containers1.add_new(test_container1)
test_containers1.add_new(test_container2)
test_containers1.add_new(test_container3)

test_containers2 = Container.Containers()
test_containers2.add_new(test_container1)
test_containers2.add_new(test_container2)
test_containers2.add_new(test_container3)

test_containers3 = Container.Containers()
test_containers3.add_new(test_container2)
test_containers3.add_new(test_container3)
test_containers3.add_new(test_container4)

test_containers4 = Container.Containers()
test_containers4.add_new(test_container1)
test_containers4.add_new(test_container2)
test_containers4.add_new(test_container3)
test_containers4.add_new(test_container4)

test_containers_empty = Container.Containers()

test_containers1_listofitems_add = [List_Object.List_object(test_container1.name,test_container1.short_description),List_Object.List_object(test_container2.name,test_container2.short_description),List_Object.List_object(test_container3.name,test_container3.short_description)]
test_containers1_allitems_add = [test_container1,test_container2,test_container3]

test_containers1_listofitems_remove = [List_Object.List_object(test_container1.name,test_container1.short_description),List_Object.List_object(test_container2.name,test_container2.short_description),List_Object.List_object(test_container4.name,test_container4.short_description)]
test_containers1_allitems_remove = [test_container1,test_container2,test_container4]

#Equipment Types
test_equip_types = []
test_equip_types.append(List_Object.List_object('Armor','Armor'))
test_equip_types.append(List_Object.List_object('Clothing','Clothing'))
test_equip_types.append(List_Object.List_object('Container','Container'))
test_equip_types.append(List_Object.List_object('Food','Food'))
test_equip_types.append(List_Object.List_object('Misc Equipment','Misc Equipment'))
test_equip_types.append(List_Object.List_object('Money','Money'))
test_equip_types.append(List_Object.List_object('Weapon','Weapon'))


#Focus
test_focus1 = Focus.Focus('test1','testshortdesc1')
test_focus1.description = 'testdesc1'
test_focus1.str_bonus = '1.0'
test_focus1.per_bonus = '1.1'
test_focus1.int_bonus = '1.2'
test_focus1.dex_bonus = '1.3'
test_focus1.cha_bonus = '1.4'
test_focus1.vit_bonus = '1.5'
test_focus1.mag_bonus = '1.6'
test_focus1.str_skill_bonus = '1.7'
test_focus1.per_skill_bonus = '1.8'
test_focus1.int_skill_bonus = '1.9'
test_focus1.dex_skill_bonus = '1.10'
test_focus1.cha_skill_bonus = '1.11'
test_focus1.vit_skill_bonus = '1.12'
test_focus1.mag_skill_bonus = '1.13'
test_focus1.will_bonus = '1.14'
test_focus1.fortitude_bonus = '1.15'
test_focus1.reflex_bonus = '1.16'
test_focus1.languages_bonus = [List_Object.List_object('lang1.1','langscore1.1'),List_Object.List_object('lang1.2','langscore1.2'),List_Object.List_object('lang1.3','langscore1.3')]

test_focus1b = Focus.Focus('test1','testshortdesc1')
test_focus1b.description = 'testdesc1'
test_focus1b.str_bonus = '1.0'
test_focus1b.per_bonus = '1.1'
test_focus1b.int_bonus = '1.2'
test_focus1b.dex_bonus = '1.3'
test_focus1b.cha_bonus = '1.4'
test_focus1b.vit_bonus = '1.5'
test_focus1b.mag_bonus = '1.6'
test_focus1b.str_skill_bonus = '1.7'
test_focus1b.per_skill_bonus = '1.8'
test_focus1b.int_skill_bonus = '1.9'
test_focus1b.dex_skill_bonus = '1.10'
test_focus1b.cha_skill_bonus = '1.11'
test_focus1b.vit_skill_bonus = '1.12'
test_focus1b.mag_skill_bonus = '1.13'
test_focus1b.will_bonus = '1.14'
test_focus1b.fortitude_bonus = '1.15'
test_focus1b.reflex_bonus = '1.16'
test_focus1b.languages_bonus = [List_Object.List_object('lang1.1','langscore1.1'),List_Object.List_object('lang1.2','langscore1.2'),List_Object.List_object('lang1.3','langscore1.3')]

test_focus1c = Focus.Focus('test1','testshortdesc1')
test_focus1c.description = 'MODIFIED'
test_focus1c.str_bonus = '1.0'
test_focus1c.per_bonus = '1.1'
test_focus1c.int_bonus = '1.2'
test_focus1c.dex_bonus = '1.3'
test_focus1c.cha_bonus = '1.4'
test_focus1c.vit_bonus = '1.5'
test_focus1c.mag_bonus = '1.6'
test_focus1c.str_skill_bonus = '1.7'
test_focus1c.per_skill_bonus = '1.8'
test_focus1c.int_skill_bonus = '1.9'
test_focus1c.dex_skill_bonus = '1.10'
test_focus1c.cha_skill_bonus = '1.11'
test_focus1c.vit_skill_bonus = '1.12'
test_focus1c.mag_skill_bonus = '1.13'
test_focus1c.will_bonus = '1.14'
test_focus1c.fortitude_bonus = '1.15'
test_focus1c.reflex_bonus = '1.16'
test_focus1c.languages_bonus = [List_Object.List_object('lang1.1','langscore1.1'),List_Object.List_object('lang1.2','langscore1.2'),List_Object.List_object('lang1.3','langscore1.3')]

test_focus2 = Focus.Focus('test2','testshortdesc2')
test_focus2.description = 'testdesc2'
test_focus2.str_bonus = '2.0'
test_focus2.per_bonus = '2.1'
test_focus2.int_bonus = '2.2'
test_focus2.dex_bonus = '2.3'
test_focus2.cha_bonus = '2.4'
test_focus2.vit_bonus = '2.5'
test_focus2.mag_bonus = '2.6'
test_focus2.str_skill_bonus = '2.7'
test_focus2.per_skill_bonus = '2.8'
test_focus2.int_skill_bonus = '2.9'
test_focus2.dex_skill_bonus = '2.10'
test_focus2.cha_skill_bonus = '2.11'
test_focus2.vit_skill_bonus = '2.12'
test_focus2.mag_skill_bonus = '2.13'
test_focus2.will_bonus = '2.14'
test_focus2.fortitude_bonus = '2.15'
test_focus2.reflex_bonus = '2.16'
test_focus2.languages_bonus = [List_Object.List_object('lang2.1','langscore2.1'),List_Object.List_object('lang2.2','langscore2.2'),List_Object.List_object('lang2.3','langscore2.3')]

test_focus3 = Focus.Focus('test3','testshortdesc3')
test_focus3.description = 'testdesc3'
test_focus3.str_bonus = '3.0'
test_focus3.per_bonus = '3.1'
test_focus3.int_bonus = '3.2'
test_focus3.dex_bonus = '3.3'
test_focus3.cha_bonus = '3.4'
test_focus3.vit_bonus = '3.5'
test_focus3.mag_bonus = '3.6'
test_focus3.str_skill_bonus = '3.7'
test_focus3.per_skill_bonus = '3.8'
test_focus3.int_skill_bonus = '3.9'
test_focus3.dex_skill_bonus = '3.10'
test_focus3.cha_skill_bonus = '3.11'
test_focus3.vit_skill_bonus = '3.12'
test_focus3.mag_skill_bonus = '3.13'
test_focus3.will_bonus = '3.14'
test_focus3.fortitude_bonus = '3.15'
test_focus3.reflex_bonus = '3.16'
test_focus3.languages_bonus = [List_Object.List_object('lang3.1','langscore3.1'),List_Object.List_object('lang3.2','langscore3.2'),List_Object.List_object('lang3.3','langscore3.3')]

test_focus4 = Focus.Focus('test4','testshortdesc4')
test_focus4.description = 'testdesc4'
test_focus4.str_bonus = '4.0'
test_focus4.per_bonus = '4.1'
test_focus4.int_bonus = '4.2'
test_focus4.dex_bonus = '4.3'
test_focus4.cha_bonus = '4.4'
test_focus4.vit_bonus = '4.5'
test_focus4.mag_bonus = '4.6'
test_focus4.str_skill_bonus = '4.7'
test_focus4.per_skill_bonus = '4.8'
test_focus4.int_skill_bonus = '4.9'
test_focus4.dex_skill_bonus = '4.10'
test_focus4.cha_skill_bonus = '4.11'
test_focus4.vit_skill_bonus = '4.12'
test_focus4.mag_skill_bonus = '4.13'
test_focus4.will_bonus = '4.14'
test_focus4.fortitude_bonus = '4.15'
test_focus4.reflex_bonus = '4.16'
test_focus4.languages_bonus = [List_Object.List_object('lang4.1','langscore4.1'),List_Object.List_object('lang4.2','langscore4.2'),List_Object.List_object('lang4.3','langscore4.3')]

test_focus_empty = Focus.Focus('','')

#Foci
test_foci1 = Focus.Foci()
test_foci1.add_new(test_focus1)
test_foci1.add_new(test_focus2)
test_foci1.add_new(test_focus3)

test_foci2 = Focus.Foci()
test_foci2.add_new(test_focus1)
test_foci2.add_new(test_focus2)
test_foci2.add_new(test_focus3)

test_foci3 = Focus.Foci()
test_foci3.add_new(test_focus2)
test_foci3.add_new(test_focus3)
test_foci3.add_new(test_focus4)

test_foci4 = Focus.Foci()
test_foci4.add_new(test_focus1)
test_foci4.add_new(test_focus2)
test_foci4.add_new(test_focus3)
test_foci4.add_new(test_focus4)

test_foci_empty = Focus.Foci()

test_foci1_listofitems_add = [List_Object.List_object(test_focus1.name,test_focus1.short_description),List_Object.List_object(test_focus2.name,test_focus2.short_description),List_Object.List_object(test_focus3.name,test_focus3.short_description)]
test_foci1_allitems_add = [test_focus1,test_focus2,test_focus3]

test_foci1_listofitems_remove = [List_Object.List_object(test_focus1.name,test_focus1.short_description),List_Object.List_object(test_focus2.name,test_focus2.short_description),List_Object.List_object(test_focus4.name,test_focus4.short_description)]
test_foci1_allitems_remove = [test_focus1,test_focus2,test_focus4]


#Food
test_food1 = Food.Food('test1','testshortdesc1')
test_food1.description = 'testdesc1'
test_food1.value = '1.1'
test_food1.weight = '1.2'
test_food1.health = '1.3'
test_food1.capacity = '1.4'
test_food1.special = 'testspec1'

test_food1b = Food.Food('test1','testshortdesc1')
test_food1b.description = 'testdesc1'
test_food1b.value = '1.1'
test_food1b.weight = '1.2'
test_food1b.health = '1.3'
test_food1b.capacity = '1.4'
test_food1b.special = 'testspec1'

test_food1c = Food.Food('test1','testshortdesc1')
test_food1c.description = 'testdesc1'
test_food1c.value = '1.1'
test_food1c.weight = '1.2'
test_food1c.health = '1.3'
test_food1c.capacity = '1.4'
test_food1c.special = 'MODIFIED'

test_food2 = Food.Food('test2','testshortdesc2')
test_food2.description = 'testdesc2'
test_food2.value = '2.1'
test_food2.weight = '2.2'
test_food2.health = '2.3'
test_food2.capacity = '2.4'
test_food2.special = 'testspec2'

test_food3 = Food.Food('test3','testshortdesc3')
test_food3.description = 'testdesc3'
test_food3.value = '3.1'
test_food3.weight = '3.2'
test_food3.health = '3.3'
test_food3.capacity = '3.4'
test_food3.special = 'testspec3'

test_food4 = Food.Food('test4','testshortdesc4')
test_food4.description = 'testdesc4'
test_food4.value = '4.1'
test_food4.weight = '4.2'
test_food4.health = '4.3'
test_food4.capacity = '4.4'
test_food4.special = 'testspec4'

test_food_empty = Food.Food('','')

#Foods
test_foods1 = Food.Foods()
test_foods1.add_new(test_food1)
test_foods1.add_new(test_food2)
test_foods1.add_new(test_food3)

test_foods2 = Food.Foods()
test_foods2.add_new(test_food1)
test_foods2.add_new(test_food2)
test_foods2.add_new(test_food3)

test_foods3 = Food.Foods()
test_foods3.add_new(test_food2)
test_foods3.add_new(test_food3)
test_foods3.add_new(test_food4)

test_foods4 = Food.Foods()
test_foods4.add_new(test_food1)
test_foods4.add_new(test_food2)
test_foods4.add_new(test_food3)
test_foods4.add_new(test_food4)

test_foods_empty = Food.Foods()

test_foods1_listofitems_add = [List_Object.List_object(test_food1.name,test_food1.short_description),List_Object.List_object(test_food2.name,test_food2.short_description),List_Object.List_object(test_food3.name,test_food3.short_description)]
test_foods1_allitems_add = [test_food1,test_food2,test_food3]

test_foods1_listofitems_remove = [List_Object.List_object(test_food1.name,test_food1.short_description),List_Object.List_object(test_food2.name,test_food2.short_description),List_Object.List_object(test_food4.name,test_food4.short_description)]
test_foods1_allitems_remove = [test_food1,test_food2,test_food4]


#Lang_set
test_languages = Misc_List.Misc_list('testlangs')
test_languages.add_new(List_Object.List_object('testlang1.1','langscore1.1'))
test_languages.add_new(List_Object.List_object('testlang1.2','langscore1.2'))
test_languages.add_new(List_Object.List_object('testlang1.3','langscore1.3'))


#size_set
test_sizes = ['testsize1.1','testsize1.2','testsize1.3']


#body_set
test_bodies = ['testbody1.1','testbody1.2','testbody1.3']


#feat_set
test_feats = ['testfeat1.1','testfeat1.2','testfeat1.3']


#List_Object
test_listobject1 = List_Object.List_object('test1','testshortdesc1')
test_listobject1b = List_Object.List_object('test1','testshortdesc1')
test_listobject2 = List_Object.List_object('test2','testshortdesc2')
test_listobject3 = List_Object.List_object('test3','testshortdesc3')
test_listobject4 = List_Object.List_object('test4','testshortdesc4')

#List set
test_set1 = [test_listobject1,test_listobject2,test_listobject3]
test_set2 = [test_listobject1,test_listobject2,test_listobject3]
test_set3 = [test_listobject2,test_listobject3,test_listobject4]
test_set4 = [test_listobject1,test_listobject2,test_listobject3,test_listobject4]


#Misc Equip
test_miscequip1 = Misc_Equipment.Misc_equip('test1','testshortdesc1')
test_miscequip1.description = 'testdesc1'
test_miscequip1.value = '1.1'
test_miscequip1.weight = '1.2'
test_miscequip1.health = '1.3'
test_miscequip1.capacity = '1.4'
test_miscequip1.special = 'testspec1'

test_miscequip1b = Misc_Equipment.Misc_equip('test1','testshortdesc1')
test_miscequip1b.description = 'testdesc1'
test_miscequip1b.value = '1.1'
test_miscequip1b.weight = '1.2'
test_miscequip1b.health = '1.3'
test_miscequip1b.capacity = '1.4'
test_miscequip1b.special = 'testspec1'

test_miscequip1c = Misc_Equipment.Misc_equip('test1','testshortdesc1')
test_miscequip1c.description = 'testdesc1'
test_miscequip1c.value = '1.1'
test_miscequip1c.weight = '1.2'
test_miscequip1c.health = '1.3'
test_miscequip1c.capacity = '1.4'
test_miscequip1c.special = 'MODIFIED'

test_miscequip2 = Misc_Equipment.Misc_equip('test2','testshortdesc2')
test_miscequip2.description = 'testdesc2'
test_miscequip2.value = '2.1'
test_miscequip2.weight = '2.2'
test_miscequip2.health = '2.3'
test_miscequip2.capacity = '2.4'
test_miscequip2.special = 'testspec2'

test_miscequip3 = Misc_Equipment.Misc_equip('test3','testshortdesc3')
test_miscequip3.description = 'testdesc3'
test_miscequip3.value = '3.1'
test_miscequip3.weight = '3.2'
test_miscequip3.health = '3.3'
test_miscequip3.capacity = '3.4'
test_miscequip3.special = 'testspec3'

test_miscequip4 = Misc_Equipment.Misc_equip('test4','testshortdesc4')
test_miscequip4.description = 'testdesc4'
test_miscequip4.value = '4.1'
test_miscequip4.weight = '4.2'
test_miscequip4.health = '4.3'
test_miscequip4.capacity = '4.4'
test_miscequip4.special = 'testspec4'

test_miscequip_empty = Misc_Equipment.Misc_equip('','')

#Misc Equipment
test_miscequipment1 = Misc_Equipment.Misc_equipment()
test_miscequipment1.add_new(test_miscequip1)
test_miscequipment1.add_new(test_miscequip2)
test_miscequipment1.add_new(test_miscequip3)

test_miscequipment2 = Misc_Equipment.Misc_equipment()
test_miscequipment2.add_new(test_miscequip1)
test_miscequipment2.add_new(test_miscequip2)
test_miscequipment2.add_new(test_miscequip3)

test_miscequipment3 = Misc_Equipment.Misc_equipment()
test_miscequipment3.add_new(test_miscequip2)
test_miscequipment3.add_new(test_miscequip3)
test_miscequipment3.add_new(test_miscequip4)

test_miscequipment4 = Misc_Equipment.Misc_equipment()
test_miscequipment4.add_new(test_miscequip1)
test_miscequipment4.add_new(test_miscequip2)
test_miscequipment4.add_new(test_miscequip3)
test_miscequipment4.add_new(test_miscequip4)

test_miscequipment_empty = Misc_Equipment.Misc_equipment()

test_miscequipment1_listofitems_add = [List_Object.List_object(test_miscequip1.name,test_miscequip1.short_description),List_Object.List_object(test_miscequip2.name,test_miscequip2.short_description),List_Object.List_object(test_miscequip3.name,test_miscequip3.short_description)]
test_miscequipment1_allitems_add = [test_miscequip1,test_miscequip2,test_miscequip3]

test_miscequipment1_listofitems_remove = [List_Object.List_object(test_miscequip1.name,test_miscequip1.short_description),List_Object.List_object(test_miscequip2.name,test_miscequip2.short_description),List_Object.List_object(test_miscequip4.name,test_miscequip4.short_description)]
test_miscequipment1_allitems_remove = [test_miscequip1,test_miscequip2,test_miscequip4]


#Misc_List
test_misclist1 = Misc_List.Misc_list('test1','testshortdesc1')
test_misclist1.add_new(List_Object.List_object('test1.1','testshortdesc1.1'))
test_misclist1.add_new(List_Object.List_object('test1.2','testshortdesc1.2'))
test_misclist1.add_new(List_Object.List_object('test1.3','testshortdesc1.3'))

test_misclist1b = Misc_List.Misc_list('test1','testshortdesc1')
test_misclist1b.add_new(List_Object.List_object('test1.1','testshortdesc1.1'))
test_misclist1b.add_new(List_Object.List_object('test1.2','testshortdesc1.2'))
test_misclist1b.add_new(List_Object.List_object('test1.3','testshortdesc1.3'))

test_misclist1c = Misc_List.Misc_list('test1','MODIFIED')
test_misclist1c.add_new(List_Object.List_object('test1.1','testshortdesc1.1'))
test_misclist1c.add_new(List_Object.List_object('test1.2','testshortdesc1.2'))
test_misclist1c.add_new(List_Object.List_object('test1.3','testshortdesc1.3'))

test_misclist2 = Misc_List.Misc_list('test2','testshortdesc2')
test_misclist2.add_new(List_Object.List_object('test2.1','testshortdesc2.1'))
test_misclist2.add_new(List_Object.List_object('test2.2','testshortdesc2.2'))
test_misclist2.add_new(List_Object.List_object('test2.3','testshortdesc2.3'))

test_misclist3 = Misc_List.Misc_list('test3','testshortdesc3')
test_misclist3.add_new(List_Object.List_object('test3.1','testshortdesc3.1'))
test_misclist3.add_new(List_Object.List_object('test3.2','testshortdesc3.2'))
test_misclist3.add_new(List_Object.List_object('test3.3','testshortdesc3.3'))

test_misclist4 = Misc_List.Misc_list('test4','testshortdesc4')
test_misclist4.add_new(List_Object.List_object('test4.1','testshortdesc4.1'))
test_misclist4.add_new(List_Object.List_object('test4.2','testshortdesc4.2'))
test_misclist4.add_new(List_Object.List_object('test4.3','testshortdesc4.3'))

test_misclist_empty = Misc_List.Misc_list('','',[])

#Misc_Lists
test_misclists1 = Misc_List.Misc_lists()
test_misclists1.add_new(test_misclist1)
test_misclists1.add_new(test_misclist2)
test_misclists1.add_new(test_misclist3)

test_misclists2 = Misc_List.Misc_lists()
test_misclists2.add_new(test_misclist1)
test_misclists2.add_new(test_misclist2)
test_misclists2.add_new(test_misclist3)

test_misclists3 = Misc_List.Misc_lists()
test_misclists3.add_new(test_misclist2)
test_misclists3.add_new(test_misclist3)
test_misclists3.add_new(test_misclist4)

test_misclists4 = Misc_List.Misc_lists()
test_misclists4.add_new(test_misclist1)
test_misclists4.add_new(test_misclist2)
test_misclists4.add_new(test_misclist3)
test_misclists4.add_new(test_misclist4)

test_misclists_empty = Misc_List.Misc_lists()

test_misclists1_listofitems_add = [List_Object.List_object(test_misclist1.name,test_misclist1.short_description),List_Object.List_object(test_misclist2.name,test_misclist2.short_description),List_Object.List_object(test_misclist3.name,test_misclist3.short_description)]
test_misclists1_allitems_add = [test_misclist1,test_misclist2,test_misclist3]

test_misclists1_listofitems_remove = [List_Object.List_object(test_misclist1.name,test_misclist1.short_description),List_Object.List_object(test_misclist2.name,test_misclist2.short_description),List_Object.List_object(test_misclist4.name,test_misclist4.short_description)]
test_misclists1_allitems_remove = [test_misclist1,test_misclist2,test_misclist4]


#Money
test_money1 = Money.Money('test1','testshortdesc1')
test_money1.description = 'testdesc1'
test_money1.value = '1.1'
test_money1.weight = '1.2'
test_money1.health = '1.3'
test_money1.capacity = '1.4'
test_money1.special = 'testspec1'

test_money1b = Money.Money('test1','testshortdesc1')
test_money1b.description = 'testdesc1'
test_money1b.value = '1.1'
test_money1b.weight = '1.2'
test_money1b.health = '1.3'
test_money1b.capacity = '1.4'
test_money1b.special = 'testspec1'

test_money1c = Money.Money('test1','testshortdesc1')
test_money1c.description = 'testdesc1'
test_money1c.value = '1.1'
test_money1c.weight = '1.2'
test_money1c.health = '1.3'
test_money1c.capacity = '1.4'
test_money1c.special = 'MODIFIED'

test_money2 = Money.Money('test2','testshortdesc2')
test_money2.description = 'testdesc2'
test_money2.value = '2.1'
test_money2.weight = '2.2'
test_money2.health = '2.3'
test_money2.capacity = '2.4'
test_money2.special = 'testspec2'

test_money3 = Money.Money('test3','testshortdesc3')
test_money3.description = 'testdesc3'
test_money3.value = '3.1'
test_money3.weight = '3.2'
test_money3.health = '3.3'
test_money3.capacity = '3.4'
test_money3.special = 'testspec3'

test_money4 = Money.Money('test4','testshortdesc4')
test_money4.description = 'testdesc4'
test_money4.value = '4.1'
test_money4.weight = '4.2'
test_money4.health = '4.3'
test_money4.capacity = '4.4'
test_money4.special = 'testspec4'

test_money_empty = Money.Money('','')

#Monies
test_monies1 = Money.Monies()
test_monies1.add_new(test_money1)
test_monies1.add_new(test_money2)
test_monies1.add_new(test_money3)

test_monies2 = Money.Monies()
test_monies2.add_new(test_money1)
test_monies2.add_new(test_money2)
test_monies2.add_new(test_money3)

test_monies3 = Money.Monies()
test_monies3.add_new(test_money2)
test_monies3.add_new(test_money3)
test_monies3.add_new(test_money4)

test_monies4 = Money.Monies()
test_monies4.add_new(test_money1)
test_monies4.add_new(test_money2)
test_monies4.add_new(test_money3)
test_monies4.add_new(test_money4)

test_monies_empty = Money.Monies()

test_monies1_listofitems_add = [List_Object.List_object(test_money1.name,test_money1.short_description),List_Object.List_object(test_money2.name,test_money2.short_description),List_Object.List_object(test_money3.name,test_money3.short_description)]
test_monies1_allitems_add = [test_money1,test_money2,test_money3]

test_monies1_listofitems_remove = [List_Object.List_object(test_money1.name,test_money1.short_description),List_Object.List_object(test_money2.name,test_money2.short_description),List_Object.List_object(test_money4.name,test_money4.short_description)]
test_monies1_allitems_remove = [test_money1,test_money2,test_money4]


#Race
test_race1 = Race.Race('test1')
test_race1.short_description = 'testshortdesc1'
test_race1.description = 'testdesc1'
test_race1.size = 'size1'
test_race1.body = 'body1'
test_race1.foci = ['foci1.1','foci1.2','foci1.3']
test_race1.feats = ['feat1.1','feat1.2','feat1.3']
test_race1.str_bonus = '1.0'
test_race1.per_bonus = '1.1'
test_race1.int_bonus = '1.2'
test_race1.dex_bonus = '1.3'
test_race1.cha_bonus = '1.4'
test_race1.vit_bonus = '1.5'
test_race1.mag_bonus = '1.6'
test_race1.will_bonus = '1.7'
test_race1.fortitude_bonus = '1.8'
test_race1.reflex_bonus = '1.9'
test_race1.languages_bonus.append(List_Object.List_object('lang1.1','+1'))
test_race1.languages_bonus.append(List_Object.List_object('lang1.2','+2'))
test_race1.languages_bonus.append(List_Object.List_object('lang1.3','+3'))

test_race1b = Race.Race('test1')
test_race1b.short_description = 'testshortdesc1'
test_race1b.description = 'testdesc1'
test_race1b.size = 'size1'
test_race1b.body = 'body1'
test_race1b.foci = ['foci1.1','foci1.2','foci1.3']
test_race1b.feats = ['feat1.1','feat1.2','feat1.3']
test_race1b.str_bonus = '1.0'
test_race1b.per_bonus = '1.1'
test_race1b.int_bonus = '1.2'
test_race1b.dex_bonus = '1.3'
test_race1b.cha_bonus = '1.4'
test_race1b.vit_bonus = '1.5'
test_race1b.mag_bonus = '1.6'
test_race1b.will_bonus = '1.7'
test_race1b.fortitude_bonus = '1.8'
test_race1b.reflex_bonus = '1.9'
test_race1b.languages_bonus.append(List_Object.List_object('lang1.1','+1'))
test_race1b.languages_bonus.append(List_Object.List_object('lang1.2','+2'))
test_race1b.languages_bonus.append(List_Object.List_object('lang1.3','+3'))

test_race1c = Race.Race('test1')
test_race1c.short_description = 'testshortdesc1'
test_race1c.description = 'MODIFIED'
test_race1c.size = 'size1'
test_race1c.body = 'body1'
test_race1c.foci = ['foci1.1','foci1.2','foci1.3']
test_race1c.feats = ['feat1.1','feat1.2','feat1.3']
test_race1c.str_bonus = '1.0'
test_race1c.per_bonus = '1.1'
test_race1c.int_bonus = '1.2'
test_race1c.dex_bonus = '1.3'
test_race1c.cha_bonus = '1.4'
test_race1c.vit_bonus = '1.5'
test_race1c.mag_bonus = '1.6'
test_race1c.will_bonus = '1.7'
test_race1c.fortitude_bonus = '1.8'
test_race1c.reflex_bonus = '1.9'
test_race1c.languages_bonus.append(List_Object.List_object('lang1.1','+1'))
test_race1c.languages_bonus.append(List_Object.List_object('lang1.2','+2'))
test_race1c.languages_bonus.append(List_Object.List_object('lang1.3','+3'))

test_race2 = Race.Race('test2')
test_race2.short_description = 'testshortdesc2'
test_race2.description = 'testdesc2'
test_race2.size = 'size2'
test_race2.body = 'body2'
test_race2.foci = ['foci2.1','foci2.2','foci2.3']
test_race2.feats = ['feat2.1','feat2.2','feat2.3']
test_race2.str_bonus = '2.0'
test_race2.per_bonus = '2.1'
test_race2.int_bonus = '2.2'
test_race2.dex_bonus = '2.3'
test_race2.cha_bonus = '2.4'
test_race2.vit_bonus = '2.5'
test_race2.mag_bonus = '2.6'
test_race2.will_bonus = '2.7'
test_race2.fortitude_bonus = '2.8'
test_race2.reflex_bonus = '2.9'
test_race2.languages_bonus.append(List_Object.List_object('lang2.1','+1'))
test_race2.languages_bonus.append(List_Object.List_object('lang2.2','+2'))
test_race2.languages_bonus.append(List_Object.List_object('lang2.3','+3'))

test_race3 = Race.Race('test3')
test_race3.short_description = 'testshortdesc3'
test_race3.description = 'testdesc3'
test_race3.size = 'size3'
test_race3.body = 'body3'
test_race3.foci = ['foci3.1','foci3.2','foci3.3']
test_race3.feats = ['feat3.1','feat3.2','feat3.3']
test_race3.str_bonus = '3.0'
test_race3.per_bonus = '3.1'
test_race3.int_bonus = '3.2'
test_race3.dex_bonus = '3.3'
test_race3.cha_bonus = '3.4'
test_race3.vit_bonus = '3.5'
test_race3.mag_bonus = '3.6'
test_race3.will_bonus = '3.7'
test_race3.fortitude_bonus = '3.8'
test_race3.reflex_bonus = '3.9'
test_race3.languages_bonus.append(List_Object.List_object('lang3.1','+1'))
test_race3.languages_bonus.append(List_Object.List_object('lang3.2','+2'))
test_race3.languages_bonus.append(List_Object.List_object('lang3.3','+3'))

test_race4 = Race.Race('test4')
test_race4.short_description = 'testshortdesc4'
test_race4.description = 'testdesc4'
test_race4.size = 'size4'
test_race4.body = 'body4'
test_race4.foci = ['foci4.1','foci4.2','foci4.3']
test_race4.feats = ['feat4.1','feat4.2','feat4.3']
test_race4.str_bonus = '4.0'
test_race4.per_bonus = '4.1'
test_race4.int_bonus = '4.2'
test_race4.dex_bonus = '4.3'
test_race4.cha_bonus = '4.4'
test_race4.vit_bonus = '4.5'
test_race4.mag_bonus = '4.6'
test_race4.will_bonus = '4.7'
test_race4.fortitude_bonus = '4.8'
test_race4.reflex_bonus = '4.9'
test_race4.languages_bonus.append(List_Object.List_object('lang4.1','+1'))
test_race4.languages_bonus.append(List_Object.List_object('lang4.2','+2'))
test_race4.languages_bonus.append(List_Object.List_object('lang4.3','+3'))

test_race_empty = Race.Race('')

#Races
test_races1 = Race.Races()
test_races1.add_new(test_race1)
test_races1.add_new(test_race2)
test_races1.add_new(test_race3)

test_races2 = Race.Races()
test_races2.add_new(test_race1)
test_races2.add_new(test_race2)
test_races2.add_new(test_race3)

test_races3 = Race.Races()
test_races3.add_new(test_race2)
test_races3.add_new(test_race3)
test_races3.add_new(test_race4)

test_races4 = Race.Races()
test_races4.add_new(test_race1)
test_races4.add_new(test_race2)
test_races4.add_new(test_race3)
test_races4.add_new(test_race4)

test_races_empty = Race.Races()

test_races1_listofitems_add = [List_Object.List_object(test_race1.name,test_race1.short_description),List_Object.List_object(test_race2.name,test_race2.short_description),List_Object.List_object(test_race3.name,test_race3.short_description)]
test_races1_allitems_add = [test_race1,test_race2,test_race3]

test_races1_listofitems_remove = [List_Object.List_object(test_race1.name,test_race1.short_description),List_Object.List_object(test_race2.name,test_race2.short_description),List_Object.List_object(test_race4.name,test_race4.short_description)]
test_races1_allitems_remove = [test_race1,test_race2,test_race4]


#Weapon
test_weapon1 = Weapon.Weapon('test1','testshortdesc1')
test_weapon1.description = 'testdesc1'
test_weapon1.value = '1.1'
test_weapon1.weight = '1.2'
test_weapon1.health = '1.3'
test_weapon1.capacity = '1.4'
test_weapon1.special = 'testspec1'
test_weapon1.hands = '1.5'
test_weapon1.weapon_type = 'testtype1'
test_weapon1.range = '1.6'
test_weapon1.ammo_type = 'testammo1'
test_weapon1.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_weapon1b = Weapon.Weapon('test1','testshortdesc1')
test_weapon1b.description = 'testdesc1'
test_weapon1b.value = '1.1'
test_weapon1b.weight = '1.2'
test_weapon1b.health = '1.3'
test_weapon1b.capacity = '1.4'
test_weapon1b.special = 'testspec1'
test_weapon1b.hands = '1.5'
test_weapon1b.weapon_type = 'testtype1'
test_weapon1b.range = '1.6'
test_weapon1b.ammo_type = 'testammo1'
test_weapon1b.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_weapon1c = Weapon.Weapon('test1','testshortdesc1')
test_weapon1c.description = 'testdesc1'
test_weapon1c.value = '1.1'
test_weapon1c.weight = '1.2'
test_weapon1c.health = '1.3'
test_weapon1c.capacity = '1.4'
test_weapon1c.special = 'MODIFIED'
test_weapon1c.hands = '1.0'
test_weapon1c.weapon_type = 'testtype1'
test_weapon1c.range = '1.5'
test_weapon1c.ammo_type = 'testammo1'
test_weapon1c.damage_types = [List_Object.List_object('dt1.1','dtscore1.1'),List_Object.List_object('dt1.2','dtscore1.2'),List_Object.List_object('dt1.3','dtscore1.3')]

test_weapon2 = Weapon.Weapon('test2','testshortdesc2')
test_weapon2.description = 'testdesc2'
test_weapon2.value = '2.1'
test_weapon2.weight = '2.2'
test_weapon2.health = '2.3'
test_weapon2.capacity = '2.4'
test_weapon2.special = 'testspec2'
test_weapon2.hands = '2.5'
test_weapon2.weapon_type = 'testtype2'
test_weapon2.range = '2.6'
test_weapon2.ammo_type = 'testammo2'
test_weapon2.damage_types = [List_Object.List_object('dt2.1','dtscore2.1'),List_Object.List_object('dt2.2','dtscore2.2'),List_Object.List_object('dt2.3','dtscore2.3')]

test_weapon3 = Weapon.Weapon('test3','testshortdesc3')
test_weapon3.description = 'testdesc3'
test_weapon3.value = '3.1'
test_weapon3.weight = '3.2'
test_weapon3.health = '3.3'
test_weapon3.capacity = '3.4'
test_weapon3.special = 'testspec3'
test_weapon3.hands = '3.5'
test_weapon3.weapon_type = 'testtype3'
test_weapon3.range = '3.6'
test_weapon3.ammo_type = 'testammo3'
test_weapon3.damage_types = [List_Object.List_object('dt3.1','dtscore3.1'),List_Object.List_object('dt3.2','dtscore3.2'),List_Object.List_object('dt3.3','dtscore3.3')]

test_weapon4 = Weapon.Weapon('test4','testshortdesc4')
test_weapon4.description = 'testdesc4'
test_weapon4.value = '4.1'
test_weapon4.weight = '4.2'
test_weapon4.health = '4.3'
test_weapon4.capacity = '4.4'
test_weapon4.special = 'testspec4'
test_weapon4.hands = '4.5'
test_weapon4.weapon_type = 'testtype4'
test_weapon4.range = '4.6'
test_weapon4.ammo_type = 'testammo4'
test_weapon4.damage_types = [List_Object.List_object('dt4.1','dtscore4.1'),List_Object.List_object('dt4.2','dtscore4.2'),List_Object.List_object('dt4.3','dtscore4.3')]

test_weapon_empty = Weapon.Weapon('','')

#Foods
test_weapons1 = Weapon.Weapons()
test_weapons1.add_new(test_weapon1)
test_weapons1.add_new(test_weapon2)
test_weapons1.add_new(test_weapon3)

test_weapons2 = Weapon.Weapons()
test_weapons2.add_new(test_weapon1)
test_weapons2.add_new(test_weapon2)
test_weapons2.add_new(test_weapon3)

test_weapons3 = Weapon.Weapons()
test_weapons3.add_new(test_weapon2)
test_weapons3.add_new(test_weapon3)
test_weapons3.add_new(test_weapon4)

test_weapons4 = Weapon.Weapons()
test_weapons4.add_new(test_weapon1)
test_weapons4.add_new(test_weapon2)
test_weapons4.add_new(test_weapon3)
test_weapons4.add_new(test_weapon4)

test_weapons_empty = Weapon.Weapons()

test_weapons1_listofitems_add = [List_Object.List_object(test_weapon1.name,test_weapon1.short_description),List_Object.List_object(test_weapon2.name,test_weapon2.short_description),List_Object.List_object(test_weapon3.name,test_weapon3.short_description)]
test_weapons1_allitems_add = [test_weapon1,test_weapon2,test_weapon3]

test_weapons1_listofitems_remove = [List_Object.List_object(test_weapon1.name,test_weapon1.short_description),List_Object.List_object(test_weapon2.name,test_weapon2.short_description),List_Object.List_object(test_weapon4.name,test_weapon4.short_description)]
test_weapons1_allitems_remove = [test_weapon1,test_weapon2,test_weapon4]


#picklist
test_picklist1 = ['test1.1','test1.2','test1.3','test1.4']
test_picklist2 = [test_listobject1,test_listobject2,test_listobject3]
test_picklist3 = ['test3.1','test3.2','test1.3','test1.4']
test_picklist4 = ['test1: testshortdesc1', 'test2: testshortdesc2', 'test3: testshortdesc3']
