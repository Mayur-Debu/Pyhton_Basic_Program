def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

n=int(input("ENTER THE NUMBER YOU WANT TO FIND FIBONACCI SERIES OF: "))
print(fibonacci(n))