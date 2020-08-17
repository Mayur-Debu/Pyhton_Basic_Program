with open("mayur.txt") as file:
    """with block is used to open file .....
    The syntax is given above ...
    thier is no need to use the close()"""
    print(file.readline())

file=open("mayur.txt")
print(file.readline())
file.close()
# print(file.__doc__)