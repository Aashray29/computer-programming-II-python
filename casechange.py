str = input("enter string : ")
def lowercase(str):
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            print(chr(ord(str[i]) + 32), end='')
        else :
            print(str[i], end='')
    print()

lowercase(str)

def uppercase(str):
    for i in range(len(str)):
        if str[i] >= 'a' and str[i] <= 'z':
            print(chr(ord(str[i]) - 32), end='')
        else :
            print(str[i], end='')
    print()

uppercase(str)

def togglecase(str):
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z':
            print(chr(ord(str[i]) + 32), end='')
        elif str[i] >= 'a' and str[i] <= 'z':
            print(chr(ord(str[i]) - 32), end='')
        else :
            print(str[i], end='')
    print()

togglecase(str)
            