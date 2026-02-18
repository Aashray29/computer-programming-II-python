s = input("enter the string : ")
n = len(s)
if n == 0:
    print("String is empty")
elif n == 1:
    print("First, Middle and Last character is:", s[0])
else:
    firstchar = s[0]
    lastchar = s[n-1]
    print("First character is:", firstchar)
    print("Last character is:", lastchar)   
    if n % 2 != 0:
        middlechar = s[n//2]
        print("Middle character is:", middlechar)
    else:
        print("String has no middle character")