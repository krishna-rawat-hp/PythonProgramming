# Python frozenset by dictionary

# Example-1 dictionary to frozenset
Dictionary = {"Name":"John", "Country":"USA", "ID":101} 
print("Type & Data: ",type(Dictionary),"  ",Dictionary)
fs = frozenset(Dictionary)
print("Type & Data: ",type(fs),"  ",fs)
