# Using word count technique, find the largest 3 frequent used words in Prof Song's speech

import os
#os.chdir('M:/Student/Python_tutorial/Week2/Week2')
os.chdir('C:/Users/KY/Google Drive/CUHKPyTutorial2019/Week2')

handle = open('welcome.txt', encoding="utf-8")
chars = handle.read()
words = chars.split()

wordbag = {}
for word in words:
    wordbag[word] = wordbag.get(word, 0) + 1

sortwordbag = [(v, k) for (k, v) in wordbag.items()]
sortwordbag.sort()
sortwordbag.reverse()
print(sortwordbag[0:3])