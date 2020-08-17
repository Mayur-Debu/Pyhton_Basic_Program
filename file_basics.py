# file IO Basics
"""
r= reading to a file (Default)
w= writing to a file
x= if file doesn't exist the  create the file
a= add to a file
t= text mode (Default)
b= binary type of file
r+= opens file in the read and write mode simultaneously
"""

# Program starts here

file=open("mayur.txt")
# print(file.read())
# print(file.read(3))  Prints only 3 charecters
#
# for lines in file:
#     print(lines) This line prints the file content with a \n at its end.
#     print(lines,end="") Whereas this line excludes the \n command
#
# print(file.readlines())   prints every line in the list format

# It is compulsory to close an opened file, it iis considered as a good practice
file.close()
# print(file.read()) It will not execute as the file is already closed