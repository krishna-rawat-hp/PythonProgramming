# Python dictionary deleting element and dictionary

# Example-1 deleting some element
emp = {"name":"krishna","age":19,"salary":1000,"company":"TCS"}
print("printing initial data: ",emp)
del emp['name']
del emp['age']
print("after deleting data: ",emp)
print("deleting dictionary:")
del emp
print("deleting dictionary:",emp)