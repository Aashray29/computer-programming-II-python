str = input("enter the string : ")
words = str.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
        
        
print(freq)