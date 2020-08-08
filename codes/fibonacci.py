num = int(input("Enter the terms: "))

a=0
b=1

if num<=0:
    print("Please Enter valid term greater than zero!!")
elif num == 1:
    print("Fabonacci series:\n",a,b)
else:
    print("Fabonacci series:")
    while num>0:
        print(a,end=' ')
        c=a+b
        #swapping
        a=b
        b=c
        num-=1
