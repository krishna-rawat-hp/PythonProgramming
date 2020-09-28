# Python set operations

# Example-1 symmetric_difference of two sets using ^ operator
set1 = {"Krishna","Hemant","Raja","Atul","mehta"}
set2 = {"Rahul","Mohan","Krishna","Hemant"}
print("symmetric_difference of two sets (^): ",set1^set2)

# Example-2 symmetric_difference of two sets using symmetric_difference() method
print("symmetric_difference of two set (symmetric_difference()): ",set1.symmetric_difference(set2))
