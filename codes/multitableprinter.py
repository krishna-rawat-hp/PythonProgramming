n=2
while 1:
    i=1
    while i<=10:
        print("%d X %d = %d"%(n,i,n*i))
        i+=1
    choice = int(input("Enter 1 for next table 0 to stop? "))
    if choice == 0:
        break
    n+=1
