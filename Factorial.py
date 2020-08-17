
def fact(num):
    if num==0 or num==1:
        return 1
    else:
        return num*fact(num-1)


if __name__ == '__main__':                 #it only executes when you run this particular program from this file only, this line of code will not be executed in Factorial1.py
    print(fact(56))