# here we will be specifying datatypes for parameters created in the constructors to check if the right thing has been entered by the
# user and to prevent any misunderstandings
# please not that when variables are declared through a constructot, we initialize the variables on creation of the object
class Person:
    # so in this constructor, you'll see how we specify the types to be inputted/ what we expect to receive
    # for name, we pass in str, to specify that we're receiving a string
    # for age, we specify float, this can receive integers and decimal numbers
    # for gender, we'll pass in a default of "male", and by this, we dont need to specify the type, since its holding a string already

    def __init__(self, name: str, age: float, gender="male"):
        self.name = name
        self.age = age
        self.gender = gender
    def character(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")


person1 = Person("James", 22, "female")
person1.character()
