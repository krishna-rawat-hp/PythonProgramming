inpmarks = input("Enter marks:  ")
marks = int(inpmarks)
if(marks >= 90):
    print("Excellent!!")
elif(marks<90 or marks>= 75):
    print("Very Good!!")
elif(marks<75 or marks>=60):
    print("Good!!")
else:
    print("Average!!")
