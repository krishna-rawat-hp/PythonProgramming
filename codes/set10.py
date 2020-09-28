# Python set operations

# Example-1 intersection_update of two sets using intersection_update() operator
set1 = {"Krishna","Hemant","Raja","Atul","mehta"}
set2 = {"Rahul","Mohan","Krishna","Hemant"}
set3 = {"Krishna","Ajeet","Mohit","Arun"}
set1.intersection_update(set2, set3)
print("Intersection_update of sets : ",set1) # it is not create extra set for store intersection

