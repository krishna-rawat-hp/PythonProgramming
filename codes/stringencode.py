# String encode method in python

# Example-1 Simple string encoding
s1 = "HELLO"
s1e = s1.encode()
print("simle string:",s1)
print("encoded string:",s1e)

# Example-2 special character string
s2 = "HËLLO"
s2e = s2.encode()
print("simle string:",s2)
print("encoded string:",s2e)

# Example-3 special character into ascii with ignore attribute
s4 = "HËLLO"
s4e = s4.encode("ascii","ignore")
print("simle string:",s4)
print("encoded string:",s4e)

# Example-4 special character into ascii with replace attribute
s5 = "HËLLO"
s5e = s5.encode("ascii","replace")
print("simle string:",s5)
print("encoded string:",s5e)

# Example-5 special character into ascii
s3 = "HËLLO"
s3e = s3.encode("ascii")
print("simle string:",s2)
print("encoded string:",s3e)