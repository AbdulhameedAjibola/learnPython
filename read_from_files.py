# we can use the python read command to read files outside of our python file
# first we have to open the file
# we also have to specify the mode in which we're opening the file, here we use r which stands for read
'''
in the read mode, we're not allowed to edit the file
w stands for write, this means we can change the file, we can add information, delete information, modify existing
content in the file too
a stands for append, this means that we cant modify existing content, but we can add/ append info onto the end of
the file
'''
# we can store the open function in a variable,and now the content of the file being opened is stored in a variable
file = open("text.txt", "r")

# how to get whats in the file
print(file.read())
# how to read characters from an individual line()
print(file.readline())
# whenever we open a file, we always have to be sure to close the file after
file.close()

