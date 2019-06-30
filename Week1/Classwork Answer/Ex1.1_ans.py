# Write a program to prompt the user for hours and rate per hour to compute gross pay.

hours = input('Input the hours:')
hours = float(hours)
rate = input('Input hourly rate:')
rate = float(rate)
print('Gross Pay: $', hours*rate)

print('End of Program')