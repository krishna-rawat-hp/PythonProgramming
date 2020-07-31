a = 0
try:
    c = 1/a
    print(c)
except Exception as e:
    print(e)
finally:
    print("Finally always Execute!")
