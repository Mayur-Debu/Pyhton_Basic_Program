n=int(input("Enter the values of n: "))
ch=int(input("ENTER 1 OR 0: "))

if ch==0:
    i=1
    while(i<=n):
        print("*"*i)
        i+=1
else:
    i=n
    while(i!=0):
        print(i*"*")
        i-=1