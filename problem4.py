def sum_avg(m1,m2,m3,m4,m5):
    total = m1 + m2 + m3 + m4 + m5
    avg = total / 5

    return("total :",total  , "avg: ",avg)

m1,m2,m3,m4,m5 = map(int , input("enter 5 subjects marks : ").split())
print(sum_avg(m1,m2,m3,m4,m5))
