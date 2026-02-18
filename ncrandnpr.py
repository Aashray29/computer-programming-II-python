n = int(input('Enter n: '))
if n < 0:
    print("Negative numbers are not allowed.")  
r = int(input('Enter r: '))
if r < 0:
    print("Negative numbers are not allowed.")
if r > n:
    print("r cannot be greater than n.")
else:
    from math import factorial
    nCr = factorial(n) // (factorial(r) * factorial(n - r))
    nPr = factorial(n) // factorial(n - r)
    print(f"{n}C{r} = {nCr}")
    print(f"{n}P{r} = {nPr}")
    