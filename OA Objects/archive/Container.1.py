import List_Object
import copy

class Containers:
    list_of_containers = []
    all_containers = []

    def add_new(self,container):
        self.all_containers.append(container)
        self.list_of_containers.append(List_Object.List_object(container.name,container.short_description))

    def remove(self,container):
        self.list_of_containers.remove(self.list_of_containers[self.all_containers.index(self.get_container(container.name))])
        self.all_containers.remove(self.get_container(container.name))

    def equals(self,tocompare):
        same = (len(self.all_containers) == len(tocompare.all_containers))
        if same:
            for idx,item in enumerate(tocompare.all_containers):
                same = same and item.equals(self.all_containers[idx])

        return same

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return len(self.all_containers) == 0

    def update(self,container):
        found = False
        for item in self.all_containers:
            if item.name == container.name:
                idx = self.all_containers.index(item)
                self.all_containers[idx] = container
                self.list_of_containers[idx].name = container.name
                self.list_of_containers[idx].short_description = container.short_description
                found = True
                break
        
        if not found:
            self.add_new(container)

    def get_container(self,name):
        for item in self.all_containers:
            if item.name == name:
                return item
        
        return Container('','')

    def __len__(self):
        return len(self.all_containers)

    def __init__(self):
        self.all_containers = []
        self.list_of_containers = []

class Container:
    name = ''
    short_description = ''
    description = ''
    value = 0
    weight = 0
    health = 0
    capacity = 0
    special = ''

    def equals(self,tocompare):
        return ((self.name == tocompare.name)
            and (self.short_description == tocompare.short_description)
            and (self.description == tocompare.description)
            and (self.value == tocompare.value)
            and (self.weight == tocompare.weight)
            and (self.health == tocompare.health)
            and (self.capacity == tocompare.capacity)
            and (self.special == tocompare.special)
            )

    def clone(self):
        return copy.deepcopy(self)

    def isempty(self):
        return (self.name.strip() == '' and self.short_description.strip() == '')

    def __init__(self,name,short_description=''):
        self.name = name
        self.short_description = short_description
