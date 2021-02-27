n,r = 6,3
lst = [1,3,9,9,27,81]
i=2
mid = n//2
count = 0
while(i<n):
	if lst[i-2]*r == lst[i-1] and lst[i-1]*r == lst[i]:
		count+=1
		i+=1
	else:
		if i<=mid:
			count+=i
			i+=2

