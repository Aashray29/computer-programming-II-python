def count_lower_upper(str):
    count = 0
    for i in str:
        if i>='A' and i <='Z':
            count += 1

    return {"count of uppper is : " : count ,
             "and count of lower is : " : len(str) - count - str.count(" ")}
            

str = input("enter the string  :")

print(count_lower_upper(str))