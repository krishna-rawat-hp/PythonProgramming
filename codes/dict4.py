# Python dictionary adding element by input

# Example-1 
emp = {"name":"krishna","age":19,"salary":1000,"company":"TCS"}
print("Printing Old Data: ",emp,"\n\n")

print("Reading data...................\n\n")
emp['name'] = input("Name: ")
emp['age'] = int(input("Age: "))
emp['salary'] = int(input("Salary: "))
emp['company'] = input("Company: ")

print("Printing New data: ",emp)