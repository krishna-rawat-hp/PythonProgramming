# Python function call by reference

# Example-1 passing mutable Object list
def mutablefunc(lst):
	lst.append(20)
	lst.append(30)
	print("Inner List:",lst)

lst = [10,20,40,50,60]

mutablefunc(lst)
print("Outer List:",lst)

# Example-2 passing immutable object string
def immutablefunc(str):
	str = str+" Krishna"
	print(str)

str = "hello"
immutablefunc(str)
print(str)

