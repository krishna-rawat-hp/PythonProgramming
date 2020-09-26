# Python list VS tuple eay debugging

# Example-1
lst = [1,2,3,4,5,6]
tup = (1,2,3,4,5,6)

print("List Element: ",lst)
print("Tuple Element: ",tup)
lst1=lst
lst[3] = 5
print("List1: ",lst1)
print("List: ",lst)

tup1 = tup
print("Tuple1: ",tup1)
tup[3] = 5
print("Tuple: ",tup)