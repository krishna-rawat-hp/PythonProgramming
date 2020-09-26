# Python Input a tuple

# Example-1
tup = tuple(input("Enter the tuple Data Here: "))
count = 0
for i in tup:
	print("tup[%d] = %s"%(count,i))
	count+=1
