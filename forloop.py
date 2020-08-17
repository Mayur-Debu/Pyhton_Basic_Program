list=[1,2,3,4,5,6,7,8,9,0,"hi",67,45,"bye"]
print(list)

for items in list:
    if type(items)is int:
        if items>6:
            print(items)