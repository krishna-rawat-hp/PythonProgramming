n = int(input("Enter the size of list: "))
i=0
lst = list()
while n>0:
    i+=1
    print("Enter ",i," Number: ")
    lst.append(int(input()))
    n-=1

sum = 0
for val in lst:
    sum = sum+val
print("Sum of list is: ",sum)
