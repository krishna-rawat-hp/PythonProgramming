# String alnum method in python

# Example-1 with simple string
str1 = "Welcome"
print(str1.isalnum())

# Example-2 with numbers and alphabetic string
str2 = "Welcome123"
print(str2.isalnum())

# Example-3 with a space anywhere
str3 = "Welcome 123"
print(str3.isalnum())

# Example-4 with a special character
str4 = "Welcome$121"
print(str4.isalnum())