var1=int(input("ENTER THE FIRST NUMBER: "))
var2=int(input("ENTER THE SECOND NUMBER: "))
operator=input("ENTER THE OPERATOR: ")

if(operator=="+"):
    if var1==56 and var2==9:
        print("77")
    else:
         print(var1+var2)
elif(operator=="-"):
    print(var1 - var2)
elif(operator=="*"):
    if var1==45 and var2==3:
        print("555")
    else:
        print(var1 * var2)
else:
    if var1==56 and var2==6:
        print("4")
    else:
      print(var1/var2)