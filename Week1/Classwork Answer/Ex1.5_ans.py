# Take the following Python code that stores a string:
str_coeff = 'R-Sq-Coefficient:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.

colon_at = str_coeff.find(':')
coeff = float(str_coeff[(colon_at+1):])
print('coeff =', coeff, type(coeff))
