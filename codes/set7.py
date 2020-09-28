# Python set deletion

# Example-1 using discard() method
set1 = {"january","february","march","april","may","june","july","august","september"}
print("set before deletion: ",set1)
set1.discard("may")
set1.discard("july")
print("set after deletion: ",set1)
print("\n")

# Example-2 using remove() method
print("before using remove: ",set1)
set1.remove("march")
print("after using remove: ",set1)
print("\n")

# Example-3 using pop() method
print("before using pop: ",set1)
set1.pop()
set1.pop()
print("after using pop: ",set1)
print("\n")

# Example-4 remove() vs discard() method
print("with discard: ",set1.discard("jan")) # it does not occur error
print("with remove: ",set1.remove("jan"))	# it occur an error