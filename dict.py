dict1 = { 1 : {50 : 5000, 25 : 2000, 32 : 65000}, 2 : {28 : 366666 , 30 : 8000000, 36 : 90000} } 
for dept,emp_data in dict1.items():
    salary = emp_data.values()

    min_salary = min(salary)                                                                                       
    max_salary = max(salary)   

    print(min_salary)
    print(max_salary)