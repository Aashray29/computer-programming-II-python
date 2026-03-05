sales1 = {
    "p1" : 200,
    "p2" : 300,
    "p3" : 400,
}
sales2 = {
    "p2" : 500,
    "p4" : 600,
    "p3" : 700,
}
merged = {**sales1 , **sales2}        

for product in sales1:
    if product in sales2:
        merged[product] = sales1[product] + sales2[product]
        
        
print(merged)        
max_product = max(merged , key = merged.get)
print("higest sale product : " , max_product , merged[max_product])

from operator import itemgetter
sorted_dict = dict(sorted(merged.items() , key = itemgetter(1) , reverse = True)) 
print("sorted dictonary : " ,sorted_dict)