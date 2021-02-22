lst = [1,4,6,3,9,2]
lst2 = lst[1::]
i=1
lst1 = list(map(lambda x,y : abs(x-y),lst,lst2))
print(lst1)