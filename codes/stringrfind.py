# String rfind method in python

# Example-1 single parameter
s1 = " Hello this is krishna kant rawat"
print(s1.rfind("krishna"))
print(s1.rfind("are"))

# Example-2 string with double parameter
print(s1.rfind("krishna",10))
print(s1.rfind("krishna",21))

# Example-3 string with triple parameter
print(s1.rfind("krishna",10,25))
print(s1.rfind("krishna",10,15))

# Example-4 string with single word
print(s1.rfind("a"))