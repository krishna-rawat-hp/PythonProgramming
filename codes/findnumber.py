lst = [12,34,56,78,38,26]
count=0
val = 78
for i in lst:
    count+=1
    if i == val:
        print(val," found at ",count," position.")
        break
