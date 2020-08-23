# String format method in python

# Example-1 format with {}
str1 = "java"
str2 = "python"
str = "{} and {} are good languages".format(str1,str2)
print(str)

# Example-2 format with {index}
strin = "{1} is easy compare to {0}.".format(str1,str2)
print(strin)

# Example-3 format with number system
val = 10
print("Decimal value is {0:d}".format(val))
print("Hexadecimal value is {0:x}".format(val))
print("Octal value is {0:o}".format(val))
print("Binary value is {0:b}".format(val))

# Example-4 format with {:,}
val1 = 100000000
print("Simple value {} VS Comma seprated value {:,}".format(val1,val1))

# Example-5 format percentage 
fval = 59/9
print("Original value {} VS formated value {:.2%}".format(fval,fval))
