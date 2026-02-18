x = float(input("Enter x coordinate of center: "))
y = float(input("Enter y coordinate of center: "))
r = float(input("Enter radius: "))
x1 = float(input("Enter x coordinate of point: "))
y1 = float(input("Enter y coordinate of point: "))
if (x1 - x) ** 2 + (y1 - y) ** 2 < r ** 2:
    print("Point is inside the circle")
elif (x1 - x) ** 2 + (y1 - y) ** 2 == r ** 2:
    print("Point is on the circle")
else:
    print("Point is outside the circle")    