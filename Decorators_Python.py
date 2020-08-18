# """ Decorators are meant to change the functionality of a function already defined .....

def decorator_function(func):
    num1=int(input("ENTER NUMBER 1: "))
    num2= int(input("ENTER NUMBER 2: "))
    total=func(num1,num2)
    print(total)

@decorator_function
#This is hoe you define a decorator and the function that you call using decorator are written under the decorator function call...

def sum_of_numbers(num1,num2):
    sum=num1+num2
    return sum
