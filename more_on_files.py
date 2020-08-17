file=open("mayur.txt")
print(file.tell()) #prints the position of pointer
file.seek(70)      #changes the pointers position to the given position
print(file.readline())