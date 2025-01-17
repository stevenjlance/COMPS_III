class Animal:
    id = 1
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
        self.__id = Animal.id
        Animal.id += 1
    
    def get_id(self):
        return self.__id
    
    def set_id(self, new_id):
        self.__id = new_id

example1 = Animal("Rex", 5, 50)
example2 = Animal("Max", 3, 30)
print(example1.get_id())
example1.set_id(10)
print(example1.get_id())
