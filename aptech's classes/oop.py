class AptechStudent:
    def assign_reg(self):
        return self.phone_number + "123"

    reg_num = assign_reg()
    course_name = "ADSE"
    course_days = "Monday, Wednesday, Friday"

    def __init__(self, firstname, lastname, phone_number):
        self.firstname = firstname
        self.lastname = lastname
        self.phone_number = phone_number
    def take_details(self):
        self.firstname = input("Please enter your firstname? ")
        self.lastname = input("Please enter your lastname? ")
        self.phone_number = input("Please input your phone number here")

        self.assign_reg()


student1 = AptechStudent("James", "Johnson", "09162791272")
student1.take_details()
