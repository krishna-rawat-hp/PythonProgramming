# Python List remove duplicate values

lst = [11,23,45,67,45,32,35,33,32,45,67]
print("Before: ",lst)
# Example-1
lst1 = []
for i in lst:
	if i not in lst1:
		lst1.append(i)

print("After: ",lst1)


