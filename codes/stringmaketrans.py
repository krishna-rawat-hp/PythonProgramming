 # String maketrans method in python

 # Example-1 

intab = "aeiou"
outtab = "12345"

trnstab = str.maketrans(intab, outtab)

str = "this is string example .... wow!!!"
print(str.translate(trnstab))