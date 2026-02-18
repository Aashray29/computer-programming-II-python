s = input("Enter a string: ")
alphabet_count = 0  
digit_count = 0
for char in s:
    if char.isalpha():
        alphabet_count += 1
    elif char.isdigit():
        digit_count += 1
print("Number of alphabets:", alphabet_count)
print("Number of digits:", digit_count)

