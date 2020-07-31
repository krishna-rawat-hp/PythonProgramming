def fun_Generator():
    yield 1
    yield 2
    yield 3
    yield 4

# Driver code to check above generator function
for i in fun_Generator():
    print(i)
