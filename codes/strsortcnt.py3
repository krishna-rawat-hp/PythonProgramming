from collections import Counter
strg = "baccc"
strg1 = "bbaaccc"
sortedstr = ''.join(sorted(strg))
print(sortedstr)
occ_cnt = Counter(sortedstr)
val = occ_cnt.values()
min_val = min(val)
dec_val = 0
flag = 1
for i in occ_cnt.values():
	if i>min_val:
		dec_val+=1
	if dec_val>1 or (i-min_val)>1:
		flag = 0
		print("invalid")
		break
lap_id = ""
if(flag==1):
	for i in occ_cnt.keys():
		lap_id += i*min_val
	print(lap_id)