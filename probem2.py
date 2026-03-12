s1 = {1001 , 1002 , 1003 , 1005}
s2 = {1002 , 1003 , 1005 , 1001, 1004}
print(s1 & s2)
print((s1 - s2) | (s2 - s1))
print(s1 | s2)

if s1 == s1 & s2:
    print(True)
else:
    print(False)