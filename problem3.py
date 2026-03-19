def create_array(r,c,d,n):
    arr = [[[n for i in range(d)] for j in range(c)] for k in range(r)]
    return arr


print(create_array(1,4,1,10))