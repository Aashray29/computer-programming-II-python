import random

lst = [random.randint(-50,50) for _ in range(30)]


print(lst)


positive = [num for num in lst if num > 0]
negative = [num for num in lst if num < 0]


print(positive)
print(negative)
