p = float(input("enter physics marks : "))
c = float(input("enter chemistry marks : "))
m = float(input("enter maths marks : "))

total = p + c + m
percentage = (total / 300) * 100
average = total / 3

def get_grade(mark):
    if mark <= 39:
        return 'F'
    elif mark < 44:
        return 'Pass'
    elif mark < 60:
        return 'C'
    elif mark < 75:
        return 'B'
    else:
        return 'A'

p_grade = get_grade(p)
c_grade = get_grade(c)
m_grade = get_grade(m)

print("total marks obtained is :", total)
print("percentage is :", percentage)
print("average is :", average)
print("Physics:", p, "-> Grade:", p_grade)
print("Chemistry:", c, "-> Grade:", c_grade)
print("Maths:", m, "-> Grade:", m_grade)

if p <= 39 or c <= 39 or m <= 39:
    print("student has failed")
else:
    print("student has passed")