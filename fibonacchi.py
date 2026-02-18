n = int(input("enter the number : "))
num = 0
count = 1
print(num)  # Print 0th term
for i in range(n-1):
    temp = num
    num = num + count
    count = temp
    print(num)  # Print subsequent terms
    
    