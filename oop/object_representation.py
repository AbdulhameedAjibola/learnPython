# in this module we'll see how we can print out our objects from a list in the actual form using the __repr__ magic method
# we are going to create a list, and then store in objects/instances created into there

class Person:
    all = [] # this class attribute stores all instances being created

    def __init__(self, name: str, age: float, gender="Male"):
        self.name = name
        self.age = age
        self.gender = gender
        # since the instance are initialized here, we can append the instance to the list through here too
        Person.all.append(self)

    def details(self):
        print(f"My name is {self.name}")

    # to print our objects from the list in a very friendly way
    # here we are going to use the __repr__ magic method
    def __repr__(self):
        return f"Person('{self.name}', {self.age}, '{self.gender}')"



person1 = Person("adanma", 27, "Female")
person2 = Person("koforola", 23, "Female")
person3 = Person("john dumelo", 22)
person4 = Person("kossi", 29)
person5 = Person("josh", 26)

# if we print out the list now, it calls the __repr__ method
print(Person.all)
# lets say we want to print the names in all the instances
for instance in Person.all:
    print(instance.name)




