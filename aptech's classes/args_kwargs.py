# arguments are often shortened to args in python documentations. we use * in front of the parameter name if we dont know
#the amount of arguments we'll give to the function. these are arbitrary arguments. this way, the function will receive a tuple of arguments
# arbitrary arguments are ofteh shortened to *args in python documentation
def children(*names):
    print("my favorite child is "+ names[3])

children("John", "Nicolas", "Malo", "Justina")


# Keyword arguments. we can receive arguments into parameters by using the key value pair syntax. i.e key = value.
#this way the order of the arguments dont matter. keyword Arguments are often shortened to kwargs in python documentation

def children(child1, child4, child3, child2):
    print("My favorite child is "+ child3)


children(child2="Chris", child4="Justina", child1="Davido", child3="Malo")

# Arbitary keyword Arguments. if we do not know the amount of keyword arguments that will be passed to the function
# we add two asterisk in front of the parameter. arbitrary keyword arguments are often shortened to **kwargs in python

def fav_child(**child):
    print("My favorite child is"+ child["child3"])

fav_child(child1 = "Malo", child2 = "Nicolas", child3 = "Justina", child4 = "Palmer")