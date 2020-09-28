# Python set some other inbuilt methods

# Example-1 Clear() Method
set1 = {1,2,3,4,5}
print("Before clear() method: ",set1)
set1.clear()
print("After clear() method: ",set1)

# Example-2 copy() Method
set2 = {1,2,3,4,5}
print("set2 :",set2)
set3 = set2.copy()
print("Set3 (A Copy of set2): ",set3)

# Example-3 difference_update() method
s1 = {1,2,3,4,5}
s2 = {3,4,5,6}
s1.difference_update(s2)
print("difference_update: ",s1)

# Example-4 isdisjoint() method
a = {1,2,3,4}
b = {5,6,7,8}
print("Disjoint: ",a.isdisjoint(b))

# Example-5 issubset() method
x = {1,2,3,4,5,6,7,8,9}
y = {2,3,4,5}
print("issubset: ",y.issubset(x))

# Example-6 issuperset() method
print("issuperset: ",x.issuperset(y))

# Example-7 symmetric_difference_update() method
set1 = {"Krishna","Hemant","Raja","Atul","mehta"}
set2 = {"Rahul","Mohan","Krishna","Hemant"}
set1.symmetric_difference_update(set2)
print("symmetric_difference_update: ",set1)
