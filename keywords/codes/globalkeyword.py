def func1():
    global a
    a = 10
    b = 20
    print(a+b)
func1()
b=30
print(a+b)
