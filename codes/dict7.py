# Python dictionary iteration

dict1 = {"Name":"krishna","age":19,"prof.":"student"}

# Example-1 iterate dictionary keys
for x in dict1:
	print(x)

# Example-2 iterate dictionary elements
for x in dict1:
	print(dict1[x])

# Example-3 iterate dictionary elements by values() method
for x in dict1.values():
	print(x)

# Example-4 iterate dictionary elements by items() method
for x in dict1.items():
	print(x)
