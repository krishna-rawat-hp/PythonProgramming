def func1():
    global a # it make a accesible anywhere in program
    a = 10
    b = 20
    print(a+b)
func1()
b=30
print(a+b)
