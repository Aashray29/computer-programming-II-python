n = int(input("enter num : "))
lst1 = []

for i in range(n):
    c = float(input())
    lst1.append(c)
    
    
lst2 = [round((i*1.8) + 32 , 2)  for i in lst1]

print(lst1)
print(lst2)