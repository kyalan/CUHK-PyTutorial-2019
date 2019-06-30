# Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters ( hours and  rate).

def computepay(hours, rate):
    if hours>40:
        gross_pay = 40*rate + (hours-40) * rate * 1.5
    else:
        gross_pay = hours*rate
        
    return(gross_pay)
	
# Enter Hours: 45
# Enter Rate: 10 

# Pay: 475.0 (475 = 40 * 10 + 5 * 15)

hours = input('Input the hours:')
hours = float(hours)
rate = input('Input hourly rate:')
rate = float(rate)

print('Gross Pay: $', computepay(hours, rate))

print('End of Program')    