# String join method in python

# Example-1 join list
lst = ["k","r","i","s","h","n","a"]
strc = ""
str1 = strc.join(lst)
print(str1)

# Example-2 join dictionary
dic = {'key1':1,'key2':2}
strc2 = "&"
str2 = strc2.join(dic)
print(str2)

# Example-3 join tuple
tup = ("abc", "bcd", "cde")
strc3 = "-"
str3 = strc3.join(tup)
print(str3.join(tup))

# Example-4 join set
st = {'01','30','44'}
strc4 = ":"
str4 = strc4.join(st)
print(str4)

# Example-5 error condition
lst1 = ['3',4,'5']
strc5 = "-"
str5 = strc5.join(lst1)
print(str5)