price = {
    "pizza" : 400,
    "burger" : 100,
    "samosa" : 20
}
quantity = {
    "pizza" : 2,
    "burger" : 5,
    "samosa" : 10
}
total_bill = 0

for item in quantity:
    if item in price:
        total_bill += price[item] * quantity[item]

print(total_bill)