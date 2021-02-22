from collections import Counter
str1 = "hi"
str2 = "world"
res1 = Counter(str1)
res2 = Counter(str2)
c=0
for i in res1.keys():
	if i in res2:
		c = 1
		print("YES")
		break
	else:
		c=0
if c == 0:
	print("NO")