count = 0
for i in range(1, 31):
    for j in range(i, 31):
        k = (i**2 + j**2)**0.5
        if k.is_integer() and k<=30:
            print(f"Pythagorean triplet: ({i}, {j}, {int(k)})")
            count += 1
print(f"Total Pythagorean triplets found: {count}")
