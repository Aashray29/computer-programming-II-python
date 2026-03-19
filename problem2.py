def compute(n):
    sum = 0

    for i in range(1,5):
        sum += int(str(n) * i)


    return sum


for n in range(4,8):
    print(f"{n} + {n}{n} + {n}{n}{n} + {n}{n}{n}{n} = {compute(n)}")