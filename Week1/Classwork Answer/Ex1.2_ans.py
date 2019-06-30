# Task 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10 

# Pay: 475.0 (475 = 40 * 10 + 5 * 15)

hours = input('Input the hours:')
hours = float(hours)
rate = input('Input hourly rate:')
rate = float(rate)

if hours>40:
    gross_pay = 40*rate + (hours-40) * rate * 1.5
else:
    gross_pay = hours*rate
print('Gross Pay: $', gross_pay)

print('End of Program')

# Task 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully.

# Enter Hours: 20 
# Enter Rate: nine 
# Error, please enter numeric input

# Enter Hours: forty  
# Error, please enter numeric input

try:
    hours = input('Input the hours:')
    hours = float(hours)
    rate = input('Input hourly rate:')
    rate = float(rate)
    
    if hours>40:
        gross_pay = 40*rate + (hours-40) * rate * 1.5
    else:
        gross_pay = hours*rate
    print('Gross Pay: $', gross_pay)
    
    print('End of Program')    
except:
    print("Error, please enter numeric input")

