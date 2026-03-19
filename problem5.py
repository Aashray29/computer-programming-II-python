def ispanagram(str):
    set1 = set(str.lower())

    frq = [0] * 26

    for ch in set1:
        frq[ord(ch) - ord('a')] += 1

    for i in range(26):
        if frq[i] == 0:
            return False
            break
        
    
    return True

str = input("enter the string : ")
print(ispanagram(str))