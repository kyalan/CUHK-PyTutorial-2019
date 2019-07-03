# List
print([1, 24, 76])
print(['red', 'yellow', 'blue'])
print(['red', 24, 98.6])
print([ 1, [5, 6], 7])
print([])

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:',  friend)
print('Done!')
print(friends[1])
print(len(friends))
print(range(len(friends)))

for i in range(len(friends)):
    print('Happy New Year:',  friends[i])
	
friends.sort()
print(friends)
friends.reverse()
print(friends)
	
# List Concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(a)

# List Slicing
t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]
print(len(t), max(t), min(t), sum(t), sum(t)/len(t))

# List as a container
stuff = []
# or stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

# check element in the list
some = [1, 9, 21, 10, 16]
9 in some
15 in some
20 not in some

# string.split
line = 'With three words'
stuff = line.split()
print(stuff)
line = 'A lot               of spaces'
print(line.split())
line = 'first;second;third'
print(line.split())
print(line.split(';'))

#############################
# Exercise --> Ex2.1.py
# List exercise, Re-do: getting R2
###############################

# Tuple
x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = ( 1, 9, 2 )
print(y)
print(max(y))

numlist = [9, 8, 7]
numlist[2] = 6
print(numlist)
numtuple = (5, 4, 3)
numtuple[2] = 0

numtuple.sort()
numtuple.append(5)
numtuple.reverse()

type(numlist)
dir(numlist)
type(numtuple)
dir(numtuple)

# multiple assignment
(x, y) = (4, 'fred')
print(y)
a, b = (99, 98)
print(a)

# Comparison
(0, 1, 2) < (5, 1, 2)
(0, 1, 2000000) < (0, 3, 4)
( 'Jones', 'Sally' ) < ('Jones', 'Sam')
( 'Jones', 'Sally') > ('Adams', 'Sam')

# Dictionary
purse = {}
# or purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

jjj = { 'chuck' : 1 , 'fred' : 42, 'jan': 100}
print(jjj)

# Counting Example
ccc = {'csev':1, 'cwen':2}
print(ccc)
print(ccc['cmen'])
'csev' in ccc

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    if name not in counts: 
		counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)

counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names :
    counts[name] = counts.get(name, 0) + 1
print(counts)

#############################
# Exercise --> Ex2.3.py
# Word Count (from Welcome from Song XY)
###############################

# Notes in pptx
# DS water blow

# Map
store1 = [10.00, 11.00, 12.34, 2.34]
store2 = [9.00, 11.10, 12.34, 2.01]
cheapest = map(min, store1, store2)
print(cheapest)

# Lambda functions
def wmin(x, y):
	return (min(x*2.0, y*3.0))
print(map(wmin, store1, store2))
print(map(lambda x, y: min(x*2.0, y*3.0), store1, store2))

# List Comprehension
my_list = []
for number in range(1000):
    if number % 2 == 0:
        my_list.append(number)
print(my_list)

my_list2 = [number for number in range(1000) if number % 2 == 0]
print(my_list2)

friends = ['Joseph', 'Glenn', 'Sally']
for friend in friends :
    print('Happy New Year:',  friend)
[print('Happy New Year:',  friend) for friend in friends]

# Dictionary Comprehension
cabins = ['First Class', 'Business', 'Economy']
nchar_cabins = {cabin: len(cabin) for cabin in cabins}
print(nchar_cabins)

#############################
# Exercise --> Ex2.4.py
###############################

# detailed explanation to pandas in pptx

import pandas as pd
# Series

# from List
cabins = ['First Class', 'Business', 'Economy']
pd.Series(cabins)
numbers = [1, 2, 3]
pd.Series(numbers)
cabins = [None, 'Business', 'Economy']
pd.Series(cabins)
numbers = [None, 2, 3]
pd.Series(numbers)
# from dictionary
hub_cities = {'CX': 'Hong Kong',
          'CI': 'Taipei',
          'NH': 'Tokyo',
          'SQ': 'Singapore'}
s = pd.Series(hub_cities)
print(s)
print(s.index)
print(s[0])
print(s['CX'])

s2 = pd.Series(cabins)
print(s2.shape)
print(len(s2))
print(type(s2))

# DataFrame
import pandas as pd
ticket_1 = pd.Series({'Name': 'Ben',
                        'Destination': 'Maldives',
                        'Price': 14610.0})
ticket_2 = pd.Series({'Name': 'Julian',
                        'Destination': 'San Francisco',
                        'Price': 3480.0})
ticket_3 = pd.Series({'Name': 'Tony',
                        'Destination': 'Shanghai',
                        'Price': 880.00})
df = pd.DataFrame([ticket_1, ticket_2, ticket_3])
df.head()

df['Price']
type(df['Price'])
df[['Name', 'Price']]
type(df[['Name', 'Price']])
df.loc[:,['Name', 'Price']]
df.iloc[0,1]

df['Flight Date'] = None
print(df)
prices = df['Price']
prices += 160
print(prices)

#############################
# Exercise --> Ex2.5.py
# Assignment 2
###############################