# Q.1
# Write a program that 
# 1. prompts the user for inputting a list of numbers, and 
# 2. end when the user enters “done”.
# 3. prints out the maximum and minimum of the numbers.
nums = []
while True:
	num = input('Input a number:')
	if num == 'done':	break
	nums.append(float(num))
print('max =', max(nums))
print('min =', min(nums))


# Q.2
# Take the following Python code that stores a string:
str = 'R-Sq-Coefficient:0.8475'
# Extract the R2 again, but this time using str.split and list functions.

R2 = float(str.split(':')[1])
print('R2 =', R2)