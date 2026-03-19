def func(n):
    lst = [(i , i**2 , i**3) for i in range(1,n+1)]

    return lst


n = int(input())
print(func(n))