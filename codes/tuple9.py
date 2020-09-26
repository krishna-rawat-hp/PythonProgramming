# Python tuple operators

tup1 = (1,2,3,4)
tup2 = (5,6,7,8)

# Example-1 * Repeatation operator
print("tup1 * 2 :", tup1*2)

# Example-2 + Concatination operator
print("tup1 + tup2 : ", tup1+tup2)

# Example-3 (in) exist or not in tuple operator
print("2 in tup1 : ",2 in tup1)
print("2 in tup2 : ",2 in tup2)

# Example-4 tuple iteration operator
for i in tup1:
	print(i)

# Example-5 tuple length operator 
print("tup1 length: ", len(tup1))
print("tup2 length: ", len(tup2))