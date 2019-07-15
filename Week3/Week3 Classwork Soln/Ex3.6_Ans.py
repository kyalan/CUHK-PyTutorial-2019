# More exercises for NumPy
https://pynative.com/python-numpy-exercise/
https://www.machinelearningplus.com/python/101-numpy-exercises-python/

# Selected Exercise
import numpy as np

# Create a 5X2 integer array from a range between 100 to 200 such that the difference between each element is 10
print("Creating 5X2 array using numpy.arange")
sampleArray = np.arange(100, 200, 10)
sampleArray = sampleArray.reshape(5,2)
print(sampleArray)

# Add the following two NumPy arrays and Modify a result array by calculating the square root of each element
arrayOne = np.array([[5, 6, 9], [21 ,18, 27]])
arrayTwo = np.array([[15 ,33, 24], [4 ,7, 1]])

resultArray  = arrayOne + arrayTwo
print("addition of two arrays is \n")
print(resultArray)
print("squart root of two arrays is \n")
sqrtArray = np.sqrt(resultArray)
print(sqrtArray)

# Following is the 2-D array. Print max from axis 0 and min from axis 1
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])

minOfAxisOne = np.amin(sampleArray, 1) 
print("Printing amin Of Axis 1")
print(minOfAxisOne)
maxOfAxisOne = np.amax(sampleArray, 0) 
print("Printing amax Of Axis 0")
print(maxOfAxisOne)