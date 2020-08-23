# String find method in python

# Example-1 single parameter
s1 = " Hello this is krishna kant rawat"
print(s1.find("krishna"))
print(s1.find("are"))

# Example-2 string with double parameter
print(s1.find("krishna",10))
print(s1.find("krishna",21))

# Example-3 string with triple parameter
print(s1.find("krishna",10,25))
print(s1.find("krishna",10,15))

# Example-4 string with single word
print(s1.find("a"))