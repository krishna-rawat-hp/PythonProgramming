n = 5
arr = [[1,2,100],[2,5,100],[3,4,100]]
lst = [0 for i in range(n)]
l = len(arr)
i=0
while(i<l):
	val = arr[i][2]
	for j in range(arr[i][0], arr[i][1]+1):
		lst[j-1] += val 
	i+=1
m = max(lst)
print(m)