# string splitlines methos in python

# Example-1 simple split
str1 = "python is a programming language"
print(str1.splitlines())

# Example-2 \n and \r string
str2 = "Python \n is a \r programming \n language"
print(str2.splitlines())

#Example-4 \n and \r with keepeds true
print(str2.splitlines(True))