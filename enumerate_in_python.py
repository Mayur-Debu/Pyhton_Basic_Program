list=["Even1","Odd1","Even2","Odd2"]

info=0
for item in list:
    if info%2==0:
        print(item)
    info+=1




for index,info in enumerate(list):           # using enumerate function
    if index%2==0:
        print(info)
