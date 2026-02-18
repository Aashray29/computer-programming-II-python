odd1 = []
even2 = []

import random

while(len(odd1))  < 5:
    
 x = random.randint(1,100)
 if x % 2 != 0 :
    odd1.append(x)

        
print(odd1)


while(len(even2)) < 4:
    
    
 x = random.randint(1,100)    
 if x % 2 == 0:
     even2.append(x)
     
     
print(even2)


odd1[2] = even2

print(odd1)


flattened_lst = []

for items in odd1:
    if isinstance(items,list):
        flattened_lst.extend(items)
    else:
        flattened_lst.append(items)
        
        
print(flattened_lst)

flattened_lst.sort()

print(flattened_lst)
        