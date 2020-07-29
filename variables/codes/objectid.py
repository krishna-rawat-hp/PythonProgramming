#declare and define two variables
a=50
b=a
print("Value of a: ", a)
#printing id of variable a
print("Id of a: ", id(a))
print("Value of b: ", b)
#printing id of variable b
print("Id of b: ", id(b))

#reassigning the value of variable a
a=100
print("After change value of a: ", a)
print("After change Id of a: ", id(a)) 
