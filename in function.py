str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str2 in str1:
    result = str1.replace(str2, "")
    print("Result after removing:", result)
else:
    print("No, second string is not present in first string")    