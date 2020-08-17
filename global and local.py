# l = 35  # Global
# def scope():
#     # l=l+45             Cannot change the global variable to do so, check the next statement
#     global l
#     l = l + 45
#     print(l)
#     Global = 55  # local
#     print(Global)
# scope()


global_variable=80

def func1():
    global_variable=20
    print("Before function 2 ",global_variable)
    def func2():
        global global_variable  # changes the global variable
        global_variable = 70
        print("Global Value Now: ",global_variable)
    func2()

func1()
# func2()
