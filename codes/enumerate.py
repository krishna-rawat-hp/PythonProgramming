# lst = [1, 2, 5, 3, 7, 8, 6, 4]
# lst = [p-1 for p in lst]
# for i,p in enumerate(lst):
# 	print(i,p)
lst = [4,3,1,2]
sortarr = sorted(lst)
count=0
index_dict = {c: i for i,c in enumerate(lst)}
for i,v in enumerate(lst):
	ind = sortarr[i]
	if(v!=ind):
		count+=1
		indv = index_dict[ind]
		lst[indv],lst[i] = lst[i],lst[indv]
		index_dict[v] = indv
		index_dict[ind] = i

print(count)