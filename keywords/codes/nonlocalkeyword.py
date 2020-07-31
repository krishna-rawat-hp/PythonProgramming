def outside_function():
    a = 20
    def inside_function():
        nonlocal a #it create a value as global
        a = 30
        print("Inner function: ",a)
    inside_function()
    print("Outer function: ",a)
outside_function()
