from collections import Counter
lst = ["two", "times", "three", "is", "not" ,"four"]
lst1 = ["two", "times", "three", "is", "four"]
res = Counter(lst)
res1 = Counter(lst1)
count=0
for i in res1.keys():
	if i not in res:
		count=0
		print("No")
		break
	elif res1[i] <= res[i]:
		count = 1
	else:
		count = 0
		print("No")
		break
if count == 1:
	print("Yes")
print(res)
print(res1)