# Python list adding element

lst = []
print("List beafore adding elements: ",lst)
# Example-1 simple addition of element in list
lst.append(1)

# Example-2 multiple element adding in list
n = int(input("Enter How much element you want to add: "))
for i in range(1,n+1):
	lst.append(int(input("Enter The Number:")))

print("List after adding elements :",lst)