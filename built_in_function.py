# a=10
# b=20
# print(sum((a,b))) #This is a builtin function, ctrl+left click to access it in the builtin.py file

"""Function in python language"""

def largest(num1,num2,num3):
    """This is a largest of three function and works with 3 variables
  ******** Please donot manipulate *****************"""
    if(num1>num2 & num1>num3):
        return  num1
    elif(num2>num3 & num2>num1):
       return num2
    else:
       return num3

print(largest(12,13,14))
print(largest.__doc__) #This statement prints the doctype of the function.....(if exists) else it prints NONE