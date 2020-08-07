rows = int(input("Enter number of rows: "))

for i in range(0, rows+1):
    for j in range(i):
        print(i,end='')
    print()
