# Python list common element in two list

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

# Example-1 
cele = []
for i in lst1:
	for j in lst2:
		if i == j:
			cele.append(i)

print("Common Element is: ",cele)