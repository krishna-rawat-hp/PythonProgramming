# String replace method in python

# Example-1 simple replace
str1 = "Java is a good programming language"
print("old string:", str1)
print("new string:", str1.replace("Java","Python"))

# Example-2 multi replace
str2 = "C C++ JAVA C# JAVA PYTHON C# JAVA"
print("old string:", str2)
print("new string:", str2.replace("JAVA", "PYTHON"))

# Example-3 counted replaces
count = 1
print("old string:", str2)
print("new string:", str2.replace("JAVA", "PYTHON", count))

# Example-3 replace whole string
str3 = "adfgf hgf jhfsj"
strr = "Krishna Kant Rawat"
print("old string:", str3)
print("new string:", str3.replace(str3, strr))