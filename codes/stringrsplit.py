# String rstrip method in python

# Example-1 simple split
str1 = "python is a programming language"
print(str1.rsplit())

# Example-2 seprate by seprator
sep = "python"
print(str1.rsplit(sep))

# Example-3 limited split
print(str1.rsplit("a",1))
print(str1.rsplit("a",3))
