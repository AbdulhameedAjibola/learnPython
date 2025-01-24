import random

# MULITPLE INHERITANCE

# class A:
#     def info_A(self):
#         print("we are inside class A")

# class B:
#     def info_B(self):
#         print("we are inside class B")

# class C(A,B):
#     def info_C(self):
#         print("we are inside class C")
        
        
# obj = C()

# obj.info_B()


# class Sand:
#     def pack_sand(self):
#         print("I am packing sand")
        
#     def wage(self):
#         return 10
        

# class Stone:
#     def carry_block(self):
#         print("I am carrying stone")
    
#     def wage(self):
#         return 20
        

# class Combined(Sand, Stone):
#     def hybrid(self):
#         print("This person can do both")
    
#     def mix_cement(self):
#         print("I can also mix cement")
        
#     def wage(self):
#         return 30
        
# budget = 100
 
# s1 = Sand()
# b1 = Stone()
# c1 = Combined()


# create warrior, Mage, Magic Swordman


def warrior_stats():
    health = 1000
    attack = 400
    defence = 500
    magic = 100
    value = [health,attack,defence,magic]
    return value


def mage_stats():
    health = 1000
    attack = 300
    defence = 200
    magic = 500
    value = [health,attack,defence,magic]
    return value




    
class Warrior:
    
    def __init__(self,name):
        self.name = name
        x = warrior_stats()
        self.health = x[0]
        self.attack = x[1]
        self.defence = x[2]
        self.magic = x[3]
        
    def offence(self,enemy):
        x = self.attack
        value = random.randrange(((self.attack-100)/10),((self.attack)/10))
        print(f"{self.name} attacked {enemy.name} and removed {value} health")
        enemy.health = enemy.health - value
        print(f"{enemy.name} has {enemy.health} health left")
        
        


class Mage:
    
    def __init__(self,name):
        self.name = name
        x = mage_stats()
        self.health = x[0]
        self.attack = x[1]
        self.defence = x[2]
        self.magic = x[3]
        
    def offence(self,enemy):
        value = random.randrange(((self.attack-100)/10),((self.attack)/10))
        print(f"{self.name} attacked {enemy.name} and removed {value} health")
        enemy.health = enemy.health - value
        print(f"{enemy.name} has {enemy.health} health left")
    

class Magic_Swordman(Warrior,Mage):
    health = 1000
    attack = 350
    defence = 350
    magic = 300
    def __init__(self,name):
        self.name = name



w1 = Warrior("sukuna")
m1 = Mage("Gojo")

w1.offence(m1)
# m1.offence(w1)













