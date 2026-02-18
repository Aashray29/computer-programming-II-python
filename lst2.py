import random

lst = [random.randint(1,100) for _ in range(20)]


print(lst)

n= int(input("enter number: "))

positions = []

for i in range(len(lst)):
    if lst[i] == n:
        positions.append(i)

print(positions)