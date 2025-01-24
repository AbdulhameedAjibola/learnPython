'''
 so in this python file, we will fetch data from a csv file named item.csv and then use it to
instantiate/ create objects for our class
to do this, we will convert our instantiate_from_csv methos to a class method. A class method is a method that can
only be accessed from the class level only
 to do this we will use python decorators. a decorator is what is used to change the behaviours of a function, by calling them
 the line before we create our functions
 this is also called annotations in java sha
to do this we will also need to import a module to handle the csv file
'''
import csv


# then we create our class
class Person:
    # class attribute to store instances
    all = []
    # then the constructor/init method
    def __init__(self, name: str, age:float, gender: str):
        self.name = name
        self.age = age
        self.gender = gender

        Person.all.append(self)

        # class method to fetch data from csv
    @classmethod
    def instantiate_from_csv(cls):
        # to open the csv file
        with open("item.csv", 'r') as f:
            # convert the csv file content into a dictionary
            reader = csv.DictReader(f)
            # convert the dictionary into a list
            items = list(reader)
        # so to create instances with the data in the dictionary from the csv
        for item in items:
            Person(
                name= item.get('name'),
                age = float(item.get('age')),
                gender= item.get('gender')
             )



# here we call the method, since its a class method, we reference it from the class directly, we dont need to create a method
Person.instantiate_from_csv()
print(Person.all)