import random

lst = [random.randint(1,30) for _ in range(50)]


print(lst)

unique_num = list(set(lst))


print(unique_num)
print(len(unique_num))