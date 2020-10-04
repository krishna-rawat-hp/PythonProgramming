# Python dictionary some other methods

dict1 = {1:"aaa",2:"bbb",3:"ccc"}

# Example-1  copy() method
dict2 = dict1.copy()
print("copy of dict1: ",dict2)

# Example-2 fromkey() method
x = ('key1',"key2","key3")
y = 1,2,3
dict3 = dict.fromkeys(x,y)
print("\n dictionary:",dict3)

# Example-3 get() method
x = dict1.get(2)
print("\n value: ",x)

# Example-4 setdefault() method
x = dict1.setdefault(2,"bbbb")
print("\n default value: ",x)

# Example-5 update() method
dict11 = {4:"ddd"}
dict1.update(dict11)
print("\n dict1: ",dict1)

# Example-6 popitem() method
dict1.popitem()
pr	int("\n Dict1: ",dict1)