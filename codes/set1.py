# Python set creating

# Example-1 using {} curly braces
set1 = {"sunday","monday","tuesday","wednesday","thursday","friday","saturday"}
print("Type of set 1: ",type(set1))
count = 0
for i in set1:
	print("index[%d] = %s"%(count,i))
	count+=1

# Example-2 using set() method
set2 = set(["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
print("Type of set 2: ",type(set2))
count = 0
for i in set2:
	print("index[%d] = %s"%(count,i))
	count+=1
