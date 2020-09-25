# Python list uncommon elements in two list

lst1 = [1,2,3,4,5]
lst2 = [4,5,6,7,8]

# Example-1 
ucele = []
for i in range(0,len(lst1)-1):
	if(lst1[i] not in lst2):
		ucele.append(lst1[i])

print("Uncommon Element is: ",ucele)